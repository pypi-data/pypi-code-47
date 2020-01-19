import subprocess
from enum import Enum

import click

from embrion.src.util import open_window, call, check_output


class DevPort(Enum):
    JUPYTER = 8888
    VSCODE = 8443
    SSH = 22


class DockerEngine(object):
    def __init__(self, docker_compose_path, project_name):
        self.docker_compose_path = docker_compose_path
        self.project_name = project_name

    def base_command(self):
        return ["docker-compose", "-f", self.docker_compose_path, "-p", self.project_name]

    def build_command(self, args):
        return self.base_command() + args

    def trace_logs(self):
        id = check_output(self.build_command(["ps", "-q"]))
        subprocess.call(["docker", "logs", id, "-f", "--since=1s"])

    def call(self, args):
        call(self.build_command(args))

    def output(self, args):
        return check_output(self.build_command(args))

    def up(self):
        self.call(["pull"])
        self.call(["up", "-d"])
        self.trace_logs()

    def down(self):
        self.call(["down"])

    def start(self):
        self.call(["start"])
        self.trace_logs()

    def stop(self):
        self.call(["stop"])

    def restart(self):
        self.call(["restart"])
        self.trace_logs()

    def refresh(self):
        self.call(["exec", "dev", "zsh", "/embrion/dev/refresh_environment.sh"])

    def shell(self):
        self.call(["exec", "dev", "zsh"])

    def base(self):
        return " ".join(self.base_command())

    def build(self):
        self.call(["build"])

    @staticmethod
    def parse_port_mapping(mapping_str):
        mapping_list = [s.lstrip() for s in mapping_str.split(",")]
        mapping_elems = [s.split('->') for s in mapping_list]
        return {int(el[1].split('/')[0]): int(el[0].split(':')[1]) for el in mapping_elems}

    @staticmethod
    def get_port_command(project_name, service_name='dev'):
        # docker ps --filter "name=playground_dev_1" --format "{{.Ports}}"
        return ["docker", "ps", "--filter", f'name={project_name}_{service_name}_1', "--format", '{{.Ports}}']

    def get_port_mapping(self):
        # 0.0.0.0:32770->22/tcp, 0.0.0.0:32769->8443/tcp, 0.0.0.0:32768->8888/tcp
        mapping_str = check_output(self.get_port_command(self.project_name))
        if not mapping_str:
            click.echo('Could not find the container to get ports.')
            return
        return self.parse_port_mapping(mapping_str)

    def ssh_port(self):
        return self.get_port_mapping()[DevPort.SSH.value]

    def open_jupyter(self):
        port = self.get_port_mapping()[DevPort.JUPYTER.value]
        open_window(port)

    def open_vscode(self):
        port = self.get_port_mapping()[DevPort.VSCODE.value]
        open_window(port)
