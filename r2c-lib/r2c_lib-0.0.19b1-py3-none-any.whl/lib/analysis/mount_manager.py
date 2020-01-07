#!/usr/bin/env python

import abc
import logging
import os
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Dict, TypeVar

import attr
import docker.errors

from r2c.lib.util import get_tmp_dir

# We need a very small Linux image so we can do some filesystem stuff through
# Docker.
ALPINE_IMAGE = "alpine:3.9"

ManagerT = TypeVar("ManagerT", bound="MountManager")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@attr.s(auto_attribs=True, frozen=True)
class MountManager(abc.ABC):
    """Generates Docker volume mount configuration.

    The intended flow is that you copy the input files to temp_input_dir, then
    call copy_input() and volumes(). After the analyzer runs, you call
    copy_output() to get the output from the image. Finally, call cleanup().

    Mount managers can be used as context managers, returning themselves, and
    automatically executing cleanup() when they go out of scope.
    """

    _docker_client: Any
    # Path inside the Docker image where the analysis volume will be mounted.
    # This is usually /analysis.
    volume_root: Path

    # Used for storage/copying.
    _temp_dir: TemporaryDirectory = attr.ib(init=False)

    @_temp_dir.default
    def _create_temp_dir(self) -> TemporaryDirectory:
        return TemporaryDirectory(prefix="r2c-mount-", dir=get_tmp_dir())

    def __attrs_post_init__(self) -> None:
        self.input_dir().mkdir()
        self.output_dir().mkdir()
        (self.output_dir() / "fs").mkdir()

    def __enter__(self: ManagerT) -> ManagerT:
        return self

    def __exit__(self, _exception_type, _exception_value, _traceback):
        self.cleanup()

    def input_dir(self) -> Path:
        """Directory to store input files/directories in."""
        return Path(self._temp_dir.name) / "inputs"

    def output_dir(self) -> Path:
        """Directory that output files will be located in after copy_output()"""
        return Path(self._temp_dir.name) / "output"

    @abc.abstractmethod
    def copy_input(self) -> None:
        """Copies the input files from input_dir() to the volume."""

    @abc.abstractmethod
    def copy_output(self) -> None:
        """Copies the output files from the volume to output_dir()."""

    @abc.abstractmethod
    def volumes(self) -> Dict[str, Any]:
        """Returns a dict that should be passed to the client's containers.create().

        Note that depending on the implementation, it may not be safe to call
        add_mount after this.
        """

    def _set_permissions(self) -> None:
        """Sets the mounted volume to 0777 permissions.

        This is necessary because we don't know that the user inside the Docker
        image and the user running r2c will have the same UID/GID (and in
        general, they won't).
        """
        self._docker_client.containers.run(
            ALPINE_IMAGE,
            ["chmod", "-R", "0777", str(self.volume_root)],
            network_mode="none",
            volumes=self.volumes(),
            remove=True,
        )

    def cleanup(self) -> None:
        """Performs any necessary cleanup."""
        try:
            self._temp_dir.cleanup()
        except PermissionError:
            self._set_permissions()
            self._temp_dir.cleanup()


@attr.s(auto_attribs=True, frozen=True)
class LocalMountManager(MountManager):
    """Manages mounts for a local Docker instance.

    This copies all to-be-mounted files into a temporary directory.
    """

    # We use bind mounts, so nothing to do for these.

    def copy_input(self) -> None:
        self._set_permissions()

    def copy_output(self) -> None:
        self._set_permissions()

    def volumes(self) -> Dict:
        return {self._temp_dir.name: {"bind": str(self.volume_root), "mode": "rw"}}


@attr.s(auto_attribs=True, frozen=True)
class RemoteMountManager(MountManager):
    """Manages mounts for a remote Docker instance.

    This constructs a Docker volume and copies files into it. This is slower,
    but necessary, since you can't bind-mount on a remote Docker.

    Note that this also works with a local Docker instance, it's just slower
    than LocalMountManager.
    """

    _volume: Any = attr.ib(init=False)
    # You can't work with a Docker volume without a container to attach it to.
    _dummy_container: Any = attr.ib(init=False)

    @_volume.default
    def _create_volume(self):
        return self._docker_client.volumes.create()

    @_dummy_container.default
    def _create_dummy_container(self):
        # We use this instead of images.list because images.list is a lot
        # slower; this is basically instant.
        try:
            self._docker_client.images.get(ALPINE_IMAGE)
        except docker.errors.ImageNotFound:
            self._docker_client.images.pull(ALPINE_IMAGE)
        return self._docker_client.containers.create(
            ALPINE_IMAGE, command=f"/bin/true", volumes=self.volumes()
        )

    # We use subprocess here because there's no convenient way to do this
    # through the Docker Python API. :(

    def copy_input(self) -> None:
        subprocess.run(
            [
                "docker",
                "cp",
                f"{self._temp_dir.name}/.",
                f"{self._dummy_container.id}:{self.volume_root}",
            ],
            check=True,
        )
        self._set_permissions()

    def copy_output(self) -> None:
        # We don't need to set permissions on the way out since docker cp sets
        # permissions for us.
        subprocess.run(
            [
                "docker",
                "cp",
                f"{self._dummy_container.id}:{self.volume_root}/output/.",
                str(self.output_dir()),
            ]
        )

    def volumes(self) -> Dict[str, Any]:
        return {self._volume.name: {"bind": str(self.volume_root), "mode": "rw"}}

    def cleanup(self) -> None:
        super().cleanup()
        try:
            self._dummy_container.remove()
            self._volume.remove()
        except docker.errors.APIError as e:
            # Don't *fatally* die, but complain loudly.
            logger.error(f"Error while cleaning up after a RemoteMountManager: {e}")


def get_manager(volume_root: Path, docker_client: Any) -> MountManager:
    """Builds the appropriate MountManager instance.

    If the Docker is remote, constructs a RemoteMountManager; otherwise,
    constructs a LocalMountManager. Setting the environment variable
    R2C_USER_REMOTE_MANAGER results in the remote manager always being used.
    """
    if "DOCKER_HOST" in os.environ or "R2C_USE_REMOTE_MANAGER" in os.environ:
        return RemoteMountManager(docker_client=docker_client, volume_root=volume_root)
    else:
        return LocalMountManager(docker_client=docker_client, volume_root=volume_root)
