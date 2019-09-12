from myproject import app, db
from myproject.models import Tasklist, Task
from myproject.forms import AddTask, AddTaskList, UpdateTask, UpdateTaskList
from flask import render_template, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def home():

    addtasklist = AddTaskList()
    addtasklist.run()

    forms = {'addtasklist': addtasklist}
    tasklists = Tasklist.query.all()

    return render_template('home.html', tasklists=tasklists, forms=forms)


@app.route('/tasklist/<id>', methods=['GET', 'POST'])
def tasklist(id):

    tasklist = Tasklist.query.get(id)
    tasklists = Tasklist.query.all()

    # FORMS
    addtasklist = AddTaskList()
    addtasklist.run()

    addtask = AddTask()
    addtask.run(tasklist)

    forms = {'addtasklist': addtasklist, 'addtask': addtask}

    return render_template('tasklist.html', tasklists=tasklists, forms=forms, tasklist=tasklist)


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

    return redirect(url_for('tasklist', id=tasklist.id))


@app.route('/update/<id>', methods=['GET', 'POST'])
def update_tasklist(id):

    tasklists = Tasklist.query.all()

    addtasklist = AddTaskList()
    addtasklist.run()

    updatetasklist = UpdateTaskList()
    if updatetasklist.validate_on_submit():

        updatetasklist.run(id)

        return redirect(url_for('tasklist', id=id))

    forms = {'updatetasklist': updatetasklist, 'addtasklist': addtasklist}

    return render_template('update_tasklist.html', forms=forms, tasklists=tasklists)


@app.route('/updatetask/<taskid>', methods=['GET', 'POST'])
def update_task(taskid):
    tasklists = Tasklist.query.all()
    addtasklist = AddTaskList()
    addtasklist.run()

    updatetask = UpdateTask()
    if updatetask.validate_on_submit():
        task = Task.query.get(taskid)
        updatetask.run(task)

        return redirect(url_for('tasklist', id=task.tasklist.id))

    forms = {'updatetask': updatetask, 'addtasklist': addtasklist}

    return render_template('update_task.html', forms=forms, tasklists=tasklists)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
