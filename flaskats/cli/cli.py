import click
import requests
import json
import signal
import time
from flask.cli import with_appcontext
from flaskats.services import RecruiteeRepository, ApplicationConsumer,\
    HelloSignContractSender, HiredCandidateConsumer,\
    MailSender, CandidateNotifier
from flaskats import mail


repository = RecruiteeRepository()
application_worker = ApplicationConsumer(repository=repository)
contract_sender = HelloSignContractSender()
hired_worker = HiredCandidateConsumer(queue='hired', contract_sender=contract_sender)
mail_sender = MailSender(mail)
notifier = CandidateNotifier(mail_sender, repository)


def handler(signum, frame):
    res = input("\nCtrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        if application_worker.is_started():
            application_worker.close_connection()
        if hired_worker.is_started():
            hired_worker.close_connection()
        print("Closing workers connections")
        exit(0)


signal.signal(signal.SIGINT, handler)


@click.group()
def workers():
    pass


@workers.command()
def start_applications_worker():

    print("Starting applications worker")
    application_worker.start()


@workers.command()
def send_offers():

    print("Starting hired candidates worker")
    hired_worker.start()


@click.group()
def candidates():
    pass


@candidates.command()
@with_appcontext
def check_candidates():

    notifier.check_candidates()
    print("Notifications sent")


cli = click.CommandCollection(sources=[workers, candidates])

if __name__ == '__main__':
    cli()