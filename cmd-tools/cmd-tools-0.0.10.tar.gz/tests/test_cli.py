import pytest
from command import cmd, define, hello, load_config, run_command


def test_cli_hello_world(runner):
    result = runner.invoke(hello)
    assert result.output == 'hello world'


def test_cli_command(runner):
    result = runner.invoke(define, ('echo', 'hello'))
    assert result.output == 'hello\n'


def test_run_command_success():
    command = 'echo hello'
    assert run_command(command) == 'hello\n'


def test_run_command_fail():
    command = 'xxdst'
    assert 'not found' in run_command(command)


def test_run_command_with_call():
    pass
    # command, useage = 'vim', 'call'
    # result = run_command(command, useage, shell=False)
    # assert result == 0


@pytest.fixture
def path(tmpdir):
    p = tmpdir.mkdir('sub').join('a.json')
    p.write('{}')
    yield p


@pytest.fixture
def path_not_exist(tmpdir):
    yield tmpdir


@pytest.fixture
def path_without_json(tmpdir):
    p = tmpdir.mkdir('sub').join('a.json')
    p.write('{')
    yield p


def test_load_config_success(path):
    config = load_config(path)
    assert config or isinstance(config, dict, )


def test_load_config_fail_with_not_exist(path_not_exist):
    with pytest.raises(ValueError) as e:
        load_config(path_not_exist / 'a.json')
        assert 'not exist' in str(e)


def test_load_config_fail_with_json_error(path_without_json):
    with pytest.raises(ValueError) as e:
        load_config(path_without_json)
        assert 'format error' in str(e)
