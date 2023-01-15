from flaskats.services.broker import Consumer
from flaskats.dtos import Application


class ApplicationsConsumer(Consumer):

    def on_message_received(self, ch, method, properties, body):
        '''Sends the application to the repository'''
        self.repository.create_record(Application.from_json(body))

    def __init__(self, repository):
        '''Sets the repository dependency'''
        super().__init__()
        self.repository = repository
