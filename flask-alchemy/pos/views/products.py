from flask import Blueprints, render_template
bp = Blueprints("products",__name__)

@bp.route("/products")
def products_list():
    return render_template("products/list.html")