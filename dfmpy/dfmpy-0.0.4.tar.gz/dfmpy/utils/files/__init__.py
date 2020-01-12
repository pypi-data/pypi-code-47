# TODO package level docs

# TODO docs
__all__ = tuple([
    'mkdir_parents'
    'path_is_directory',
    'path_is_file',
    'path_is_symlink',
    'path_exists',
])

from logging import getLogger

from dfmpy.utils.files.normalizer import normalize_for_phantom_files
from dfmpy.utils.files.normalizer import normalize_repo_path

# TODO docs
LOG = getLogger()


def mkdir_parents(symlink_path):
    # TODO docs
    # TODO unit test
    if not symlink_path.parent.exists():
        LOG.warning('Making directory with parents: %s', symlink_path.parent)
        symlink_path.parent.mkdir(parents=True)


def path_is_directory(path):
    # TODO docs - explain why path.is_dir() alone is not safe.
    # TODO unit test
    return path_exists(path) and path.is_dir() and not path.is_symlink()


def path_is_file(path):
    # TODO docs - explain why path.is_file() alone is not safe.
    # TODO unit test
    return path_exists(path) and path.is_file()


def path_is_symlink(path):
    # TODO docs - explain why path.is_symlink() alone is not safe.
    # TODO unit test
    return path_exists(path) and path.is_symlink()


def path_exists(path):
    # TODO docs - explain why path.exists() alone is not safe.
    # TODO unit test
    try:
        # Stat the path, but do not follow symlinks.
        path.lstat()
        return True
    except FileNotFoundError:
        return False
