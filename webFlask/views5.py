#!flask/bin/python

from flask import Flask, render_template, request, url_for, redirect, session
import connection as db

app = Flask(__name__, static_url_path='')

konek = db.MysqlUserDB('127.0.0.1', 'root', '', 'pos')
cur = konek.getDB()


@app.route('/')
def index():
    return render_template('home5.html')


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
        cur.execute("SELECT * from product")
        resultProduct = cur.fetchall()
        return render_template('dashboard5.html', resultProduct=resultProduct)
    else:
        return redirect(url_for('index'))


@app.route('/product/add', methods=['GET', 'POST'])
def add_product():
    # cek apakah user sudah login, untuk mencegah akses data pada database
    if 'username' in session:
        if request.method == "GET":
            return render_template("add_product5.html")
        # ambil data dari form add product
        name = request.form["name"]
        price = request.form["price"]
        stock = request.form["stock"]

        # input ke database
        cur.execute("INSERT INTO product values ((%s),(%s),(%s),(%s))",
                    (None, name, price, stock,))

        return redirect("/dashboard")
    # jika belum login maka diarahkan ke login page
    else:
        return redirect(url_for('login'))


@app.route('/product/update', methods=['GET', 'POST'])
def update_product():
    # cek apakah user sudah login, untuk mencegah akses data pada database
    if 'username' in session:
        if request.method == "GET":
            return render_template("add_product5.html")
        # ambil data dari form add product
        name = request.form["name"]
        price = request.form["price"]
        stock = request.form["stock"]

        # input ke database
        cur.execute("INSERT INTO product values ((%s),(%s),(%s),(%s))",
                    (None, name, price, stock,))

        return redirect("/dashboard")
    # jika belum login maka diarahkan ke login page
    else:
        return redirect(url_for('login'))


#   End Bagian keempat
# if __name__ == '__main__':
app.debug = True
app.secret_key = '4KuC1nT@K4MU'
app.run()
