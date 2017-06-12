from flask import Blueprint, render_template, request, redirect, url_for
from pos.models import db
from pos.models.login import TB_user

bp = Blueprint("login", __name__)

# method login


@bp.route("/login")
def login():
    # Jika belum login maka di arah ke login.html
    if request.method == 'GET':
        return render_template('login.html')
    # Jika sudah login
    return redirect(url_for('product'))


def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = TB_user(request.form['username'], request.form['password'],
                   request.form['email'])
    db.session.add(user)
    db.session.commit()
    # flash('User successfully registered')
    return redirect(url_for('login'))
