from unittest import mock

import pika
import pytest

from flaskats.services.broker import Producer
from flaskats.dtos import Application


class TestProducer:

    @pytest.mark.unit
    @mock.patch('flaskats.services.broker.rabbitmq_connection.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_submit_event(self, connection_mock):
        connection_mock.return_value.channel.return_value.basic_publish.return_value = True
        app = Application(name="AName AndSurname",
                            email="mail@gmail.com",
                            job="ABC-123",
                            candidate_id="123456")
        subject = Producer(queue="queue_name")

        assert subject.submit_event(app) is True
