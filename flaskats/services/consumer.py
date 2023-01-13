from abc import ABC, abstractmethod
from flaskats.services import RabbitmqConnection


class Consumer(RabbitmqConnection):
    '''For event consuming'''

    @abstractmethod
    def on_message_received(self, ch, method, properties, body):
        '''To be implemented in subclasses'''
        return

    def start(self):
        '''Starts the consumer function'''
        self.channel.basic_consume(queue=self.queue,
                                    auto_ack=True,
                                    on_message_callback=self.on_message_received)
        self.channel.start_consuming()

    def close_connection(self):
        '''Closes the connection'''
        self.connection.close()
