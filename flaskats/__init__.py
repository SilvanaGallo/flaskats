import os
from flask import Flask
from flask_mail import Mail
from flaskats.config import Config
from flaskats.repository import AirtableRepository
#from flaskats.broker import Consumer
from flaskats.notifier import CandidateNotifier
from flaskats.mailer import MailSender


mail = Mail()
repository = AirtableRepository()
#worker = Consumer(repository=repository)
mail_sender = MailSender(mail)
notifier = CandidateNotifier(mail_sender, repository)

def create_app(config_class=Config):
    from cli import start_worker, check_candidates

    app = Flask(__name__)
    app.config.from_object(config_class)

    mail.init_app(app)

    from flaskats.main.routes import main
    from flaskats.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    app.cli.add_command(check_candidates)
    app.cli.add_command(start_worker)

    return app
