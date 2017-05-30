#!flask/bin/python

from webFlask import app
app.route('/')


def index():
    return "hello"
