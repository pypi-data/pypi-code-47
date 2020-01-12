# TODO docs

from logging import getLogger

# TODO remove dependency on other commands
from dfmpy.utils.config import get_config
from dfmpy.utils.files.deleter import remove_broken_files
from dfmpy.utils.files.finder import get_expected_paths
from dfmpy.utils.files.finder import get_installed_paths
from dfmpy.utils.files.syncer import sync_expected_paths

# TODO docs
LOG = getLogger()


def sync(force=False, interactive=False):
    # TODO docs
    # TODO unit test

    install_dir = get_config().install_dir
    repository_dir = get_config().repository_dir

    expected_paths = get_expected_paths(install_dir, repository_dir)
    installed_paths = get_installed_paths(install_dir, repository_dir)

    if not force:
        LOG.error("Must use '-f' to force overwriting of symlinked dotfiles.")

    sync_expected_paths(expected_paths, force, interactive)
    remove_broken_files(installed_paths, force, interactive)


def sync_main(cli):
    # TODO docs
    # TODO unit test
    sync(cli.force, cli.interactive)
