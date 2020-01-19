import click

from embrion.src.docker_engine import DockerEngine, DevPort
from embrion.src.storage import Storage
from embrion.src.util import open_window, call, check_output


class RemoteEngine(object):
    def __init__(self, server_name, project_name, storage_path):
        self.server_name = server_name
        self.project_name = project_name
        self.storage = Storage(storage_path)
        self.key_name = f'connection_{self.server_name}_{self.project_name}'

    @staticmethod
    def get_open_port():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
        s.close()
        return port

    def get_remote_port_mapping(self):
        # ssh -t aws-xxx 'xxx'
        command = DockerEngine.get_port_command(self.project_name)
        mapping_str = check_output(['ssh', '-t', self.server_name, ' '.join(command)])
        if not mapping_str:
            click.echo('Could not find the container to get ports.')
            return
        return DockerEngine.parse_port_mapping(mapping_str)

    def retrieve_tunnel_mapping(self):
        mapping = self.storage.retrieve(self.key_name)
        if mapping is None:
            click.echo('Not attached.')
            return None
        else:
            return dict(mapping)

    def store_tunnel_mapping(self, mapping):
        self.storage.store(self.key_name, list(mapping.items()))

    def delete_tunnel_mapping(self):
        self.storage.delete(self.key_name)

    def get_socket_path(self, local_port):
        return f'/tmp/{self.key_name}_{local_port}'

    def detach(self):
        # ssh -S <path-to-socket> -O exit <server>
        click.echo('Tunnel status is being checked.')
        mapping = self.retrieve_tunnel_mapping()
        if mapping is not None:
            click.echo('Detaching...')
            for remote_port, local_port in dict(mapping).items():
                socket_path = self.get_socket_path(local_port)
                call(['ssh', '-S', socket_path, '-O', "exit", self.server_name])
            self.delete_tunnel_mapping()
            click.echo('Detached successfully.')

    def attach(self):
        # ssh -fNMS <path-to-socket> -L <port>:<host>:<port> <server>
        click.echo('Tunnel status is being checked.')
        if self.retrieve_tunnel_mapping() is None:
            click.echo('Attaching...')
            port_mapping = self.get_remote_port_mapping()
            new_mapping = {}
            for docker_port, remote_port in port_mapping.items():
                local_port = self.get_open_port()
                new_mapping[remote_port] = local_port
                socket_path = self.get_socket_path(local_port)
                call(['ssh', '-fNMS', socket_path, '-L', f'{local_port}:localhost:{remote_port}', self.server_name])
            self.store_tunnel_mapping(new_mapping)
            click.echo('Attached successfully.')
        else:
            click.echo('Already attached.')

    def get_tunnel_port_mapping(self):
        remote_mapping = self.get_remote_port_mapping()
        mapping = self.retrieve_tunnel_mapping()
        new_mapping = {}
        for docker_port, remote_port in remote_mapping.items():
            new_mapping[docker_port] = mapping[remote_port]
        return new_mapping

    def ssh_port(self):
        return self.get_tunnel_port_mapping()[DevPort.SSH.value]

    def open_vscode(self):
        self.attach()
        port = self.get_tunnel_port_mapping()[DevPort.VSCODE.value]
        open_window(port)

    def open_jupyter(self):
        self.attach()
        port = self.get_tunnel_port_mapping()[DevPort.JUPYTER.value]
        open_window(port)
