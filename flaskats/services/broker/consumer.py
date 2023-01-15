from abc import ABC, abstractmethod
from flaskats.services.broker import RabbitmqConnection


class Consumer(RabbitmqConnection):
    '''For event consuming'''

    started: bool = False

    @abstractmethod
    def on_message_received(self, ch, method, properties, body):
        '''To be implemented in subclasses'''
        raise NotImplementedError

    def start(self):
        '''Starts the consumer function'''
        self.started = True
        self.channel.basic_consume(queue=self.queue,
                                    auto_ack=True,
                                    on_message_callback=self.on_message_received)
        self.channel.start_consuming()

    def is_started(self) -> bool:
        return self.started

    def close_connection(self):
        '''Closes the connection'''
        self.connection.close()
