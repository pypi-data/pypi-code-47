# TODO docs


from collections import OrderedDict
from functools import lru_cache
from logging import getLogger
from os import R_OK
from os import access
from pathlib import Path

from dfmpy.utils.config import get_config
from dfmpy.utils.config import get_ignore_globs
from dfmpy.utils.files import path_is_directory
from dfmpy.utils.files import path_is_file
from dfmpy.utils.files import path_is_symlink
from dfmpy.utils.files.normalizer import normalize_for_phantom_files
from dfmpy.utils.files.normalizer import normalize_repo_path

# TODO docs
LOG = getLogger()

# TODO docs
# The cache should never get larger than 2, one for $HOME and one for the repo
# dir.  There should be no need for a cache of any other directory.
__FILE_TREE_CACHE_SIZE = 2


def __ignore(path):
    # TODO docs
    # TODO unit test
    for pattern in get_ignore_globs():
        if path.match(pattern):
            return True
    return False


def __no_permissions_to_stat(path):
    # TODO docs - the path must exist, but is not accessible.
    # TODO unit test
    # TODO is it possible to remove access() in favor or Path() methods?
    return path.exists() and not access(path, R_OK)


def __find_all_paths(dir_path):
    # TODO docs - returns all files and (directories with markers)
    # TODO unit test
    marker = get_config().marker
    if not dir_path.exists():
        return tuple()
    else:
        for path in dir_path.iterdir():
            if __ignore(path):
                LOG.debug('Ignoring: %s', path)

            elif __no_permissions_to_stat(path):
                LOG.error('No permissions to read: %s', path)

            elif path_is_directory(path):
                if marker in path.name:
                    LOG.debug('Found special directory: %s', path)
                    yield path
                else:
                    LOG.debug('Traversing down directory: %s', path)
                    yield from get_all_paths(path)

            elif path_is_file(path):
                LOG.debug('Found file: %s', path)
                yield path

            elif path_is_symlink(path):
                LOG.debug('Found symlink: %s', path)
                yield path

            else:
                LOG.error('Found unknown node type: %s', path)


@lru_cache(maxsize=__FILE_TREE_CACHE_SIZE)
def get_all_paths(dir_name):
    # TODO docs - returns the same as __find_all_paths()
    # TODO unit test
    paths = []
    paths.extend(__find_all_paths(Path(dir_name)))
    paths.sort()
    return tuple(paths)


@lru_cache(maxsize=__FILE_TREE_CACHE_SIZE)
def get_installed_paths(install_dir, repo_dir):
    # TODO docs
    # TODO unit test
    LOG.debug('Searching for installed paths under: %s', install_dir)
    installed_paths = get_all_paths(install_dir)
    installed_paths = [p for p in installed_paths if path_is_symlink(p)]
    installed_paths = [p for p in installed_paths
                       if str(p.resolve()).startswith(repo_dir)]
    mapping = OrderedDict()
    mapping.update([(p, Path(p.resolve())) for p in installed_paths])
    return mapping


@lru_cache(maxsize=__FILE_TREE_CACHE_SIZE)
def get_expected_paths(install_dir, repo_dir):
    # TODO docs
    # TODO unit test
    LOG.debug('Searching for expected paths under: %s', repo_dir)
    marker = get_config().marker
    repo_paths = get_all_paths(repo_dir)
    repo_paths = normalize_for_phantom_files(repo_paths)
    repo_paths = [p for p in repo_paths if not __ignore(p)]
    repo_paths = [p for p in repo_paths if marker not in p.name]
    mapping = OrderedDict()
    for rp in repo_paths:
        installed_file = str(rp).replace(repo_dir, install_dir)
        installed_path = Path(installed_file)
        nrp = normalize_repo_path(rp)
        if nrp.resolve().exists():
            mapping[installed_path] = nrp
    return mapping
