import json
import webbrowser
from pathlib import Path
from subprocess import PIPE, call, run

import click


@click.command(name='hello')
def hello():
    click.echo('hello world', nl=False)


@click.command(name='command')
@click.argument('command', nargs=-1)
def define(command):
    command = " ".join(command)
    result = run_command(command, usage='run')
    click.echo(result, nl=False)


def run_command(command, usage='run', **kwargs):
    if usage == 'run':
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True, **kwargs)
        output = result.stdout
        return output if output else result.stderr
    elif usage == 'call':
        result = call(command.split(' '), **kwargs)
        return result


def load_config(path=Path.home() / Path('.cmdrc.json')):
    if not path.exists():
        raise ValueError('~/.cmdrc.json not exist')
    with open(path, 'r') as f:
        config = f.read()

    try:
        config = json.loads(config)
    except json.decoder.JSONDecodeError:
        raise ValueError(f'{path} file format error')
    return config


@click.command(name='name')
@click.argument('name', type=str, required=True)
def cmd(name):
    config = load_config()
    command, usage = config[name]['command'], config[name]['usage']
    result = run_command(command, usage)
    if usage == 'run':
        click.echo(result, nl=False)


@click.command(name='u')
@click.argument('url', type=str, required=True)
def open_url(url: str):
    if not url.startswith('http'):
        url = 'http://' + url
    webbrowser.open_new(url)
