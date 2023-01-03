from unittest import mock
from unittest.mock import Mock

import pytest
import pika
import json

from flaskats.broker import Consumer
from flaskats.repository import AirtableRepository


class TestConsumer:

    @pytest.mark.unit
    @mock.patch('flaskats.broker.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_consumer_is_connected_to_rabbitmq(self, connection_mock):
        channel_mock = Mock()
        connection_mock.return_value.channel.return_value = channel_mock
        repo = AirtableRepository()

        subject = Consumer(repo)
        subject.start()

        channel_mock.basic_consume.assert_called()
        channel_mock.start_consuming.assert_called()

    @pytest.mark.unit
    @mock.patch('flaskats.broker.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_new_message_processed(self, connection_mock):
        repo_mock = Mock(spec=AirtableRepository)
        connection_mock.return_value.channel.return_value

        data = json.dumps({"name": "Silvana", "email": "silvana@gmail.com", "job": "JT123"})
        subject = Consumer(repo_mock)
        subject.on_message_received(None, None, None, data)

        repo_mock.create_record.assert_called()
