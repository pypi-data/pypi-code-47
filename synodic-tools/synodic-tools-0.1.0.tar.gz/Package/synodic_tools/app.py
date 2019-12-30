import click
import pkg_resources


@click.group()
def entrypoint() -> None:
    pass


# Attach commands
# entrypoint.add_command(VersionGroup)
# entrypoint.add_command(ReleaseGroup)

for subcommand in pkg_resources.iter_entry_points('command_groups'):
    entrypoint.add_command(subcommand.load())
