from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError
# for form running
from myproject import app, db
from myproject.models import Tasklist, Task
from flask import render_template, redirect, url_for


class AddTask(FlaskForm):
    taskname = StringField('', validators=[DataRequired()])
    submit = SubmitField('Add Task')

    def run(self, tasklist):
        if self.validate_on_submit():
            newtask = Task(self.taskname.data, tasklist.id)
            db.session.add(newtask)
            db.session.commit()

            return redirect(url_for('tasklist', id=tasklist.id))


class AddTaskList(FlaskForm):
    tasklistname = StringField('',  validators=[DataRequired()])
    submit = SubmitField('Add Project')

    def run(self):
        if self.validate_on_submit():
            newtasklist = Tasklist(self.tasklistname.data)
            db.session.add(newtasklist)
            db.session.commit()

            return redirect(url_for('home'))


class UpdateTaskList(FlaskForm):
    new_tasklistname = StringField(
        'New Project Name here:',  validators=[DataRequired()])
    submit = SubmitField('Update Project Name')

    def run(self, id):
        tasklist = Tasklist.query.get(id)
        tasklist.name = self.new_tasklistname.data
        db.session.add(tasklist)
        db.session.commit()


class UpdateTask(FlaskForm):
    new_taskname = StringField('',  validators=[DataRequired()])
    submit = SubmitField('Update Task')

    def run(self, task):
        if self.validate_on_submit():
            task.name = self.new_taskname.data
            db.session.add(task)
            db.session.commit()
