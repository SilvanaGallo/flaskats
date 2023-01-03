import pytest
# import os
# from flaskats import create_app
# from flaskats.repository import AirtableRepository
from flaskats.dto import Application


# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update({"TESTING": True,
#                        "WTF_CSRF_ENABLED": False})

#     # other setup can go here

#     yield app

#     # clean up / reset resources here


# @pytest.fixture()
# def client(app):
#     return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()


@pytest.fixture()
def application_dtos():
    return {"rec560UJdUtocSouk": Application(name="AName AndSurname",email="mail@gmail.com",job="ABC-123").to_dict(), 
            "rec3lbPRG4aVqkeOQ": Application(name="AName2 AndSurname2",email="mail2@gmail.com",job="ABC-123").to_dict()}
