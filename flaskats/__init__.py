import os
from flask import Flask, current_app
from flask_mail import Mail
from flaskats.config import Config
from flaskats.repository import AirtableRepository


mail = Mail()
repository = AirtableRepository()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    from flaskats.main.routes import main
    from flaskats.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
