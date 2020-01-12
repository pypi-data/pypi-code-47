"""Implementation of the 'environment' concept.
"""

import os
from pathlib import Path

import fitb
from godkjenn.config import Config


class Environment:
    """Manages extensions and the overall program configuration.
    """
    def __init__(self):
        self._extension_points = fitb.load_from_pkg_resources('godkjenn')
        self._config = None

    @property
    def config(self):
        if not self.activated:
            raise ValueError('Environment is not yet activated.')
        return self._config

    @property
    def activated(self):
        return self._config is not None

    def activate(self, config):
        self._config = config
        for point in self._extension_points.values():
            point.activate(config)

    def default_config(self, root_path=None):
        if root_path is None:
            root_path = Path(os.getcwd())

        config = Config(
            root_path,
            {
                'vault_type': 'fs-vault',
                'differ_type': 'text',
                'comparator_type': 'exact',
            }
        )
        extension_config = fitb.default_config(*self._extension_points.values())
        fitb.merge(config, extension_config)

        return config

    def get_vault(self):
        """Construct a vault.

        This reads a config dict to determine how to create a vault.

        This will look for the "vault_type" key in the config, defaulting to 'fs-vault'. This indicates the name of the
        vault plugin to use.

        It will then look for the subdict with the same name as the vault type, defaulting to an empty dict if this is
        not found. This subconfig dict is passed to the plugin driver.

        Args: config: A config dict.

        Returns: A vault instance.
        """
        vault_plugin_name = self.config['vault_type']
        extension_point = self._extension_points['vault']
        return extension_point[vault_plugin_name]

    def get_comparator(self):
        """Construct a comparator object.

        Args:
            name: Name of comparator type to get.
            config: A config dict.

        Returns: A comparator instance.
        """
        plugin_name = self.config['comparator_type']
        extension_point = self._extension_points['comparator']
        return extension_point[plugin_name]

    def comparator_names(self):
        """Get all comparator plugin names.

        Returns: An iterable of comparator names.
        """
        extension_point = self._extension_points['comparator']
        return extension_point.names()

    def get_differ(self):
        """Construct a comparator object.

        Args:
            name: Name of comparator type to get.
            config: A config dict.

        Returns: A comparator instance.
        """
        plugin_name = self.config['differ_type']
        extension_point = self._extension_points['differ']
        return extension_point[plugin_name]

    def differ_names(self):
        """Get all differ plugin names.

        Returns: An iterable of differ plugin names.
        """
        extension_point = self._extension_points['differ']
        return extension_point.names()
