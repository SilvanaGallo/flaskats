from click.testing import CliRunner
from cli import start_worker, check_candidates

def test_start_worker():
  runner = CliRunner()
  result = runner.invoke(start_worker)
  assert result.exit_code == 0
  assert "Starting worker" in result.output

def test_check_candidates(app):
  runner = CliRunner()
  result = runner.invoke(check_candidates)
  assert "Notifications sent" in result.output