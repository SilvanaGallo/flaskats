import pytest
from flaskats.models import ApplicationStatus


class TestApplicationStatus:

    @pytest.mark.unit
    def test_inbox_creation_and_print(self):
        app_status = ApplicationStatus.INBOX
        assert str(app_status) == "INBOX"
        assert app_status.value == 1

    @pytest.mark.unit
    def test_hired_creation_and_print(self):
        app_status = ApplicationStatus.HIRED
        assert str(app_status) == "HIRED"
        assert app_status.value == 2

    @pytest.mark.unit
    def test_rejected_creation_and_print(self):
        app_status = ApplicationStatus.REJECTED
        assert str(app_status) == "REJECTED"
        assert app_status.value == 3