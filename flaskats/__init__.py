from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskats.config import Config


db = SQLAlchemy()
migrate = Migrate(db, compare_type=True)

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

offers_repository = None


def create_app(config_class=Config):
    from flaskats.cli import start_applications_worker, check_candidates, send_offers
    from flaskats.repositories import SQLAlchemyOffersRepository

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    listOfGlobals = globals()
    listOfGlobals['offers_repository'] = SQLAlchemyOffersRepository()

    from flaskats.blueprints.users.routes import users
    from flaskats.blueprints.offers.routes import offers
    from flaskats.blueprints.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(offers)
    app.register_blueprint(errors)

    app.cli.add_command(check_candidates)
    app.cli.add_command(start_applications_worker)
    app.cli.add_command(send_offers)

    return app
