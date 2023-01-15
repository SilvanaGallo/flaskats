from unittest import mock
from unittest.mock import Mock

import pytest
import pika
import json

from flaskats.services.broker import HiredCandidateConsumer
from flaskats.services import ContractSender


class TestHiredCandidateConsumer:

    @pytest.mark.unit
    @mock.patch('flaskats.services.broker.rabbitmq_connection.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_hired_candidate_consumer_is_connected_to_rabbitmq(self, connection_mock):
        channel_mock = Mock()
        connection_mock.return_value.channel.return_value = channel_mock

        contract_sender_mock = Mock(spec=ContractSender)
        subject = HiredCandidateConsumer(queue='hired', contract_sender=contract_sender_mock)
        subject.start()

        channel_mock.basic_consume.assert_called()
        channel_mock.start_consuming.assert_called()

    @pytest.mark.unit
    @mock.patch('flaskats.services.broker.rabbitmq_connection.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_new_message_processed(self, connection_mock):
        contract_sender_mock = Mock(spec=ContractSender)
        subject = HiredCandidateConsumer(queue='hired', contract_sender=contract_sender_mock)
        subject.start()

        data = json.dumps({"name":"AName AndSurname",
                            "email":"mail@gmail.com",
                            "job":"ABC-123",
                            "candidate_id":"123456"})
        subject.on_message_received(None, None, None, data)

        contract_sender_mock.send_contract.assert_called()
