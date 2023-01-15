from unittest import mock
from unittest.mock import Mock

import pytest
import pika
import json

from flaskats.services.broker import ApplicationsConsumer
from flaskats.services import RecruiteeRepository


class TestApplicationsConsumer:

    @pytest.mark.unit
    @mock.patch('flaskats.services.broker.rabbitmq_connection.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_hired_candidate_consumer_is_connected_to_rabbitmq(self, connection_mock):
        channel_mock = Mock()
        connection_mock.return_value.channel.return_value = channel_mock

        repo_mock = Mock(spec=RecruiteeRepository)
        subject = ApplicationsConsumer(repo_mock)
        subject.start()

        channel_mock.basic_consume.assert_called()
        channel_mock.start_consuming.assert_called()

    @pytest.mark.unit
    @mock.patch('flaskats.services.broker.rabbitmq_connection.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_new_message_processed(self, connection_mock):
        repo_mock = Mock(spec=RecruiteeRepository)
        connection_mock.return_value.channel.return_value

        data = json.dumps({"name": "AName AndSurname",
                           "email": "mail@gmail.com",
                           "job": "ABC-123",
                           "candidate_id": "123456"})

        subject = ApplicationsConsumer(repo_mock)
        subject.on_message_received(None, None, None, data)

        repo_mock.create_record.assert_called()
