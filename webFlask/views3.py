#!flask/bin/python

from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.route('/')
def index(name='Yunindyo'):
    return render_template('index3.html', name=name)


@app.route('/Hello')
def hello():
    content = {'Nama': 'Yunindyo Prabowo', 'Asal': 'Semarang', 'Umur': '20'}
    return render_template('hello.html', content=content)


if __name__ == '__main__':

    app.run()
