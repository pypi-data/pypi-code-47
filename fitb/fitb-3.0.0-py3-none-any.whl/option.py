class Option:
    """Description of a single configurable option.

    Args:
        name: The name of the option, i.e. its key in the config.
        description: Description of the option.
        default: Default value of the option.
        path: Path segments to the option in the config.
    """
    def __init__(self, name, description, default, path=()):
        self._name = name
        self._description = description
        self._default = default
        self._path = tuple(path)

    @property
    def name(self):
        "The name of the option."
        return self._name

    @property
    def description(self):
        "The description of the option."
        return self._description

    @property
    def default(self):
        "The default value of the option."
        return self._default

    @property
    def path(self):
        "Path leading to option in the config."
        return self._path

    def __repr__(self):
        return "Option(name='{}', description='{}', default={}, path={})".format(
            self.name, self.description, self.default, self.path)

    def __str__(self):
        return "{}: {} [default={}]".format(self.name, self.description, self.default)


def build_default_config(options):
    """Build a default config from an iterable of options.
    """
    config = {}
    for option in options:
        subconfig = config
        for segment in option.path:
            subconfig = subconfig.setdefault(segment, {})
        subconfig[option.name] = option.default
    return config
