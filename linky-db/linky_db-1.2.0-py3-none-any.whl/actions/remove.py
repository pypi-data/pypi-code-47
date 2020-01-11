import logging
import shutil

from linky.config import read_conf
from linky.utils import path_utils


def remove(path):
    """
    Permanently removes a file or directory from linky management

    @param path: What we're trying to delete
    @type path: Path
    """
    logger = logging.getLogger("actions.remove")
    logger.debug("Removing: %s", path)
    config = read_conf(path)
    base_path = config.base_path
    logger.debug("Base path: %s", base_path)

    path_in_base = path_utils.get_path_in_base(base_path, path, config.categories.keys())
    other_paths = path_utils.get_paths_in_root(path_in_base, config)

    for other_path in other_paths + [path_in_base]:
        if other_path.is_symlink() or other_path.is_file():
            other_path.unlink()
        elif other_path.is_dir():
            shutil.rmtree(other_path)
        logger.info("Removed %s", other_path)

        # Make sure to remove empty parent directories
        other_parent = other_path.parent
        if other_parent != base_path and other_parent.is_dir() and not list(other_parent.iterdir()):
            shutil.rmtree(other_parent)
