import subprocess
import ast

import click
import os
import webbrowser
from enum import Enum


class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


dir_path = os.path.dirname(os.path.realpath(__file__))
docker_compose_original_path = os.path.join(dir_path, 'docker-compose.yml')
environment_init_path = os.path.join(dir_path, 'dev', 'environment_init.yml')


class DevPort(Enum):
    JUPYTER = 8888
    VSCODE = 8443
    SSH = 22


def get_user_dir():
    return subprocess.check_output(['pwd'], shell=True).decode().rstrip()


def get_folder_name():
    return os.path.basename(get_user_dir())


def base_command():
    return ["docker-compose", "-f", docker_compose_original_path, "-p", get_folder_name()]


def build_command(args):
    return base_command() + args


def trace_logs():
    id = subprocess.check_output(build_command(["ps", "-q"])).decode().rstrip()
    subprocess.call(["docker", "logs", id, "-f", "--since=1s"])


def open_jupyter():
    jupyter_path = f'http://localhost:{get_port_mapping()[DevPort.JUPYTER]}'
    webbrowser.open(jupyter_path, new=2)


def open_vscode():
    vscode_path = f'http://localhost:{get_port_mapping()[DevPort.VSCODE]}'
    webbrowser.open(vscode_path, new=2)


def get_port_mapping():
    return {port: get_port(port.value) for port in DevPort}


def get_port(internal_port, service_name='dev'):
    address = subprocess.check_output(build_command(["port", service_name, str(internal_port)])).decode().rstrip()
    return address.split(':')[1]


@click.group()
def main():
    pass


@main.command()
def up():
    subprocess.call(build_command(["pull"]))
    subprocess.call(build_command(["up", "-d"]))
    trace_logs()
    # subprocess.call(["docker-compose", "-f", docker_compose_original_path, "logs", "-f"])


@main.command()
def down():
    subprocess.call(build_command(["down"]))


@main.command()
def start():
    subprocess.call(build_command(["start"]))
    trace_logs()
    # subprocess.call(["docker-compose", "-f", docker_compose_original_path, "logs", "-f"])


@main.command()
def stop():
    subprocess.call(build_command(["stop"]))


@main.command()
def restart():
    subprocess.call(build_command(["restart"]))
    trace_logs()


@main.command()
def refresh():
    subprocess.call(build_command(["exec", "dev", "zsh", "/embrion/dev/update_environment.sh"]))


@main.command()
def shell():
    subprocess.call(build_command(["exec", "dev", "zsh"]))


@main.command()
def vscode():
    open_vscode()


@main.command()
def jupyter():
    open_jupyter()


@main.command()
def build():
    subprocess.call(build_command(["build"]))


@main.command()
def base():
    click.echo(" ".join(base_command()))


@main.command()
def port():
    click.echo(get_port_mapping())


@main.command()
@click.option('--arg', cls=PythonLiteralOption, default=[])
def eval(arg):
    click.echo(f'Arguments: {arg}')
    click.echo(subprocess.check_output(build_command(arg)).decode())


@click.option('--version', default='3.7', type=str)
@main.command()
def init(version):

    write_path = os.path.join(get_user_dir(), 'environment.yml')

    if os.path.exists(write_path):
        click.echo('Environment already exists.')
    else:
        with open(environment_init_path, 'r') as r:
            data = r.read()

        data = data.replace('{{name}}', get_folder_name())
        data = data.replace('{{version}}', version)

        with open(write_path, 'w') as w:
            w.write(data)


if __name__ == '__main__':
    main()
