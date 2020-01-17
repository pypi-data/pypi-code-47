"""Support for loading/getting configuration dictionaries.
"""

import fitb
import toml


class Config(fitb.Profile):
    """Combines the notion of a fitb.Profile, a root-path, and
    a configuration dictionary into a single entity.
    """

    def __init__(self, root_path):
        super().__init__()

        # self._root_path = root_path

        for ep in fitb.load_from_pkg_resources('godkjenn'):
            self.extension_points.add(ep)

        self.add_option(
            fitb.Option(name='vault_type',
                        description='Type of vault to use',
                        default='fs-vault'))

        self.add_option(
            fitb.Option(name='differ_type',
                        description='Type of differ to use',
                        default='text'))

        self.add_option(
            fitb.Option(name='comparator_type',
                        description='Type of comparator to use',
                        default='exact'))

        self._config = fitb.build_default_config(
            self.options())

        self._config['root_path'] = root_path
        # if config_file is not None:
        #     config_dict = fitb.merge(
        #         config_dict,
        #         load_config(config_file))

    def add_config(self, config):
        self._config = fitb.merge(self._config, config)

    def get_vault(self):
        return self.extension_points['vault'].activate(
            self._config['vault_type'], self._config)

    def get_comparator(self):
        return self.extension_points['comparator'].activate(
            self._config['comparator_type'], self._config)

    def get_differ(self):
        return self.extension_points['differ'].activate(
            self._config['differ_type'], self._config)

    # @property
    # def root_path(self):
    #     return self._root_path


def deserialize_config(config_string):
    config = toml.loads(config_string)
    return config.get('godkjenn', {})


def load_config(path):
    return deserialize_config(
        path.read_text(encoding='utf-8'))


def serialize_config(config):
    return toml.dumps({'godkjenn': dict(config)})


def save_config(config, path):
    config_string = serialize_config(config)
    path.write_text(config_string, encoding='utf-8')
