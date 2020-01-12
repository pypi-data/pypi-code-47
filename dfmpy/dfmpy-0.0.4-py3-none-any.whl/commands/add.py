# TODO docs

from logging import getLogger
from pathlib import Path

from dfmpy.utils.files.normalizer import normalize_file_names
from dfmpy.utils.files.syncer import sync_expected_paths
from dfmpy.utils.config import get_config
from dfmpy.utils.files import mkdir_parents
from dfmpy.utils.files import path_exists

LOG = getLogger()


def __filter_non_destination_paths(paths):
    # TODO docs
    # TODO unit test
    install_dir = get_config().install_dir
    good_paths = []
    for p in paths:
        if not path_exists(p):
            LOG.error('Cannot add non-existent path: %s', p)
        elif not str(p).startswith(install_dir):
            LOG.error('Cannot add path not under destination: %s', p)
        else:
            good_paths.append(p)
    return tuple(good_paths)


def __determine_expected_paths(paths):
    # TODO docs
    # TODO unit test
    repository_dir = get_config().repository_dir
    install_dir = get_config().install_dir

    marker = get_config().marker
    delimiter = get_config().delimiter
    hostname = get_config().hostname
    system_type = get_config().system

    expected_paths = {}
    for p in paths:
        target_path = str(p).replace(install_dir, repository_dir)
        target_path += marker
        target_path += delimiter.join(hostname, system_type)
        expected_paths[p] = Path(target_path)
    return expected_paths


def __move_expected_paths(expected_paths, force):
    # TODO docs
    # TODO unit test
    for old, new in expected_paths.items():
        if not force:
            LOG.info('Simulated renaming %s -> %s', old, new)
        else:
            mkdir_parents(new)
            LOG.info('Renaming %s -> %s', old, new)
            Path(old).rename(new)


def add(files=None, force=False, interactive=False):
    # TODO do not overwrite existing files
    # TODO docs
    # TODO unit test
    # TODO implement interactive
    # TODO implement force
    paths = normalize_file_names(files)
    paths = __filter_non_destination_paths(paths)
    expected_paths = __determine_expected_paths(paths)
    __move_expected_paths(expected_paths, force)
    # TODO make this the next method public, or move to the "files" utility?
    sync_expected_paths(expected_paths, force, interactive)
    # if interactive:
    #     raise NotImplementedError('Interactive not yet implemented.')
    # __install_file('config.ini', overwrite=force)
    # __install_file('ignore.globs', overwrite=force)


def add_main(cli):
    # TODO docs
    # TODO unit test
    add(cli.files,
        cli.force,
        cli.interactive)
