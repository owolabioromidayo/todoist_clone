from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError


class AddTask(FlaskForm):
    taskname = StringField('', validators=[DataRequired()])
    submit = SubmitField('Add Task')


class AddTaskList(FlaskForm):
    tasklistname = StringField('',  validators=[DataRequired()])
    submit = SubmitField('Add Project')


class UpdateTaskList(FlaskForm):
    new_tasklistname = StringField('',  validators=[DataRequired()])
    submit = SubmitField('Update Project Name')


class UpdateTask(FlaskForm):
    new_taskname = StringField('',  validators=[DataRequired()])
    submit = SubmitField('Add Project')
