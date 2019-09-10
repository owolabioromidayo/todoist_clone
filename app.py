from myproject import app, db
from myproject.models import Tasklist, Task
from myproject.forms import AddTask, AddTaskList
from flask import render_template, redirect, url_for


def tasklistform(addtasklist):
    if addtasklist.validate_on_submit():
        newtasklist = Tasklist(addtasklist.tasklistname.data)
        db.session.add(newtasklist)
        db.session.commit()

        return redirect(url_for('home'))


@app.route('/', methods=['GET', 'POST'])
def home():

    addtasklist = AddTaskList()
    tasklistform(addtasklist)

    return render_template('home.html', tasklists=Tasklist.query.all(), addtasklist=addtasklist)


@app.route('/tasklists/<id>', methods=['GET', 'POST'])
def tasklists(id):

    addtasklist = AddTaskList()
    tasklistform(addtasklist)

    tasklist = Tasklist.query.get(id)
    tasks = tasklist.tasks

    addtask = AddTask()

    if addtask.validate_on_submit():
        newtask = Task(addtask.taskname.data, tasklist.id)
        db.session.add(newtask)
        db.session.commit()

        return redirect(url_for('tasklists', id=id))

    return render_template('tasklists.html', name=tasklist.name, tasks=tasks, tasklists=Tasklist.query.all(), addtasklist=addtasklist, addtask=addtask, tasklist=tasklist)


@app.route('/delete/<id>')
def delete(id):
    tasklist = Tasklist.query.get(id)
    db.session.delete(tasklist)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/deltask/<taskid>')
def deltask(taskid):
    task = Task.query.get(taskid)
    tasklist = task.tasklist
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('tasklists', id=tasklist.id))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
