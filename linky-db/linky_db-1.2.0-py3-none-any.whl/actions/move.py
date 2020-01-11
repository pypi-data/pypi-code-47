import logging
import shutil
from pathlib import Path

from linky.config import read_conf
from linky.utils.library_utils import recreate_with_symlinks
from linky.utils.path_utils import find_base, get_path_in_base, get_paths_in_root, \
    is_path_in_base, get_first_dir, get_cat_tag


def move(*paths):
    """

    @param paths: At least 2 paths.
                  >2 means the last path will be interpreted as a directory
    @type paths: list[Path]
    @return:
    @rtype:
    """
    if len(paths) < 2:
        raise ValueError("Need at least 2 paths")
    sources = paths[:-1]
    new_path = paths[-1]

    if len(sources) == 1:
        _move(sources[0], new_path)
    else:
        for source in sources:
            _move(source, new_path, target_is_dir=True)


def _move(path, new_path, target_is_dir=False):
    logger = logging.getLogger("move")
    base_path = find_base(path)

    config = read_conf(path)
    categories = config.categories.keys()

    # When moving into a directory tack on the name of item being moved
    target_is_dir = target_is_dir or new_path.is_dir()
    if target_is_dir:
        new_path = new_path / path.name

    _check_move_params(path, new_path, base_path, categories)

    old_rel_path = get_path_in_base(base_path, path, categories, True)
    try:
        new_rel_path = get_path_in_base(base_path, new_path, categories, True)
    except ValueError:
        raise ValueError("Bad move target", new_path)

    path_in_base = base_path / old_rel_path
    other_links = get_paths_in_root(path, config)
    # First move the file or directory in the base
    new_path_in_base = base_path / new_rel_path
    new_path_in_base.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Moving from '%s' to '%s'", old_rel_path, new_rel_path)
    logger.debug("Moving from '%s' to '%s'", path_in_base, new_path_in_base)
    shutil.move(str(path_in_base), str(new_path_in_base))

    # Then move the other links in the link root

    for other_link in other_links:
        # Remove the relative path from the other link
        # that gets the tag dir or the link root
        dir_root = Path(
            *other_link.parts[:-len(old_rel_path.parts)]
        )
        new_other_path = dir_root / new_rel_path
        if new_path_in_base.is_file():
            other_link.unlink()
        elif new_path_in_base.is_dir():
            shutil.rmtree(other_link)
        logger.info("Moving in other link: '%s' -> '%s'", other_link, new_other_path)
        recreate_with_symlinks(new_other_path, new_path_in_base)


def _check_move_params(path, new_path, base_path, categories):
    """
    Make sure an attempt is being made to make an unsupported move:

     into or out of the root, base, category or tag
    @type path: Path
    @type new_path: Path
    @type base_path: Path
    @type categories: list[basestring]
    """
    in_base = is_path_in_base(path, base_path)
    new_in_base = is_path_in_base(new_path, base_path, False)
    if in_base != new_in_base:
        raise ValueError("Trying to move in or out of base")
    if in_base:
        return
    old_parent = get_first_dir(path, base_path)
    new_parent = get_first_dir(new_path, base_path)

    old_categorized = old_parent in categories
    new_categorized = new_parent in categories
    if old_categorized != new_categorized:
        raise ValueError("Cannot categorize using move")
    if old_categorized and new_categorized:
        old_tag = get_cat_tag(path, base_path.parent)
        new_tag = get_cat_tag(new_path, base_path.parent)
        if old_tag != new_tag:
            raise ValueError("Cannot switch categories or tag using move")
