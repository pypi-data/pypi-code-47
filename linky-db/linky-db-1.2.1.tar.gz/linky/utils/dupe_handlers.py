import shutil

from linky.utils import path_utils


class DupeHandler:
    """
    A base class for handling duplicate paths
    """
    NAME = None

    def __call__(self, path, new_path):
        raise NotImplementedError()


class KeepDupeHandler(DupeHandler):
    """
    Keeps the destination and removes the source.
    """

    NAME = "keep"

    def __call__(self, path, new_path):
        """
        @type path: pathlib.Path
        @type new_path: pathlib.Path
        """
        if path.is_file():
            path.unlink()
        else:
            shutil.rmtree(path)


class MergeDupeHandler(DupeHandler):
    """
    Merges directories.
    Files will be moved and empty directories will be ignored
    """
    NAME = "merge"

    def __call__(self, path, new_path):
        """
        @type path: pathlib.Path
        @type new_path: pathlib.Path
        """
        if not path.is_dir():
            raise ValueError("Source is not a directory", path)
        if not new_path.is_dir():
            raise ValueError("Destination is not a directory", new_path)

        for abs_item, rel_item in path_utils.walk(path):
            abs_new_item = new_path / rel_item

            # Ignore directories and older source files
            if abs_item.is_dir() or \
                    (abs_new_item.is_file() and
                     abs_new_item.stat().st_mtime < abs_item.stat().st_mtime):
                continue
            # Move files
            abs_item.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(abs_item, abs_new_item)
        shutil.rmtree(path)


class ReplaceDupeHandler(DupeHandler):
    """
    Replaces the destination with a source
    """
    NAME = "replace"

    def __call__(self, path, new_path):
        """
        @type new_path: pathlib.Path
        """
        shutil.move(str(path), str(new_path))


class ReplaceOldDupeHandler(DupeHandler):
    """
    Replaces the destination if the source is new
    """
    NAME = "replace_old"

    def __call__(self, path, new_path):
        """
        @type new_path: pathlib.Path
        """
        if new_path.stat().st_mtime > path.stat().st_mtime:
            return
        shutil.move(str(path), str(new_path))


DUPE_HANDLERS = {
    c.NAME: c
    for c in (
        KeepDupeHandler(),
        MergeDupeHandler(),
        ReplaceDupeHandler(),
        ReplaceOldDupeHandler(),
    )}
