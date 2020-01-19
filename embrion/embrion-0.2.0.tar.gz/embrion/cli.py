import click
import os

from embrion.src.docker_engine import DockerEngine
from embrion.src.remote_engine import RemoteEngine
from embrion.src.util import get_project_name, PythonLiteralOption, init_environment

dir_path = os.path.dirname(os.path.realpath(__file__))
docker_compose_original_path = os.path.join(dir_path, 'docker-compose.yml')
environment_init_path = os.path.join(dir_path, 'dev', 'environment_init.yml')
storage_path = os.path.join(dir_path, 'connections')
docker_engine = DockerEngine(docker_compose_original_path, get_project_name())


@click.group()
def main():
    pass


@main.command()
def up():
    docker_engine.up()


@main.command()
def down():
    docker_engine.down()


@main.command()
def start():
    docker_engine.start()


@main.command()
def stop():
    docker_engine.stop()


@main.command()
def restart():
    docker_engine.restart()


@main.command()
def refresh():
    docker_engine.refresh()


@main.command()
def shell():
    docker_engine.shell()


@main.command()
def vscode():
    docker_engine.open_vscode()


@main.command()
def jupyter():
    docker_engine.open_jupyter()


@main.command()
def build():
    docker_engine.build()


@main.command()
def base():
    click.echo(docker_engine.base())


@main.command()
def port():
    click.echo(docker_engine.get_port_mapping())


@main.command()
def ssh_port():
    click.echo(docker_engine.ssh_port())


@main.command()
@click.option('--args', cls=PythonLiteralOption, default=[])
def eval(args):
    click.echo(f'Arguments: {args}')
    click.echo(docker_engine.output(args))


@click.option('--version', default='3.7', type=str)
@main.command()
def init(version):
    init_environment(environment_init_path, version)


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def remote_port(server_name, project_name):
    remote_engine = RemoteEngine(server_name, project_name, storage_path)
    click.echo(remote_engine.get_remote_port_mapping())


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def tunnel_port(server_name, project_name):
    remote_engine = RemoteEngine(server_name, project_name, storage_path)
    click.echo(remote_engine.get_tunnel_port_mapping())


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def tunnel_ssh_port(server_name, project_name):
    remote_engine = RemoteEngine(server_name, project_name, storage_path)
    click.echo(remote_engine.ssh_port())


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def attach(server_name, project_name):
    RemoteEngine(server_name, project_name, storage_path).attach()


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def detach(server_name, project_name):
    RemoteEngine(server_name, project_name, storage_path).detach()


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def vscode_remote(server_name, project_name):
    RemoteEngine(server_name, project_name, storage_path).open_vscode()


@click.option('--server_name', type=str, required=True)
@click.option('--project_name', type=str, required=True)
@main.command()
def jupyter_remote(server_name, project_name):
    RemoteEngine(server_name, project_name, storage_path).open_jupyter()


if __name__ == '__main__':
    main()
