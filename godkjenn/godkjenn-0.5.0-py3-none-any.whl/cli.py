import logging
import sys
from pathlib import Path

import click
from exit_codes import ExitCode

from godkjenn.artifact import Artifact
import godkjenn.config
import godkjenn.environment
from godkjenn.version import __version__

log = logging.getLogger(__name__)


@click.group()
@click.option('--config', help='Config file to load', type=Path)
@click.option('--root-dir', help='Root directory', type=Path)
@click.option('--verbosity',
              default='WARNING',
              help="The logging level to use.",
              type=click.Choice([name
                                 for lvl, name in sorted(logging._levelToName.items())
                                 if lvl > 0],
                                case_sensitive=True))
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, config, root_dir, verbosity):
    """Command-line interface for godkjenn.
    """
    logging_level = getattr(logging, verbosity)
    logging.basicConfig(level=logging_level)

    env = godkjenn.environment.Environment()

    if config is not None:
        config = godkjenn.config.load_config(config)
    else:
        config = env.default_config(root_dir)

    env.activate(config)

    ctx.obj = env


@cli.command()
@click.argument('test_id')
@click.pass_obj
def accept(env, test_id):
    """Accept the current received data for a test.
    """
    vault = env.get_vault()

    try:
        vault.accept(test_id)
    except KeyError:
        log.error('No received data for {}'.format(test_id))
        return ExitCode.DATA_ERR

    return ExitCode.OK


@cli.command()
@click.pass_obj
def accept_all(env):
    """Accept all received data for a configuration/root directory.
    """
    vault = env.get_vault()

    for test_id in vault.ids():
        try:
            vault.accept(test_id)
        except KeyError:
            # This just means there isn't any received data for the ID, just accepted.
            pass

    return ExitCode.OK


@cli.command()
@click.argument('test_id')
@click.argument('destination', type=click.File(mode='wb'))
@click.pass_obj
def accepted(env, test_id, destination):
    """Get accepted data for a test.
    """
    vault = env.get_vault()

    try:
        artifact = vault.accepted(test_id)
    except KeyError:
        print(f'No accepted data for id {test_id}', file=sys.stderr)
        return ExitCode.DATA_ERR

    destination.write(artifact.data)

    return ExitCode.OK


@cli.command()
@click.argument('test_id')
@click.argument('data_source', type=click.File(mode='rb'))
@click.pass_obj
def receive(env, test_id, data_source):
    """Receive new data for a test.
    """
    vault = env.get_vault()

    data = data_source.read()
    vault.receive(test_id, Artifact(data=data, config={}))

    return ExitCode.OK


@cli.command()
@click.argument('test_id')
@click.argument('destination', type=click.File(mode='wb'))
@click.pass_obj
def received(env, test_id, destination):
    """Get received data for a test.
    """
    vault = env.get_vault()

    try:
        artifact = vault.received(test_id)
    except KeyError:
        print(f'No received data for {test_id}', file=sys.stderr)
        return ExitCode.DATA_ERR

    destination.write(artifact.data)

    return ExitCode.OK


@cli.command()
@click.argument('test_id')
@click.pass_obj
def diff(env, test_id):
    """Get received data for a test.
    """
    vault = env.get_vault()
    try:
        received = vault.received(test_id)
        accepted = vault.accepted(test_id)
    except KeyError:
        print(f'Do not have both received and accepted data. No diff possible.', file=sys.stderr)
        return ExitCode.DATA_ERR

    # TODO: Merge accepted config in
    differ = env.get_differ()

    diff = differ(accepted, received)
    print(diff)

    return ExitCode.OK


@cli.command()
@click.pass_obj
def default_config(env):
    """Print a default config to stdout.
    """
    print(godkjenn.config.serialize_config(
        env.default_config(env.config.root_path)))


@cli.command()
@click.pass_obj
def status(env):
    """Print status of godkjenn vault
    """
    vault = env.get_vault()
    for test_id in vault.ids():
        try:
            accepted = vault.accepted(test_id)
        except KeyError:
            accepted = None

        try:
            received = vault.received(test_id)
        except KeyError:
            received = None

        if accepted is None:
            if received is None:
                assert False, 'Test ID with no information: {}'.format(test_id)
            else:
                message = 'initialized'
        else:
            if received is None:
                message = 'up-to-date'
            elif accepted == received:
                message = 'status-quo'
            else:
                message = 'mismatch'

        print(test_id, message)


def main(argv=None, standalone_mode=True):
    return cli(argv, standalone_mode=standalone_mode)


if __name__ == '__main__':
    sys.exit(main())
