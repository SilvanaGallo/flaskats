from click.testing import CliRunner
from flaskats.cli import start_applications_worker, check_candidates, send_offers


def test_check_candidates(app):
    with app.app_context():
        runner = CliRunner()
        result = runner.invoke(check_candidates)
        assert "Notifications sent" in result.output


def test_start_applications_worker(app):
    assert False
    # with app.app_context(): # problems because the execution is not finished
    #     runner = CliRunner()
    #     result = runner.invoke(start_applications_worker)
    #     assert result.exit_code == 0
    #     assert "Starting worker" in result.output


def test_send_offers(app):
    assert False
    # with app.app_context(): # problems because the execution is not finished we need to type Ctrl
    #     runner = CliRunner()
    #     result = runner.invoke(send_offers)
    #     assert "Notifications sent" in result.output