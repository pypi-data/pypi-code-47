# -*- coding: utf-8 -*-
__all__ = ('DockerDaemon',)

from loguru import logger
from docker.models.containers import Container as DockerContainer
import attr
import docker

from .container import Container


@attr.s(frozen=True)
class DockerDaemon:
    """Maintains a connection to a Docker daemon."""
    url: str = attr.ib(default='unix://var/run/docker.sock')
    client: docker.DockerClient = \
        attr.ib(init=False, eq=False, hash=False, repr=False)
    api: docker.APIClient = \
        attr.ib(init=False, eq=False, hash=False, repr=False)

    def __attrs_post_init__(self) -> None:
        api = docker.APIClient(self.url)
        client = docker.DockerClient(self.url)
        object.__setattr__(self, 'client', client)
        object.__setattr__(self, 'api', api)
        logger.debug(f"created daemon connection: {self}")

    def __enter__(self) -> 'DockerDaemon':
        return self

    def __exit__(self, ex_type, ex_val, ex_tb) -> None:
        self.close()

    def close(self) -> None:
        logger.debug(f"closing daemon connection: {self}")
        self.api.close()
        self.client.close()
        logger.debug(f"closed daemon connection: {self}")

    def attach(self, id_or_name: str) -> Container:
        """Attaches to a running Docker with a given ID or name."""
        logger.debug(f"attaching to container with ID or name [{id_or_name}]")
        docker_container = self.client.containers.get(id_or_name)
        container = Container(daemon=self, docker=docker_container)
        logger.debug(f"attached to container [{container}]")
        return container

    def provision(self, image: str) -> Container:
        """Creates a Docker container from a given image."""
        logger.debug(f"provisioning container for image [{image}]")
        docker_container = \
            self.client.containers.run(image, stdin_open=True, detach=True)
        container = self.attach(docker_container.id)
        logger.debug(f"provisioned container [{container}]"
                     f" for image [{image}]")
        return container
