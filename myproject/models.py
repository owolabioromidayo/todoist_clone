from myproject import db


class Tasklist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    tasks = db.relationship('Task', backref='tasklist', lazy='dynamic')

    def __init__(self, name):
        self.name = name


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    tasklist_id = db.Column(db.Integer, db.ForeignKey('tasklist.id'))

    def __init__(self, name, tasklist_id):
        self.name = name
        self.tasklist_id = tasklist_id
