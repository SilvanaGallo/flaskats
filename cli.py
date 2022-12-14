import click
import requests
import json
from flaskats import worker, notifier
import signal
import time
from flask.cli import with_appcontext

 
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
@with_appcontext
def check_candidates():
    notifier.check_candidates()


cli = click.CommandCollection(sources=[workers, candidates])

if __name__ == '__main__':
    cli()