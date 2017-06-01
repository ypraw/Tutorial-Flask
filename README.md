# Tutorial-Flask
Source Belajar Framework Flask, didalam repository ini terdapat dua jenis source code,
yaitu versi 1 dan versi 2.
Untuk instalasi Flask, bisa menggunakan file requirements.txt.

Jika, pada konsol anda bukan berada di directory file requirements.txt gunakan perintah berikut :

```bash
pip install -r /path/to/requirements.txt
```

Jika, path directory pada konsol sudah berada di directory yang sama dengan file requirements, maka gunakan :

```bash
pip install -r requirements.txt
```

# V.1
Merupakan source tutorial flask dengan basic template, routing dan views. Dimana setiap file template dan views direpresentasikan masing-maing viewsZ.py/indexZ.html dimana **Z** merujuk pada bagian 1 2 3.

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

> [coming soon] khusus bagian ke 4, merupakan gabungan dari bagian 1,2,3 ditambah dengan koneksi database.

Dapat dilihat selengkapnya di [My Blog](https://ypraw.github.io/2017/05/29/Tutorial-Flask-Framework/)
> ### Terdiri Dari
> * Return String Hello World (commited)
> * Rendering Template (commited)
> * Routing (commited)
> * Login Modelling mysql (on Progress)

# V.2
comming soon ....
