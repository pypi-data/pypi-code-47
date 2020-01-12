class Extension:
    """Metadata for an extension.

    This describes the configuration options for an extension, and it provides
    a way to configure the extension.
    """

    def __init__(self, name, description, activate, config_options=()):
        self._name = name
        self._description = description
        self._config_options = tuple(config_options)
        self._activate = activate

    @property
    def name(self):
        "The name of the extension."
        return self._name

    @property
    def description(self):
        "A description of the extension."
        return self._description

    def activate(self, full_config, extension_config):
        return self._activate(full_config, extension_config)

    @property
    def config_options(self):
        "An iterable of ConfigOptions for the extension."
        return self._config_options

    def __repr__(self):
        return "Extension(name='{}')".format(self.name)

