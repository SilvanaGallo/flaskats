import click
import requests
import json
from flaskats.broker import RabbitmqConsumer
from flaskats import repository

candidates_url = 'http://localhost:5000/reports'

@click.group()
def worker():
    pass

@worker.command()
def start_worker():
    worker = RabbitmqConsumer(repository=repository)
    worker.start()


@click.group()
def candidates():
    pass

@candidates.command()
def check_candidates():
    repository.check_candidates()


cli = click.CommandCollection(sources=[worker, candidates])

if __name__ == '__main__':
    cli()
