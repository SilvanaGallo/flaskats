import click
import requests
import json
from flaskats.broker import RabbitmqConsumer
from flaskats import worker, mail_sender, repository
import signal
import time
from flaskats.notifier import CandidateNotifier
 
def handler(signum, frame):
    res = input("\nCtrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        worker.close_connection()
        exit(1)
 
signal.signal(signal.SIGINT, handler)

@click.group()
def workers():
    pass

@workers.command()
def start_worker():
    worker.start()


@click.group()
def candidates():
    pass

@candidates.command()
def check_candidates():
    notifier = CandidateNotifier(mail_sender, repository)
    notifier.check_candidates()


cli = click.CommandCollection(sources=[workers, candidates])

if __name__ == '__main__':
    cli()
