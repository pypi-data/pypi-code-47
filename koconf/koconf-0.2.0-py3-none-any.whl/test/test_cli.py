import pytest

from click.testing import CliRunner
from koconf.cli import main, entry_command
from koconf.db import DataBaseManager
from koconf.task import BashManager, CronManager


@pytest.fixture()
def runner():
    return CliRunner()


def test_show(mocker, runner):
    mock = mocker.patch.object(DataBaseManager, 'show')
    runner.invoke(main, ['show'])
    mock.assert_called_once()


def test_show_with_no_param(mocker, runner):
    mock = mocker.patch.object(DataBaseManager, 'show_by_applicable')
    runner.invoke(main, ['show', '--applicable'])
    mock.assert_called_once()


@pytest.mark.parametrize(
    'keyword',
    ['id', 'title', 'city', 'tag'],
)
def test_show_with_single_param(mocker, runner, keyword):
    arg = 'string'

    mock = mocker.patch.object(DataBaseManager, 'show_by_' + keyword)
    runner.invoke(main, ['show', '--' + keyword, arg])
    mock.assert_called_once_with(arg)


@pytest.mark.parametrize(
    'keyword, option',
    [
        ('applies', 'apply'),
        ('events', 'event'),
    ],
)
def test_show_with_multiple_param(mocker, runner, keyword, option):
    arg = 'string'

    mock = mocker.patch.object(DataBaseManager, 'show_by_' + keyword)
    runner.invoke(main, ['show', '--' + option, arg])
    mock.assert_called_once_with((arg,))


def test_refresh(mocker, runner):
    mock1 = mocker.patch.object(DataBaseManager, 'refresh')
    mock2 = mocker.patch.object(DataBaseManager, 'expire')
    runner.invoke(main, ['refresh'])
    mock1.assert_called_once()
    mock2.assert_called_once()


def test_refresh_only_expired(mocker, runner):
    mock = mocker.patch.object(DataBaseManager, 'expire')
    runner.invoke(main, ['refresh', '--only-expired'])
    mock.assert_called_once()


def test_refresh_with_clean(mocker, runner):
    mock1 = mocker.patch.object(DataBaseManager, 'clean')
    mock2 = mocker.patch.object(DataBaseManager, 'refresh')
    mock3 = mocker.patch.object(DataBaseManager, 'expire')
    runner.invoke(main, ['refresh', '--with-clean'])
    mock1.assert_called_once()
    mock2.assert_called_once()
    mock3.assert_called_once()


@pytest.mark.parametrize(
    'keyword',
    ['set', 'unset'],
)
def test_refresh_task(mocker, runner, keyword):
    command_name = 'refresh'

    mock = mocker.patch.object(CronManager, keyword + '_reboot_task')
    runner.invoke(main, [command_name, '--' + keyword + '-auto'])
    mock.assert_called_once_with(command=entry_command + ' ' + command_name)


def test_remind(mocker, runner):
    mock = mocker.patch.object(DataBaseManager, 'remind')
    runner.invoke(main, ['remind'])
    mock.assert_called_once()


@pytest.mark.parametrize(
    'keyword',
    ['set', 'unset'],
)
def test_remind_task(mocker, runner, keyword):
    command_name = 'remind'

    mock = mocker.patch.object(BashManager, keyword + '_terminal_task')
    runner.invoke(main, [command_name, '--' + keyword + '-background'])
    mock.assert_called_once_with(command=entry_command + ' ' + command_name)


@pytest.mark.parametrize(
    'keyword',
    ['add', 'remove'],
)
def test_remind_modification(mocker, runner, keyword):
    arg = 'NOT_ID_FORMAT'

    mock = mocker.patch.object(DataBaseManager, keyword + '_remind')
    runner.invoke(main, ['remind', '--' + keyword, arg])
    mock.assert_called_once_with(arg)
