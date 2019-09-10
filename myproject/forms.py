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
