import pytest
from flask_mail import Mail
from flaskats.services import MailSender
from flaskats.dtos import Application


class TestMailSender:

    @pytest.mark.unit
    def test_rejected_candidate(self, app):
        with app.app_context():
            mail = Mail().init_app(app)
            with mail.record_messages() as outbox:
                mailer = MailSender(mail)
                mailer.rejected_candidate(Application(name="Example", email="example@example.com", job="ABC-123", candidate_id=123))

                assert len(outbox) == 1
                assert "Application Status" in outbox[0].subject
                assert "usefulapp2022@outlook.com" == outbox[0].sender
                assert "example@example.com" in outbox[0].recipients 

    @pytest.mark.unit
    def test_hired_candidate(self, app):
        with app.app_context():
            mail = Mail().init_app(app)
            with mail.record_messages() as outbox:
                mailer = MailSender(mail)
                mailer.hired_candidate(Application(name="Example", email="example@example.com", job="ABC-123", candidate_id=123))

                assert len(outbox) == 1
                assert "Offer" in outbox[0].subject
                assert "usefulapp2022@outlook.com" == outbox[0].sender
                assert "example@example.com" in outbox[0].recipients
