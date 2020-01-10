#!/usr/bin/env python

import abc
import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import mkdtemp
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


@attr.s(auto_attribs=True)
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

    # If this is True, then the mount manager will use Docker to set the input
    # and output's permissions to 0777 so it can be cleaned up properly. If
    # we're running inside the Docker container using the same user that's
    # running `r2c`, this should be false.
    #
    # The default is true on Linux (since that's where this issue occurs) and
    # false elsewhere. We provide R2C_ALWAYS_SET_PERMISSIONS as a convenient
    # hook for debugging.
    #
    # If we're running the Docker image using the same UID as the Docker host,
    # then this should be set to false no matter what.
    should_set_permissions: bool = (sys.platform == "linux") or (
        "R2C_ALWAYS_SET_PERMISSIONS" in os.environ
    )

    # Used for storage/copying.
    #
    # Implementation note: we can't use TemporaryDirectory here because of how
    # cleanup() 'optimistically' tries to rmtree the directory before setting
    # permissions. If TemporaryDirectory gets its directory deleted out from
    # under it on 3.6, it complains.
    _temp_dir: Path = attr.ib(init=False)

    @_temp_dir.default
    def _create_temp_dir(self) -> Path:
        return Path(mkdtemp(prefix="r2c-mount-", dir=get_tmp_dir()))

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
        return self._temp_dir / "inputs"

    def output_dir(self) -> Path:
        """Directory that output files will be located in after copy_output()"""
        return self._temp_dir / "output"

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
        if not self.should_set_permissions:
            return

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
            shutil.rmtree(self._temp_dir)
        except PermissionError:
            self._set_permissions()
            shutil.rmtree(self._temp_dir)


@attr.s(auto_attribs=True)
class LocalMountManager(MountManager):
    """Manages mounts for a local Docker instance.

    This copies all to-be-mounted files into a temporary directory.
    """

    # We use bind mounts, so nothing to do for these.

    def copy_input(self) -> None:
        self._set_permissions()

    def copy_output(self) -> None:
        # We don't need to set permissions, since cleanup() will do it if it
        # fails anyway. And if the output is a single file, we won't run into
        # permissions issues, since you can delete a file you don't own inside
        # a folder you do own.
        pass

    def volumes(self) -> Dict:
        return {self._temp_dir: {"bind": str(self.volume_root), "mode": "rw"}}


@attr.s(auto_attribs=True)
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
                f"{self._temp_dir}/.",
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
