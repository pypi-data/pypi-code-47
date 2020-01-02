"""
config handles loading configuration from file system.
"""

from pathlib import Path

from ruamel.yaml import YAML

__all__ = (
    'load',
    'loads',
    'Config',
)

CURRENT_VERSION = 0
SUPPORTED_VERSIONS = (0,)


def load(fp, *, file=""):
    """
    load loads configurations from file reader.
    """
    return loads(fp.read(), file=file)


def loads(s, *, file=""):
    """
    loads loads configurations from string.
    """
    obj = _load_obj(s)
    if file == "":
        cwd = Path(cwd)
    else:
        file_path = Path(file)
        if not file_path.is_file():
            raise ValueError("'file' should be a valid file path")
        cwd = file_path.parent

    version = _parse_version(obj.get("version", 0))

    includes = {"": Path(file)}  # name -> Path mapping
    new_includes = _parse_includes(obj.get("includes", {}), cwd=cwd)
    while new_includes:
        next_includes = {}
        for path in new_includes.values():
            included_obj = _load_obj(path)
            next_includes.update(_parse_includes(
                included_obj.get("includes", {}), includes, cwd=path.parent))

            includes.update(next_includes)

        new_includes = next_includes

    services = []
    unresolved = obj.get("services", [])
    while unresolved:
        service = unresolved.pop(0)
        if 'stack' in service:
            if len(service) != 1:
                raise ValueError("unexpected keys in service: {}".format(", ".join(
                    key for key in service if key != "service")))

    return Config(services, path=str(cwd), version=version, includes=includes)


def _parse_stack(service):
    if 'stack' in service:
        if len(service) != 1:
            raise ValueError("unexpected keys in service: {}".format(", ".join(
                key for key in service if key != "service")))


def _load_obj(s):
    yaml = YAML()
    return yaml.load(s)


def _parse_version(version):
    if not isinstance(version, int):
        raise ValueError("Invalid version {}".format(version))

    if version == 0:
        version = CURRENT_VERSION

    if version not in SUPPORTED_VERSIONS:
        raise NotImplementedError(
            "Version {} is not supported".format(version))

    return version


def _parse_includes(includes, curr_includes=None, *, cwd=""):
    if not isinstance(includes, list):
        raise ValueError(
            "Expect includes to be a list of included configs")

    if curr_includes is None:
        curr_includes = {}

    cwd = Path(cwd)

    ret = {}

    for item in includes:
        if 'name' not in item:
            raise ValueError("includes.item should have attribute 'name'")

        if 'path' not in item:
            raise ValueError("includes.item should have attribute 'path'")

        name, path = item.get('name'), cwd.joinpath(item.get('path'))
        if name == "":
            raise ValueError("includes.item.name cannot be an empty string")

        if not path.is_file():
            raise ValueError(
                "Path {} should point to a config file".format(path))

        if name in curr_includes or name in ret:
            if curr_includes[name].samefile(path) or ret[name].samefile(path):
                continue

            raise ValueError((
                "Duplicate name '{}' but different config "
                "paths ({} and {}) defined in 'includes' section").format(
                    name, curr_includes[name], path))

        ret[name] = path

    return ret


class Config:
    """
    Config stores and validates configuration.
    """

    def __init__(self,
                 services=None,
                 *,
                 path="",
                 version=0,
                 includes=None):
        super().__init__()

        self.path = path
        self.version = version
        self.includes = includes or {}
        self.services = services or []
        self.service_map = {srv.get("name"): srv for srv in self.services}
