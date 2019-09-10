from myproject import app, db
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return render_template('base.html')
