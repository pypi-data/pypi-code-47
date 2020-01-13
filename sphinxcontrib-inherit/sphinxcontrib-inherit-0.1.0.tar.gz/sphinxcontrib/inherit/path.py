# This file is part of the sphinxcontrib-inherit extension.
# Please see the COPYRIGHT and README.rst files at the top level of this
# repository for full copyright notices, license terms and support information.
from pathlib import Path


def path_contains(path, other_path):
    path_parts = Path(other_path).parts
    if len(path.parts) > len(path_parts):
        return False
    if path.is_absolute() != Path(other_path).is_absolute():
        return False
    return all(t == s for t, s in zip(path.parts, path_parts))


def path_subdir_contains(path, other_path):
    return (
        path_contains(path, other_path) and
        (len(Path(other_path).parts) - len(path.parts)) > 1)
