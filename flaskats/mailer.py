from flask_mail import Message
from flask import current_app


class MailSender:
    def __init__(self, mail):
        self.mail = mail

    def _send_email(self, message):
        self.mail.send(message)

    def rejected_candidate(self, app):
        message = f'''<h1>Application Status - {app.job}</h1>
                    <p>Hello {app.name},</p>
                    <p>We are writing in connection with the selection process for the requested position.</p>
                    <p>We regret to inform you that despite the indisputable qualities you possess, after final consideration we have decided that we will not be offering you the position. 
                    We came to this conclusion after interviewing another candidate who matched more precisely the requirements that our company demands.</p>
                    <p>We offer you our sincerest thanks for your interest and trust shown in our organisation.</p>
                    <p>
                    Regards, 
                    ATS Group
                    </p>'''
        subject = f"Application Status - {app.job}"
        msg = Message(recipients=[app.email],
                      html=message,
                      subject=subject)
        self._send_email(msg)

    def hired_candidate(self, app):
        message = f'''<h1>Offer</h1>
                    <p>Hello {app.name},</p>
                    <p>Congratulations! We are happy to inform you that you have been selected to join the team! 
                    You were selected over many other applicants because of the skills, experience, and attitude 
                    that you will bring to the company. Please wait for a new contact with the next steps.
                    </p>
                    <p>
                    Regards, 
                    ATS Group
                    </p>'''
        subject = f"Offer - {app.job}"
        msg = Message(recipients=[app.email],
                      html=message,
                      subject=subject)
        self._send_email(msg)