#!flask/bin/python

from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static/')


'''
Untuk Bagian pertama dan kedua hapus salah satu komentar pada fungsi index
sampai dengan return.
* jika mengikuti bagian Pertama maka berikan komentar
  pada fungsi index bagian kedua
* jika mengikuti bagian kedua dan seterusnya, maka biarkan index bagian pertama
  seperti ini (settingan default, bagian pertama di jadikan komentar)
'''


@app.route('/')
# Start Bagian Pertama
# Bagian Pertama, Hello World from flask
#
#
# hapus komentar dari bawah ini sampai return
# def index():
#    return "hello world"
#
# End Bagian Pertama
#
#
######################################################
#
#
# Start Bagian Kedua
# Bagian Kedua routing dan Render Template
#
def index(name='Yunindyo'):
    return render_template('index.html', name=name)
# End Bagian Kedua


@app.route('/Hello')
# Bagian Ketiga routing untuk hyperlink
def hello():
    content = {'Nama': 'Yunindyo Prabowo', 'Asal': 'Semarang', 'Umur': '20'}
    return render_template('hello.html', content=content)


if __name__ == '__main__':
    app.run()
