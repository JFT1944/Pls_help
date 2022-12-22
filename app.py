"""Blogly application."""

from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'cows'
toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context()
# db.create_all()

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/users')
def users():
    return render_template('ui.html')


@app.route('/users/new')
def newUser():
    return render_template('new-user-form.html')



@app.route('/users/<userid>')
def userId(userid):
    return render_template('new-user-form.html')
