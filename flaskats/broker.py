'''This module contains classes for Queuing and Dequeuing applications'''
import json
from abc import ABC
import pika
from flaskats import Config
from flaskats.dto import Application

class RabbitmqConnection(ABC):
    '''This class initializes the Rabbitmq connection.'''

    def __init__(self):
        self.connection_parameters = pika.ConnectionParameters(Config.BROKER_HOST)
        self.connection = pika.BlockingConnection(self.connection_parameters)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='applications')


class Producer(RabbitmqConnection):
    '''For applications submitting'''

    def submit_application(self, application):
        '''Enqueue an application to the queue'''
        ret = self.channel.basic_publish(exchange='',
                                        routing_key='applications',
                                        body=application.to_json()
                                    )
        self._close_connection()
        return ret

    def _close_connection(self):
        '''Closes the connection'''
        self.connection.close()


class Consumer(RabbitmqConnection):
    '''For applications sending to the Repo'''

    def on_message_received(self,ch, method, properties, body):
        '''Sends the application to the repository'''
        self.repository.create_record(Application.from_json(body))

    def __init__(self, repository):
        '''Sets the repository dependency'''
        super().__init__()
        self.repository = repository

    def start(self):
        '''Starts the consumer function'''
        self.channel.basic_consume(queue='applications',
                                    auto_ack=True,
                                    on_message_callback=self.on_message_received
                                )
        self.channel.start_consuming()
        
    def close_connection(self):
        '''Closes the connection'''
        self.connection.close()
