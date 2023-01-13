from flaskats.services import Consumer
from flaskats.dtos import Application


class HiredCandidateConsumer(Consumer):

    def on_message_received(self, ch, method, properties, body):
        '''Sends the application to the repository'''
        self.contract_sender.send_contract(Application.from_json(body))

    def __init__(self, queue, contract_sender):
        '''Sets the repository dependency'''
        super().__init__(queue)
        self.contract_sender = contract_sender
