import os
import re
from collections import namedtuple
from os.path import commonpath, abspath
from pathlib import Path

BASE_NAME = ".base"
CONFIG_DIR_NAME = ".linky"

RESERVED_DIR_NAMES = (BASE_NAME, CONFIG_DIR_NAME)

ALNUM_REGEX = re.compile(r"[a-z0-9]", re.IGNORECASE)


class CategoryTagTuple(namedtuple("_CategoryTagTuple", ["c", "t"])):
    """
    A specialized tuple to hold a category and a tag.

    It simply has a specialized __str__ function
    """

    def __str__(self):
        return "%s/%s" % (self.c, self.t)


def get_dir_prefix(name):
    """
    Calculates the 1 to 2 directory prefix for a name

    Example:

        Avadakedavra --> [ A , Ava]
        Lol --> [L]
        Ba --> [B]
        '' --> []

    :param name: A file or folder name
    :type name: basestring
    :return: prefix for long enough names or empty list
    :rtype: list[str]
    """
    res = "".join(ALNUM_REGEX.findall(name))
    prefix = []
    res_len = len(res)
    if res_len > 1:
        comp_1 = res[0].upper()
        if res_len <= 3:
            prefix = [comp_1]
        else:
            prefix = [comp_1, res[:3].capitalize()]

    return prefix


def get_prefixed_path(path):
    """
    Prefix a path name with a linky directory prefix

    >>>> get_prefixed_path(Path("/opt/link_root/some_item")
    >>>> # Path("/opt/link_root/S/Som/some_item")

    @see: get_dir_prefix
    @type path: Path
    @rtype: Path
    """
    return Path(*[
        path.parent,
        *get_dir_prefix(path.name),
        path.name
    ])


def get_path_in_base(base_path, target, categories=None, relative=False):
    """

    :param base_path:
    :type base_path: Path
    :param target:
    :type target: Path
    :type categories: list | tuple | None
    :param relative: Make sure the path we return is relative to the base
    :type relative: bool
    :rtype: Path
    """
    if not (base_path.is_absolute() and target.is_absolute()):
        raise ValueError("Paths have to be absolute")

    if target == base_path:
        raise ValueError("Cannot target the base path")
    if target == base_path.parent:
        raise ValueError("Cannot target the link root")
    if str(target).startswith(str(base_path / CONFIG_DIR_NAME)):
        raise ValueError("Cannot target the config dir or its contents")

    common_path = Path(commonpath([base_path, target]))
    if common_path == base_path:
        if relative:
            return target.relative_to(base_path)
        return target
    try:
        relative_target = target.relative_to(base_path.parent)
    except ValueError:
        raise ValueError("Cannot target path outside of root")

    cut_depth = 0
    if is_path_in_base(target, base_path):
        # Being in
        cut_depth = 1
    elif categories is not None and relative_target.parts[0] in categories:
        # Is the target manage or not
        # Being in a category means, it has to be
        # So we ignore the first 2 directories: category and tag
        cut_depth = 2

    ret = Path(*[
        base_path if not relative else "",
        *relative_target.parts[cut_depth:]
    ])
    return ret


def is_path_in_base(path, base_path=None, check_exist=True):
    """
    :type path: Path
    :type base_path: Path | None
    :param check_exist: Additional check whether the path actually exists
    :type check_exist: bool
    """
    if check_exist and not path.exists():
        return False

    if base_path:
        try:
            path.relative_to(base_path)
            return True
        # pylint: disable=bare-except
        except:
            return False
    else:
        for part in reversed(path.parts):
            if part == BASE_NAME:
                return True
        return False


def get_paths_in_root(path, config, category=None):
    """
    Finds other symlinks to the given file in the linked root.

    @param path: When given a path outside of the base, the corresponding path in base is used
    @type path: Path
    @type config: Config
    @param category: Limits the search of other symlinks to this category
    @type category: basestring | None
    @rtype: list[Path]
    """
    base_path = _check_path_and_category(path, category, config)

    link_root = base_path.parent
    category_names = config.categories.keys()
    paths = []

    if is_path_in_base(path, base_path):
        rel_path = path.relative_to(base_path)
    else:
        first_parent = get_first_dir(path, base_path)
        rel_path = path.relative_to(link_root)
        # Is it tagged?
        if first_parent in category_names:
            # Remove category and tag
            rel_path = Path(*rel_path.parts[2:])

    def add_possible_path(root):
        possible_path = root / rel_path
        if possible_path.exists():
            paths.append(possible_path)

    for item in link_root.iterdir():
        if item.name == BASE_NAME:
            continue
        # Filter by category if requested
        if category and item.name != category:
            continue
        if item.name in category_names:
            for tag in item.iterdir():
                add_possible_path(tag)
        else:
            add_possible_path(item)
    return paths


def _check_path_and_category(path, category, config):
    if not path.exists():
        raise ValueError("Path doesn't exist")

    if not path.is_absolute():
        raise ValueError("Path must be absolute")

    base_path = config.base_path
    if path == base_path:
        raise ValueError("Can't target base")
    if path == base_path.parent:
        raise ValueError("Can't target linked root")
    if category is not None and category not in config.categories:
        raise ValueError("Unknown category")
    return base_path


def find_base(current_dir, max_count=None, current_count=1):
    """
    Find first parent with a basedir

    :type current_dir: Path
    :type max_count: int
    :type current_count: int
    :rtype: Path
    """
    if current_dir.is_file():
        return find_base(current_dir.parent, max_count, current_count)
    if max_count and current_count > max_count:
        raise StopIteration("Maximum height reached without finding base")
    for entry in current_dir.iterdir():
        if entry.is_dir() and entry.name == BASE_NAME:
            return entry
    if str(current_dir) == current_dir.root:
        raise ValueError("Reached root without finding base")
    return find_base(current_dir.parent, max_count, current_count + 1)


def get_first_dir(path, base_path=None):
    """

    :param path:
    :type path: Path
    :param base_path:
    :type base_path:
    :return:
    :rtype: basestring
    """
    if not path.is_absolute():
        raise ValueError("Please provide an absolute path")
    if not base_path:
        base_path = find_base(path)
    root = base_path.parent
    if path == root:
        raise ValueError("Can't get first directory from root")
    rel_path = path.relative_to(root)
    first = rel_path.parts[0]

    return first


def get_path_props(path):
    """
    Compile select information about a path

    @type path: Path
    @rtype: dict
    """
    return {
        "is_symlink": path.is_symlink(),
        "is_dir": path.is_dir(),
        "is_file": path.is_file(),
    }


def get_cat_tag(path, link_root):
    """
    Guess the category and tag of a path in the link root

    We assume it actually is a categorized/tagged path in the linked root

    @type path: Path
    @type link_root: Path
    @rtype: CategoryTagTuple
    """
    rel = path.relative_to(link_root)
    return CategoryTagTuple(rel.parts[0], rel.parts[1])


def iter_linked_root(root_path, config):
    """
    Iterates over a linked root only returning managed (or to be managed) elements.

    That means it will return the contents of the directory and category-tag directories.
    It will NOT return:

     - category directories themselves
     - tag directories themselves
     - the base directory itself
     - nor the base directory contents

    @type root_path: Path
    @type config: Config
    """
    category_dict = config.categories
    for entry in root_path.iterdir():
        if entry.name == BASE_NAME:
            continue
        # Entry category folder
        if entry.is_dir() and entry.name in category_dict:
            for tag_dir in entry.iterdir():
                for tagged_entry in tag_dir.iterdir():
                    yield tagged_entry, CategoryTagTuple(entry.name, tag_dir.name)
        else:
            yield entry, None


def walk(path, topdown=True, include_dirs=True, include_files=True):
    """
    Simplified os.walk yielding the absolute and relative path per item

    @type path: Path
    @param topdown: Whether to navigate from the top of the directory structure
    @type topdown: bool
    @param include_dirs: Adds directories to the items to yield in each directory
    @type include_dirs: bool
    @param include_files: Adds files to the items to yield in each directory
    @type include_files: bool
    """
    for current_dir, dirnames, filenames in os.walk(path, topdown=topdown):
        current_dir = Path(current_dir)
        rel_root = current_dir.relative_to(path)
        items = []
        if include_dirs:
            items += dirnames
        if include_files:
            items += filenames
        for item in items:
            yield current_dir / item, rel_root / item


def abs_path(path):
    """
    @type path: basestring
    @rtype: Path
    """
    return Path(abspath(path))


def del_empty_parents(path):
    """
    Deletes the parent of the given path if it's empty,
    then tries to delete the parent's parent, etc.

    @type path: Path
    """
    try:
        path.parent.rmdir()
        del_empty_parents(path.parent)
    # pylint:disable=bare-except
    except:
        pass
