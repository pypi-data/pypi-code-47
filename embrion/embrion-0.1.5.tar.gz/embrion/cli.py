import subprocess

import click
import os
import webbrowser

dir_path = os.path.dirname(os.path.realpath(__file__))
docker_compose_original_path = os.path.join(dir_path, 'docker-compose.yml')
jupyter_path = 'http://localhost:28888'
vscode_path = 'http://localhost:28443'


# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')


@click.group()
def main():
    pass


def trace_logs():
    id = subprocess.check_output(["docker-compose", "-f", docker_compose_original_path, "ps", "-q"]).decode().rstrip()
    subprocess.call(["docker", "logs", id, "-f", "--since=1s"])


def open_default():
    webbrowser.open(jupyter_path, new=2)


@main.command()
def up():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "pull"])
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "up", "-d"])
    trace_logs()
    # subprocess.call(["docker-compose", "-f", docker_compose_original_path, "logs", "-f"])


@main.command()
def down():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "down"])


@main.command()
def start():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "start"])
    trace_logs()
    # subprocess.call(["docker-compose", "-f", docker_compose_original_path, "logs", "-f"])


@main.command()
def stop():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "stop"])


@main.command()
def restart():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "restart"])
    trace_logs()


@main.command()
def refresh():
    subprocess.call(
        ["docker-compose", "-f", docker_compose_original_path, "exec", "dev", "zsh",
         "/embrion/dev/update_environment.sh"])


@main.command()
def shell():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "exec", "dev", "zsh"])


@main.command()
def open_vscode():
    webbrowser.open(vscode_path, new=2)


@main.command()
def open_jupyter():
    open_default()


@main.command()
def build():
    subprocess.call(["docker-compose", "-f", docker_compose_original_path, "build"])


if __name__ == '__main__':
    main()
