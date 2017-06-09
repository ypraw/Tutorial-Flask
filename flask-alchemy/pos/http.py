from flask import Flask
from pos.config import Config
from pos.models import db
from pos.views import product, index, transaction


def create_app(config=Config):
    app = Flask(__name__, static_url_path='')

    # load config
    app.config.from_object(config)

    # load sqlaclhemy
    db.init_app(app)

    # register bluepritn
    app.register_blueprint(index.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(transaction.bp)

    return app
