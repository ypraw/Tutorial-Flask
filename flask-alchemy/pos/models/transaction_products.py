from sqlalchemy import event
from sqlalchemy.orm import relationship
from pos.models import db
from pos.models.product import Product


class TransactionProducts(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    transaction_id = db.Column(db.Integer, db.ForeignKey("transactions.id"),
                               nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"),
                           nullable=False)

    product_qty = db.Column(db.Integer, nullable=False)

    transaction = relationship("Transactions", backref="transaction_products")

    product = relationship("Product", backref="transaction_products")


@event.listens_for(db.session, "before_flush")
def reduce_stock_product(*arg):
    sess = arg[0]
    for obj in sess.new:
        if isinstance(obj, TransactionProducts):
            product = Product.query.filter_by(id=obj.product_id).first()

            product.stock = product.stock - obj.product_qty
            db.session.add(product)
