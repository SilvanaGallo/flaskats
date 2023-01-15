from flaskats.services.broker import RabbitmqConnection


class Producer(RabbitmqConnection):
    '''For event submission'''

    def submit_event(self, event) -> bool:
        '''Enqueue an event to the queue'''
        try:
            self.channel.basic_publish(exchange='',
                                        routing_key=self.queue,
                                        body=event.to_json()
                                    )
            self._close_connection()
            return True
        except:
            return False

    def _close_connection(self):
        '''Closes the connection'''
        self.connection.close()
