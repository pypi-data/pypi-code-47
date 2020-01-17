import click

from boiler import cli
from boiler.definitions import all_activity_codes


@click.group(name='activity', short_help='utils')
@click.pass_obj
def activity(ctx):
    pass


@activity.command(name='list-types', help='list known activities')
def list_activities():
    for activity_type in all_activity_codes.values():
        click.echo(activity_type.value)


cli.add_command(activity)
