"""Deploy command module."""
from .command import Command


class DeployCommand(Command):
    """Deploys a site to LXD hosts."""

    name = 'deploy'

    def configure(self, parser):
        """See Command documentation."""

    def run(self, arguments):
        """See Command documentation."""
