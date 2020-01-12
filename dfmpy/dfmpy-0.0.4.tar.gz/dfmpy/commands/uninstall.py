# TODO docs

from logging import getLogger

from dfmpy.utils.config import get_config
from dfmpy.utils.files.deleter import unlink_path
from dfmpy.utils.files.finder import get_installed_paths

# TODO docs
LOG = getLogger()


def uninstall(force=False, interactive=False):
    # TODO docs
    # TODO unit test

    install_dir = get_config().install_dir
    repository_dir = get_config().repository_dir

    installed_paths = get_installed_paths(install_dir, repository_dir)

    if not force:
        LOG.error("Must use '-f' to force removal of dotfiles.")

    for file in installed_paths:
        unlink_path(file,
                    force,
                    interactive,
                    tuple([install_dir, repository_dir]),
                    )


def uninstall_main(cli):
    # TODO docs
    # TODO unit test
    uninstall(cli.force, cli.interactive)
