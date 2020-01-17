"""Define a simple system of extension-points and extensions.

An extension-point represents a point in a program that can be extended. It comprises a name and a collection of
extensions at that point. Each extension on an extension-point provides a specific "implementation" for that
extension-point.

Extensions themselves comprise a name, a description, a sequence of configurable options, and a method for "activating"
them. This activation produces the object that actually embodies the implementation of the extension.
"""

import logging

from .extension import Extension
from .option import Option

log = logging.getLogger()


class ExtensionPoint:
    """A named point in a program that can be extended.
    """

    def __init__(self, name):
        self._name = name
        self._extensions = {}

    @property
    def name(self):
        "The name of the extension point."
        return self._name

    def add(self, name, description, activate, config_options=()):
        """Add an extension to the point.
        """
        extension = Extension(
            name=name,
            description=description,
            config_options=config_options,
            activate=activate)

        if extension.name in self._extensions:
            raise ValueError(
                'Extension {} already in {}'.format(extension.name, self))

        self._extensions[extension.name] = extension

    def activate(self, name, config):
        """Activate an extension.

        Args:
            name: The name of the extension to activate.
            config: The full config dict.

        Returns:
            The activate extension object (i.e. as returned from the extension on activation).

        Raises:
            KeyError: There is no extension named `name`.
        """
        return self._extensions[name].activate(
            config,
            config.get(self.name, {}).get(name, {}))

    def config_options(self):
        """All configurable options for this extension point.

        Iterable of Options.
        """
        for extension in self._extensions.values():
            path = (self.name, extension.name)
            for option in extension.config_options:
                yield Option(
                    name=option.name,
                    description=option.description,
                    default=option.default,
                    # Each option path is "translated" into the overall config
                    path=option.path + path
                )

    def __getitem__(self, name):
        """Get the extension object with the given name.

        Returns: An Extension instance.

        Raises:
            KeyError: There is no extension with that name.
        """
        return self._extensions[name]

    def __iter__(self):
        "Iterable of extension names."
        return iter(self._extensions.values())

    def __repr__(self):
        return "ExtensionPoint(name='{}')".format(self.name)
