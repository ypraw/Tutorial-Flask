#!flask/bin/python

from flask import Flask, render_template
app = Flask(__name__, static_url_path='')


@app.route('/')
def index(name="Yunindyo"):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run()
