import pytest
from click.testing import CliRunner
from app.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_create_vault(runner):
    result = runner.invoke(cli, ['create-vault', 'foobar'])
    assert result.exit_code == 0
    assert 'create vault: foobar' in result.output


def test_create_vault_already_exists(runner):
    result = runner.invoke(cli, ['create-vault', 'foobar'])
    assert result.exit_code == 0
    assert 'exists vault: foobar' in result.output


def test_create_vault_failed(runner):
    result = runner.invoke(cli, ['create-vault', 'foobar'])
    assert result.exit_code != 0
    assert 'failed vault: foobar' in result.output
