import os
from flask import Flask
from flask_mail import Mail
from flaskats.config import Config
from flaskats.repository import AirtableRepository
from flaskats.broker import RabbitmqConsumer
from flaskats.notifier import CandidateNotifier
from flaskats.mailer import MailSender

mail = Mail()
repository = AirtableRepository()
worker = RabbitmqConsumer(repository=repository)
mail_sender = MailSender(mail)
#notifier = CandidateNotifier(mail_sender, repository)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)    

    from flaskats.main.routes import main
    from flaskats.errors.handlers import errors
    
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
