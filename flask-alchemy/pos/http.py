from flask import Flask
from pos.config import Config
from pos.models import db


def create_app(config=Config):
    app = Flask(__name__)

    # load config
    app.config.from_object(config)

    # load sqlaclhemy
    db.init_app(app)

    return app
