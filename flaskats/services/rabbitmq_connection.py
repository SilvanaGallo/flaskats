'''This module contains classes for Queuing and Dequeuing applications'''
from abc import ABC
import pika
from flaskats import Config


class RabbitmqConnection(ABC):
    '''This class initializes the Rabbitmq connection.'''

    def __init__(self, queue='applications'):
        self.queue = queue
        self.connection_parameters = pika.ConnectionParameters(Config.BROKER_HOST)
        self.connection = pika.BlockingConnection(self.connection_parameters)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
