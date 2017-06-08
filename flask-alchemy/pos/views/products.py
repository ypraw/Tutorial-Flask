from flask import Blueprints
bp = Blueprints("products",__name__)

@bp.route("/products")
def products_list():
    return