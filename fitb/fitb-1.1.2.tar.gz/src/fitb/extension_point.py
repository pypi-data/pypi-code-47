"""Define a simple system of extension-points and extensions.

An extension-point represents a point in a program that can be extended. It comprises a name and a collection of
extensions at that point. Each extension on an extension-point provides a specific "implementation" for that
extension-point.

Extensions themselves comprise a name, a description, a sequence of configurable options, and a method for "activating"
them. This activation produces the object that actually embodies the implementation of the extension.
"""

import logging
from fitb.utilities import merge

from .extension import Extension

log = logging.getLogger()


class ExtensionPoint:
    """A named point in a program that can be extended.
    """

    def __init__(self, name):
        self._name = name
        self._extensions = []
        self._activated = {}

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

        if extension.name in (x.name for x in self._extensions):
            raise ValueError(
                'Extension {} already in {}'.format(extension.name, self))

        self._extensions.append(extension)

    def activate(self, config):
        """Activate all extensions.
        """
        for extension in self._extensions:
            self._activated[extension.name] = extension.activate(
                config,
                config.get(self.name, {}).get(extension.name, {}))

    def default_config(self):
        config = {}
        for extension in self._extensions:
            merge(
                config,
                {
                    extension.name: {
                        option.name: option.default
                        for option in extension.config_options
                    }
                }
            )
        return config

    def __getitem__(self, name):
        "Get a configured extension object with the given name."
        return self._activated[name]

    def names(self):
        "Iterable of activated extension names."
        return iter(self._activated)

    def __repr__(self):
        return "ExtensionPoint(name='{}')".format(self.name)
