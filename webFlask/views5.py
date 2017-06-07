#!flask/bin/python

from flask import Flask, render_template, request, url_for, redirect, session
import connection as db

app = Flask(__name__, static_url_path='')

konek = db.MysqlUserDB('127.0.0.1', 'root', '', 'flasktutorial')
cur = konek.getDB()


@app.route('/')
def index():
    cur.execute("SELECT * from  tb_content")
    result = cur.fetchall()
    print(result)
    if 'username' in session:
        return render_template('dashboard5.html', username=session['username'])
    else:
        return render_template('home5.html', result=result)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if validasi_login(request.form['username'], konek.computeMD5hash(request.form['password'])):
            session['username'] = request.form.get('username')
            return redirect(url_for('dashboard'))
        else:
            error = "incorrect password or username"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for("index"))


def validasi_login(username, password):
    cur.execute("SELECT * from tb_user WHERE username=%s AND password=%s",
                (username, password))
    if cur.fetchone():
        return True
    else:
        return False


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard5.html', username=session['username'])
    else:
        return redirect(url_for('index'))


@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    else:
        return redirect(url_for('index'))


#   End Bagian keempat
# if __name__ == '__main__':
app.debug = True
app.secret_key = '4KuC1nT@K4MU'
app.run()
