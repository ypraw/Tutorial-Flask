from flask import Blueprint, render_template, request, redirect
#from pos.models import db
#from pos.models.login import TB_user

bp = Blueprint("login", __name__)

# method login


@bp.route("/login")
def login():
    return render_template("login.html")
