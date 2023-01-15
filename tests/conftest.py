import pytest
import os
from flaskats import create_app, db
from flask_mail import Mail
from flaskats.services import RecruiteeRepository
from flaskats.dtos import Application


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({"TESTING": True,
                       "DEBUG" : True,
                       "WTF_CSRF_ENABLED": False,
                       "MAIL_SUPPRESS_SEND": True})

    # other setup can go here
    yield app
    # clean up / reset resources here

@pytest.fixture()
def test_client_db(app):
    # set up
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    with app.app_context():
        db.init_app(app)
        db.create_all()
    testing_client = app.test_client() 
    ctx = app.app_context()
    ctx.push()

    # do the testing
    yield testing_client

    # tear down
    with app.app_context():
        db.session.remove()
        db.drop_all()

    ctx.pop()
# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()


@pytest.fixture()
def application_dtos():
    return {"rec560UJdUtocSouk": Application(name="AName AndSurname",
                                            email="mail@gmail.com",
                                            job="ABC-123",
                                            candidate_id="123456").to_dict(),
            "rec3lbPRG4aVqkeOQ": Application(name="AName2 AndSurname2",
                                            email="mail2@gmail.com",
                                            job="ABC-123",
                                            candidate_id="654321").to_dict()}
