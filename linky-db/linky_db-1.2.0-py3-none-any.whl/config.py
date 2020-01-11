import logging

import pkg_resources
import yamale
import yaml
from yamale.schema import Schema

from linky.utils.path_utils import find_base, CONFIG_DIR_NAME


class Config:
    """
    Container for the configuration of a link root
    """
    FILE_CATEGORIES = "categories.yaml"
    FILE_MAIN = "main.yaml"

    def __init__(self, base_path):
        self._log = logging.getLogger("Config")
        self._categories = {}
        self.prefix_at_import = False
        self.base_path = base_path

    @property
    def categories(self):
        """
        :returns dict[basestring,Category]
        """
        return self._categories

    @categories.setter
    def categories(self, value):
        for name, props in value.items():
            self._categories[name] = Category(**props)
        self._log.debug("Known categories: %s", ",".join(self._categories.keys()))


class Category:
    """
    A container for a category's configuration
    """

    def __init__(self,
                 default=None,
                 extensible=False,
                 exclusive_default=False,
                 exclusive=False,
                 tags=None
                 ):
        self.default = default
        self.extensible = extensible
        self.exclusive_default = exclusive_default
        self.exclusive = exclusive
        self.tags = tags or []


def _get_schema(name):
    schema_stream = pkg_resources.resource_stream(
        "linky", "schemas/%s.schema.yaml" % name
    )
    try:
        Loader = yaml.CSafeLoader
    except AttributeError:  # System does not have libyaml
        Loader = yaml.SafeLoader

    raw_schemas = list(yaml.load_all(schema_stream, Loader=Loader))
    # First document is the base schema
    try:
        schema = Schema(raw_schemas[0], name)
        # Additional documents contain Includes.
        for raw_schema in raw_schemas[1:]:
            schema.add_include(raw_schema)
    except (TypeError, SyntaxError) as ex:
        error = "Schema error in file %s\n" % name
        error += str(ex)
        raise SyntaxError(error)
    finally:
        try:
            schema_stream.close()
        finally:
            pass
    return schema


def read_conf(path):
    """
    :type path: Path
    :returns Config
    """
    base_path = find_base(path)
    config_dir_path = base_path / CONFIG_DIR_NAME

    config = Config(base_path)
    configs_d = {}
    # Validate the configs
    for filename in (config.FILE_MAIN, config.FILE_CATEGORIES):
        config_path = config_dir_path / filename
        if not config_path.is_file():
            continue
        schema = _get_schema(filename.split(".")[0])
        data = yamale.make_data(config_path)
        yamale.validate(schema, data)
        configs_d[filename] = data[0][0]

    main_config = configs_d.get(config.FILE_MAIN)
    if main_config:
        config.prefix_at_import = main_config.get("prefix_at_import", False)

    categories_config = configs_d.get(config.FILE_CATEGORIES)
    if categories_config:
        config.categories = categories_config

    return config
