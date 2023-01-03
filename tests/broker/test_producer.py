from unittest import mock

import pytest
import pika

from flaskats.broker import Producer
from flaskats.dto import Application


class TestProducer:

    @pytest.mark.unit
    @mock.patch('flaskats.broker.pika.BlockingConnection', spec=pika.BlockingConnection)
    def test_submit_application(self, connection_mock):
        connection_mock.return_value.channel.return_value.basic_publish.return_value = True
        app = Application(name="Silvana Gallo", email="silvana@gmail.com", job="JT123")
        subject = Producer()

        assert subject.submit_application(app) is True