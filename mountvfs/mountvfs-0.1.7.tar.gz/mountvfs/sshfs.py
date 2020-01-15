import os
import subprocess

from typeguard import typechecked
from typing import Optional

from mountvfs.vfs import Vfs


class Sshfs(Vfs):

    _AUTH_CMD = '-o IdentityFile="{}"'
    _CONN_CMD = 'sshfs -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no  ' \
                '-o ServerAliveInterval={alive_interval} -o ServerAliveCountMax={alive_max_count} {auth} ' \
                '{user}@{server}:"{remote_dir}" "{target_dir}"'
    _DISCONN_CMD = 'fusermount -u "{}"'

    @typechecked
    def __init__(self,
                 remote_dir: Optional[str] = None,
                 server: Optional[str] = None,
                 user: Optional[str] = None,
                 key: Optional[str] = None,
                 server_alive_interval: int = 10,
                 server_alive_max_count: int = 3,
                 *args, **kwargs):
        """
        :param Optional[str] user: Remote user name; is required for remote saving.
        :param Optional[str] server: Remote server name; is required for remote saving.
        :param Optional[str] remote_dir: Remote server path to save to; is required for remote saving.
        :param Optional[str] key: A path to SSH security key.
        """
        super().__init__(*args, **kwargs)

        if user and server and remote_dir:
            assert server_alive_interval > 0 and server_alive_max_count > 0
            auth = ''
            if key and isinstance(key, str):
                key = os.path.abspath(os.path.expanduser(key))
                assert os.path.isfile(key), f'Auth key "{key}" does not exist.'
                auth = self._AUTH_CMD.format(key)
            self._conn = self._CONN_CMD.format(
                alive_interval=server_alive_interval, alive_max_count=server_alive_max_count, auth=auth, user=user,
                server=server, remote_dir=remote_dir, target_dir=self._target_dir)
        elif user or server or remote_dir:
            raise TypeError('One of user, server or remote_dir parameters is not specified.')
        else:
            self._conn = ''

    def _mount(self):
        try:
            subprocess.check_output(self._conn, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            raise ConnectionError(str(exc.output))

    def _unmount(self):
        try:
            subprocess.check_output(self._DISCONN_CMD.format(self._target_dir), shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            raise ConnectionError(exc.output)
