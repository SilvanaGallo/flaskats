from flaskats.mailer import MailSender
from flaskats.dto import Application
from flaskats import mail


class TestMailSender:

    def test_rejected_candidate():
        with mail.record_messages() as outbox:
            mailer = MailSender(mail)
            mailer.rejected_candidate(Application(name="Example", email="example@example.com"))

            assert len(outbox) == 1
            assert "Application Status" in outbox[0].subject
            assert "usefulapp2022@outlook.com" == outbox[0].sender
            assert "example@example.com" == outbox[0].to

    def test_hired_candidate(mail):
        with mail.record_messages() as outbox:
            mailer = MailSender(mail)
            mailer.hired_candidate(Application(name="Example", email="example@example.com"))

            assert len(outbox) == 1
            assert "Offer" in outbox[0].subject
            assert "usefulapp2022@outlook.com" == outbox[0].sender
            assert "example@example.com" == outbox[0].to