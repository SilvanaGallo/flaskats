import pytest
from unittest import mock
from unittest.mock import Mock
import pika
from flaskats.services.broker import Consumer


class TestConsumer:

    @pytest.mark.unit
    def test_consumer_creation(self):
        with pytest.raises(Exception):
            cs: Consumer = Consumer()

    @pytest.mark.unit
    def test_on_message_received_abstract_method(self, mocker):
        with pytest.raises(NotImplementedError):
            mocker.patch.multiple(Consumer, __abstractmethods__=set())
            consumer: Consumer = Consumer()
            consumer.on_message_received(None, None, None, {})

    @pytest.mark.unit
    def test_is_started(self, mocker):
        mocker.patch.multiple(Consumer, __abstractmethods__=set())
        consumer: Consumer = Consumer()
        consumer.started = True
        assert consumer.is_started()

    @pytest.mark.unit
    def test_connection_closing(self, mocker): 
        connection_mock = Mock(spec=pika.BlockingConnection)
        mocker.patch.multiple(Consumer, __abstractmethods__=set())
        
        consumer: Consumer = Consumer()
        consumer.connection = connection_mock
        consumer.close_connection()
        connection_mock.close.assert_called()