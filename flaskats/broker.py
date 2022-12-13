from flask import request
from flaskats import Config
from flaskats.dto import Application
import requests
import json
import pika

class RabbitmqProducer():
        
    def __init__(self):
        self.connection_parameters = pika.ConnectionParameters(Config.BROKER_HOST)
        self.connection = pika.BlockingConnection(self.connection_parameters)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='applications')

    def submit_application(self, application):
        self.channel.basic_publish(exchange='', routing_key='applications', body=json.dumps(application))
        self._close_connection()

    def _close_connection(self):
        self.connection.close()

class RabbitmqConsumer():

    def on_message_received(self,ch, method, properties, body):
        self.repository.create_record(Application.from_json(json.loads(body)) )
        
    def __init__(self, repository):
        self.connection_parameters = pika.ConnectionParameters(Config.BROKER_HOST)
        self.connection = pika.BlockingConnection(self.connection_parameters)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='applications')
        self.repository = repository

    def start(self):
        self.channel.basic_consume(queue='applications', auto_ack=True, on_message_callback=self.on_message_received)
        print("Starting worker")
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()