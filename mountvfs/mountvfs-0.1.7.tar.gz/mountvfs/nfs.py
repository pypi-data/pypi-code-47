import subprocess

from typeguard import typechecked
from typing import Optional

from mountvfs.vfs import Vfs


class Nfs(Vfs):

    _CONN_CMD = 'mount "{server}:{remote_dir}" "{target_dir}"'
    _DISCONN_CMD = 'umount "{}"'

    @typechecked
    def __init__(self, remote_dir: Optional[str] = None, server: Optional[str] = None, *args, **kwargs):
        """
        :param Optional[str] server: Remote server name; is required for remote saving.
        :param Optional[str] remote_dir: Remote server path to save to; is required for remote saving.
        :param Optional[str] key: A path to SSH security key.
        """
        super().__init__(*args, **kwargs)

        if server and remote_dir:
            self._conn = self._CONN_CMD.format(server=server, remote_dir=remote_dir, target_dir=self._target_dir)
        elif server or remote_dir:
            raise TypeError('One of server or remote_dir parameters is not specified.')
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
