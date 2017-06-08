from flask import Blueprint, render_template, request, redirect
from pos.models import db
from pos.models.products import Products

bp = Blueprint("products", __name__)


@bp.route("/products")
def products_list():
    """List product"""

    # mengambil semua product
    products = Products.query.all()
    return render_template("product/list.html", products=products)


@bp.route("/products/add", methods=["POST", "GET"])
def product_add():
    """Add product"""
    if request.method == "GET":
        return render_template('product/form_add.html')

    # get from form
    name = request.form["name"]
    price = request.form["price"]
    stock = request.form['stock']

    # jika lupa cara menyimpan buka notebook sebelumnya
    product = Products()
    product.name = name
    product.price = price
    product.stock = stock
    db.session.add(product)
    db.session.commit()

    # setelah simpan selesai redirect ke list products
    return redirect("/products")


@bp.route("/products/update", methods=["POST", "GET"])
def product_update():
    """Update product"""
    product_id = request.args['id']

    if request.method == "GET":
        # get product by id
        product = Products.query.filter_by(id=product_id).first()

        # tampilkan data produk yang akan di update
        return render_template('product/form_edit.html', product=product)

    # ambil data form
    name = request.form['name']
    price = request.form['price']
    stock = request.form['stock']

    # get product by id
    product = Products.query.filter_by(id=product_id).first()

    # update product
    product.name = name
    product.price = price
    product.stock = stock
    db.session.add(product)
    db.session.commit()

    # redirect ke list products
    return redirect("/products")


@bp.route("/products/delete")
def product_delete():
    """Delete product"""
    product_id = request.args['id']
    product = Products.query.filter_by(id=product_id).first()
    if product:
        # delete product by id
        db.session.delete(product)
        db.session.commit()

    return redirect("/products")
