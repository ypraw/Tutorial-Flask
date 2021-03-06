# Tutorial-Flask
Source Belajar Framework Flask, didalam repository ini terdapat dua jenis source code,
yaitu versi 1 dan versi 2.
Untuk instalasi Flask, bisa menggunakan file requirements.txt. (_disarankan menggunakan virtual environment_)
Jika belum mengetahui virtual environment, [Kunjungi Blog saya](https://ypraw.github.io/2017/05/29/Mengenal-Virtual-Environment-pada-Python/)

Jika, pada konsol anda bukan berada di directory file requirements.txt gunakan perintah berikut :

```bash
pip install -r /path/to/requirements.txt
```

Jika, path directory pada konsol sudah berada di directory yang sama dengan file requirements, maka gunakan :

```bash
pip install -r requirements.txt
```

# Versi 1 (webFlask)
Merupakan source tutorial flask dengan basic template, routing, views dan CRUD. Dimana setiap file template dan views direpresentasikan masing-maing viewsZ.py/indexZ.html dimana **Z** merujuk pada bagian 1 2 3.

<b><i>setiap kali pindah bagian perhatikan untuk meng-export viewx.py sesuai dengan bagian yang sedang diikuti.</i></b>

sebagai contoh untuk bagian satu :

```bash
$ export FLASK_APP=views1.py
$ flask run
```
kemudian lanjut lagi bagian dua, maka kita ulangi lagi dengan mengganti views1 menjadi views2 :

```bash
$ export FLASK_APP=views2.py
$ flask run
```
hal ini berlaku seterusnya. atau jika ingin menggunakan 1 views. maka hapus semua kode di disetiap bagian dari tutorial ini, lalu samakan dengan kode dari bagian yang sedang anda pelajari.

Dapat dilihat selengkapnya di [My Blog](https://ypraw.github.io/categories/Flask-Tutorial-Dasar/)
> ### Terdiri Dari
> * Return String Hello World (commited)
> * Rendering Template (commited)
> * Routing (commited)
> * The Real Aplication, Template Inheritance (commited)
> * The Real Aplication, CRUD Modelling (commited)

Untuk yang ingin langsung menggunakan CRUD (bagian kelima) , dapat mengupload Pos(2).sql langsung ke mysqlnya masing-masing bisa menggunakan mysql workbrench atau phpmyadmin.
password defaultnya adalah admin dan usernamenya adalah ypraw

# V.2 (Flask SQL-Alchemy)
Tutorial lanjutan Flask menggunakan ORM Flask-SqlAlchemy dan Blueprint sebagai modul untuk membuat modular application
[On Progress]



# Sumber
> _Di edit dan di mofidifikasi seperlunya_
> https://github.com/faisalburhanudin/py89
