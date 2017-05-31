#!flask/bin/python

from flask import Flask, render_template, request, url_for, redirect, make_response

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if validasi_login(request.form['username'], request.form['password']):
            return redirect(url_for('dashboard', username=request.form.get('username')))
        else:
            error = "incorrect password or username"
    return render_template('login.html', error=error)


def validasi_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)


#   End Bagian keempat
if __name__ == '__main__':
    app.debug = True
    app.run()
