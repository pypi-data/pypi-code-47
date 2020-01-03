"""Command system base class & utilities."""
from abc import abstractmethod


class Command:
    """Base class for a Caasa command."""

    @abstractmethod
    def configure(self, parser):
        """Configure command line arguments for this command.

        Args:
            parser (ArgumentParser) : The argument parser.

        """
        raise NotImplementedError()

    @abstractmethod
    def run(self, arguments) -> int:
        """Run the command.

        Args:
            arguments: Command line arguments configured in configure method.

        """
        raise NotImplementedError()
