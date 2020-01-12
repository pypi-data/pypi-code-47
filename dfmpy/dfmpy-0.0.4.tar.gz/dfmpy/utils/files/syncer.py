# TODO docs

from logging import getLogger

from dfmpy.utils.files import mkdir_parents
from dfmpy.utils.files import path_is_file
from dfmpy.utils.files import path_is_symlink
from dfmpy.utils.files.deleter import unlink_path
from dfmpy.utils.interactive import ask_to

# TODO docs
LOG = getLogger()


def link_path(symlink_path, target_path, force, interactive):
    # TODO docs
    # TODO unit test
    if ask_to(f'Overwrite to link file: {symlink_path}', force, interactive):
        mkdir_parents(symlink_path)
        symlink_path.symlink_to(target_path)
        LOG.warning('Symlinked: %s -> %s', symlink_path, target_path)
    else:
        LOG.info('Simulated symlink: %s -> %s', symlink_path, target_path)


def sync_expected_paths(expected_paths, force, interactive):
    # TODO docs
    # TODO unit test
    LOG.info('Syncing files.')
    force_it_kwargs = {'force': True, 'interactive': False}
    for symlink_path, target_path in expected_paths.items():

        if path_is_symlink(symlink_path):
            if symlink_path.resolve() == target_path:
                # The symlink exists and points to the correct target.
                LOG.debug('No need to sync: %s -> %s',
                          symlink_path,
                          target_path)
            else:
                # If the symlink exists, but it points to the wrong target!
                sync_prompt = f'Sync broken link: {symlink_path}'
                if ask_to(sync_prompt, force, interactive):
                    unlink_path(symlink_path, **force_it_kwargs)
                    link_path(symlink_path, target_path, **force_it_kwargs)

        elif path_is_file(symlink_path):
            sync_prompt = f'Replace existing file: {symlink_path}'
            if ask_to(sync_prompt, force, interactive):
                unlink_path(symlink_path, **force_it_kwargs)
                link_path(symlink_path, target_path, **force_it_kwargs)

        else:
            # The file/link does not exist, so create it.
            link_path(symlink_path, target_path, force, interactive)
