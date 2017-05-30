#!flask/bin/python

from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='')


'''
KETENTUAN :

* Jika mengikuti bagian Pertama maka berikan komentar
  pada fungsi index bagian kedua, dst
* Jika mengikuti bagian kedua , berikan komentar pada bagian Pertama
  dan bagian ketiga dan seterusnya.
* Jika mengikuti bagian ke 3, maka pada bagian pertama dan dua dibuat
  menjadi kolom komentar

* JIKA TERJADI ERROR PADA APP.ROUTE, PERHATIKAN IDENTASINYA

IDENTASI YANG BENAR
@app.route()
def namafungsi

Bukan,
 @app.route()
 def namafungsi
'''


# Start Bagian Pertama
# Bagian Pertama, Hello World from flask
#@app.route('/')
#
#
# def index():
#    return "hello world"
#
# End Bagian Pertama
#
#
######################################################
# Start Bagian Kedua
# Bagian Kedua routing dan Render Template
# hapus/berikantanda#
#
# def index(name='Yunindyo'):
#    return render_template('index.html', name=name)
# End Bagian Kedua
########################################################################
# Bagian Ketiga routing untuk hyperlink (hapus/berikantanda# dibawah ini)
#@app.route('/Hello')
#
# def hello():
#    content = {'Nama': 'Yunindyo Prabowo', 'Asal': 'Semarang', 'Umur': '20'}
#    return render_template('hello.html', content=content)
############################################################################
# Bagian keempat, Database.
#   Start Bagian keempat
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if validasi_login(request.form['username'], request.form['password']):
            return "Hello %s" % request.form['username']
        else:
            error = "incorrect password or username"
    return render_template('login.html', error=error)


def validasi_login(username, password):
    if username == password:
        return True
    else:
        return False


#   End Bagian keempat
if __name__ == '__main__':
    app.debug = True
    app.run()
