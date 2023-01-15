import pytest
from flaskats.services.broker import Consumer


class TestConsumer:

    @pytest.mark.unit
    def test_consumer_creation(self):
        with pytest.raises(Exception):
            cs: Consumer = Consumer()

    @pytest.mark.unit
    def test_send_contract_abstract_method(self, mocker):
        with pytest.raises(NotImplementedError):
            mocker.patch.multiple(Consumer, __abstractmethods__=set())
            consumer: Consumer = Consumer()
            consumer.on_message_received(None, None, None, {})

    def test_is_started(self, mocker):
        mocker.patch.multiple(Consumer, __abstractmethods__=set())
        consumer: Consumer = Consumer()
        consumer.started = True
        assert consumer.is_started()
