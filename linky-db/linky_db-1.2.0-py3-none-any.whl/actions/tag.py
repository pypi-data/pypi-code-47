import logging
import shutil
from collections import defaultdict
# pylint: disable=unused-import
from pathlib import Path

from linky.utils import path_utils
from linky.utils.library_utils import recreate_with_symlinks
from linky.utils.path_utils import get_first_dir, get_paths_in_root, get_path_in_base, get_cat_tag


def tag(paths, cat_tags, config, delete=False, best_effort=False):
    """
    Apply (or delete) multiple tags to multiple paths

    @param paths: The absolute paths. Paths will be wrapped in a string
    @type paths: list[Path] | Path
    @param cat_tags: List of "<category>/<tag>" string
    @type cat_tags: list[basestring] | basestring
    @type config: linky.config.Config
    @param delete: Removes the tag instead of applying it
    @type delete:
    @param best_effort: Ignores errors applying/deleting tags and tries to
                        treat every path
    @type best_effort: bool
    @return:
    @rtype:
    """
    logger = logging.getLogger("tag_multiple")
    if not isinstance(paths, list):
        paths = [paths]
    if not isinstance(cat_tags, list):
        cat_tags = [cat_tags]
    # First clean and separate tags and group them to reduce useless actions
    cleaned_cat_tags = defaultdict(set)
    for cat_tag in cat_tags:
        cat, _tag = [split.strip() for split in cat_tag.split("/")]
        cleaned_cat_tags[cat].add(_tag)

    # Apply tags
    for path in paths:
        # Use the path in the base since tagging might delete the old path
        # in the linked root
        for rel_path_in_base in _iter_path_to_tag(path, config):
            for cat, tags in cleaned_cat_tags.items():
                try:
                    delete = _apply_cat_tags(cat, tags, path, rel_path_in_base, config, delete,
                                             best_effort)
                # pylint: disable=bare-except
                except:
                    if not best_effort:
                        raise
                    logger.warning(
                        "Error ignored while handling path='%s', category='%s', delete='%s'",
                        path, cat, delete
                    )


def _apply_cat_tags(category, tags, path, rel_path_in_base, config, delete, best_effort):
    if category not in config.categories:
        raise ValueError("Unknown category: %s" % category)
    logger = logging.getLogger("tag.apply_cat_tags")
    category_o = config.categories[category]
    other_paths = get_paths_in_root(
        config.base_path / rel_path_in_base, config, category=category
    )
    for _tag in tags:
        try:
            if not category_o.extensible and _tag not in category_o.tags:
                raise ValueError("Unknown tag in %s: %s" % (category, _tag))
            delete, _tag = _check_delete(delete, category_o, _tag, other_paths)
            tag_once(rel_path_in_base, category, _tag, other_paths, config, delete=delete)
        # pylint: disable=bare-except
        except:
            if not best_effort:
                raise
            logger.warning(
                "Error ignored while handling path='%s', category='%s', tag='%s', delete='%s'",
                path, category, _tag, delete
            )
    return delete


def _iter_path_to_tag(path, config):
    """
    Yields files in the given path in order to tag files instead of directories

    @param path:
    @type path: Path
    @param config:
    @type config: linky.config.Config
    @rtype: collections.Iterable[Path]
    """
    if not path.exists():
        raise FileNotFoundError(path)

    base_path = config.base_path
    linked_root = base_path.parent
    current_parent = get_first_dir(path, base_path)
    category_parent = current_parent in config.categories.keys()

    if category_parent:
        distance_from_root = len(path.relative_to(linked_root).parts)

        # Check if we're actually the root
        if distance_from_root == 0:
            raise ValueError("Cannot tag the root")

        # Check whether the given path is a category path
        if distance_from_root == 1:
            raise ValueError("Cannot tag a category")

        # Check whether the given path is a tag path
        if distance_from_root == 2:
            raise ValueError("Cannot tag a tag")
    path_in_base = get_path_in_base(base_path, path, categories=config.categories.keys())
    if path_in_base.is_dir():
        for _abs_path, _ in path_utils.walk(path_in_base, include_dirs=False):
            yield _abs_path.relative_to(base_path)
    else:
        yield path_in_base.relative_to(base_path)


def _check_delete(delete, category_o, tag_str, other_paths):
    if delete:
        # Exclusive tag_once applies default on deletion
        # Removing the last applied tag_once also has the same effect
        if category_o.exclusive or len(other_paths) == 1:
            tag_str = category_o.default
            delete = False
    return delete, tag_str


def tag_once(rel_path_in_base, category_str, tag_str, other_paths, config, delete=False):
    """
    Adds a tag to a file or directory

    :type rel_path_in_base: Path
    :type category_str: basestring
    :type tag_str: basestring
    :type other_paths: list[Path]
    :type config: linky.config.Config
    :param delete: reverses the action to removing the tag_once instead of adding it
    :type delete: bool
    """
    logger = logging.getLogger("tag_once")
    category_o = config.categories[category_str]
    base_path = config.base_path
    linked_root = base_path.parent
    # Build new parent
    new_path = linked_root / category_str / tag_str / rel_path_in_base
    sub_logger = logger.getChild(str(rel_path_in_base))
    if new_path.exists():
        if delete:
            if new_path.is_file():
                new_path.unlink()
            else:
                shutil.rmtree(new_path)
            path_utils.del_empty_parents(new_path)
        else:
            logger.info("Already correctly tagged")
        return

    to_delete = _collect_deletion_candidates(
        base_path, category_o, other_paths, tag_str
    )

    # Actually do the tagging
    recreate_with_symlinks(new_path, base_path / rel_path_in_base)
    sub_logger.info("Tagged %s/%s", category_str, tag_str)

    # Clean up
    if to_delete:
        sub_logger.info("Deleting old tags...")
    for item in to_delete:
        try:
            if item.is_file():
                item.unlink()
            else:
                shutil.rmtree(item, ignore_errors=True)
            path_utils.del_empty_parents(item)
        except FileNotFoundError:
            pass
        if sub_logger.level <= logging.INFO:
            sub_logger.info("\t%s", get_cat_tag(item, base_path.parent))


def _collect_deletion_candidates(base_path, category_o, other_paths, tag_str):
    to_delete = []
    # Handle exclusiveness
    if category_o.exclusive or (tag_str == category_o.default and category_o.exclusive_default):
        # Filter to current category only
        to_delete.extend(other_paths)
    elif category_o.exclusive_default:
        # Delete the exclusive default if it's among the paths
        for other_path in other_paths:
            if get_cat_tag(other_path, base_path.parent).t == category_o.default:
                to_delete.append(other_path)
    return [
        item for item in to_delete
        # Don't delete files that aren't symlinks
        if (item.is_file() and item.is_symlink()) or item.is_dir()
    ]
