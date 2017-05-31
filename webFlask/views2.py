#!flask/bin/python

from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.route('/')
# Start Bagian Kedua
# Bagian Kedua routing dan Render Template
def index(name='Yunindyo'):
    return render_template('index2.html', name=name)
# End Bagian Kedua


if __name__ == '__main__':
    app.debug = True
    app.run()
