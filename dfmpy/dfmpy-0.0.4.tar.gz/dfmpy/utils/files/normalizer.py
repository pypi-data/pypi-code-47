# TODO docs

from os.path import expanduser
from os.path import expandvars
from pathlib import Path

from dfmpy.utils.config import get_config
from dfmpy.utils.files.constants import suffixes


def normalize_for_phantom_files(file_paths):
    # TODO docs - explain this shit!  explain why it's needed when determining expected files when there only exists a markered file (and not the equivalent non-marked file).
    # TODO use this with EXTREME caution, since it's a hack it causes too many side-effects in other places -- causing misleading bugs.
    # TODO unit test
    # TODO optimize this? so it does not iterate over the list many times! (eg use of "in" keyword).
    file_paths = list(file_paths)
    marker = get_config().marker
    for fp in file_paths:
        file_name = str(fp)
        if marker in file_name:
            marker_index = file_name.find(marker)
            phantom_file_name = file_name[:marker_index]
            phantom_file_path = Path(phantom_file_name)
            if phantom_file_path not in file_paths:
                file_paths.append(phantom_file_path)
    file_paths.sort()
    return tuple(file_paths)


def normalize_repo_path(file_path):
    # TODO docs
    # TODO unit test
    file_name = str(file_path)
    for suffix in suffixes():
        file_with_suffix = file_name + suffix
        if Path(file_with_suffix).exists():
            return Path(file_with_suffix)
    return Path(file_path)


def normalize_file_names(files):
    # TODO docs
    # TODO unit test
    if not files:
        files = []
    files = [expanduser(expandvars(f)) for f in files]
    files = [Path(f).absolute() for f in files]
    return tuple(files)
