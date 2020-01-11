import errno
import os
import shutil
from os.path import relpath
from pathlib import Path

from linky.utils.path_utils import walk, get_dir_prefix


def move_to_base(path, base_path, config, prefix=""):
    """
    Move an item into the base

    @param path: what to move
    @type path: Path
    @type base_path: Path
    @type config: linky.config.Config
    @param prefix: What to prefix the item with in the base
    @type prefix: basestring
    @return: The new path in the base
    @rtype: Path
    """
    if not path.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(path))
    rel_path = Path(path.name)
    if prefix:
        rel_path = Path(prefix) / rel_path
    if config.prefix_at_import:
        rel_path = Path(*[
            *get_dir_prefix(rel_path.parts[0]),
            rel_path
        ])
    new_path = base_path / rel_path

    new_path.parent.mkdir(parents=True, exist_ok=True)
    if new_path.exists():
        raise ValueError("Destination exists. Please choose a dupe handler", new_path)
    shutil.move(path, new_path)

    return new_path


def recreate_with_symlinks(path, symlink_target):
    """
    Recreates a file or directory structure in a new location.
    All files will be relative symlinks

    @param path: The new location
    @type path: Path
    @param symlink_target: What to recreate
    @type symlink_target: Path
    """
    if symlink_target.is_dir():
        for abs_base_item, rel_base_item in walk(symlink_target):
            new_path = (path / rel_base_item)
            if abs_base_item.is_dir():
                # Recreate directory
                new_path.mkdir(parents=True, exist_ok=True)
            else:
                # Link to new path in base
                create_relative_symlink(new_path, abs_base_item)
    elif symlink_target.is_file():
        create_relative_symlink(path, symlink_target)
    else:
        raise ValueError("Symlink target doesn't exist", symlink_target)


def create_relative_symlink(path, symlink_target):
    """
    Creates a relative symlink at the given path.

    @type path: Path
    @type symlink_target: Path | basestring
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    link_path = relpath(symlink_target, path.parent)
    if path.exists():
        if path.resolve(False) == symlink_target:
            return
        path.unlink()
    path.symlink_to(link_path)
