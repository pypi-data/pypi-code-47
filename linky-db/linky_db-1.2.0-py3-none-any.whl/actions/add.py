import logging
import shutil

from linky.actions.tag import tag
from linky.utils.dupe_handlers import DUPE_HANDLERS, DupeHandler, MergeDupeHandler, \
    ReplaceDupeHandler
from linky.utils.library_utils import move_to_base, recreate_with_symlinks
from linky.utils.path_utils import get_path_in_base, get_paths_in_root, get_cat_tag


def add(path, base_path, config, cat_tag=None, prefix="", linked_root_prefix=False,
        dupe_handler_name=None):
    """
    Imports a path into the base to be managed by linky

    @param path: What we're trying to import
    @type path: Path
    @param base_path: The base into which the item should be imported
    @type base_path: Path
    @type config: linky.config.Config
    @param cat_tag: The predefined tag for a specific category
    @type cat_tag: linky.utils.path_utils.CategoryTagTuple
    @param prefix: An additional prefix to add to the path
                   If config.prefix_at_import is used in addition to this,
                   this prefix will first be added and the standard prefix
                   calculated thereafter
    @type prefix: basestring
    @param linked_root_prefix: Mutually exclusive with prefix and cat_tag.
                                Calculates the prefix within the linked root
                                as well as the category and tag
    @type linked_root_prefix: bool
    @param dupe_handler_name: How dupes will be handled
    @type dupe_handler_name: DupeHandler
    """
    logger = logging.getLogger("actions.add.add")
    logger.info("Adding: %s", path)
    logger.debug("Base path: %s", base_path)

    if linked_root_prefix:
        prefix = get_path_in_base(
            base_path, path,
            categories=config.categories.keys(), relative=True
        ).parent
        cat_tag = get_cat_tag(path, config.base_path.parent)
        logger.debug("Adding linked root prefix '%s'", prefix)

    if cat_tag:
        logger.info("Pre cat-tag: %s", cat_tag)

    dupe_handler = DUPE_HANDLERS.get(dupe_handler_name)  # type: DupeHandler
    try:
        path_in_base = move_to_base(path, base_path, config, prefix)
    except ValueError as value_error:
        if not dupe_handler:
            raise
        path_in_base = value_error.args[1]
        logger.info("Handling dupe with method %s", dupe_handler.NAME)
        dupe_handler(path, path_in_base)
    logger.debug("New path in base '%s'", path_in_base)
    if config.categories:
        if isinstance(dupe_handler, (MergeDupeHandler, ReplaceDupeHandler)):
            logger.debug("Modified existing item in base. Deleting existing tags...")
            _remove_other_paths(path_in_base, config, logger)

        logger.debug("Categorizing and tagging...")
        # Apply default tags for everything
        # except when cat_tag is passed
        for cat_name, category in config.categories.items():
            tag_name = category.default
            if cat_tag is not None and cat_name == cat_tag.c:
                tag_name = cat_tag.t
            tag(path_in_base, "%s/%s" % (cat_name, tag_name), config)
    else:
        logger.info("Simply relinking in root...")
        recreate_with_symlinks(base_path.parent / path_in_base.relative_to(base_path), path_in_base)


def _remove_other_paths(path_in_base, config, logger):
    for other_path in get_paths_in_root(path_in_base, config):
        # Don't delete files
        if not (other_path.is_symlink() or other_path.exists()):
            continue
        if other_path.is_file():
            other_path.unlink()
        else:
            shutil.rmtree(other_path)
        logger.debug("Deleted %s", other_path)
