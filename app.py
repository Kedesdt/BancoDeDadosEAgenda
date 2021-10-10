from flask import Flask, render_template
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'pass'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')