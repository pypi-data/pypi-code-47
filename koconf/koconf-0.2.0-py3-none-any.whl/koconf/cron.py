import click

from crontab import CronTab
from koconf.db import DataBaseManager

settings = {
    'max_content_width': 100,
}


@click.group(help='Korea IT conference manager with terminal.')
def main():
    pass


@main.command('show', context_settings=settings, help='Show searched conference list.')
@click.option('--id', '-i', help='Show conference list with id.')
@click.option('--title', '-t', help='Show conference list with title.')
@click.option('--city', '-c', help='Show conference list with city.')
@click.option('--tag', '-g', help='Show conference list with tag.')
@click.option('--apply', '-a', is_flag=True, help='Show applicable conference list.')
@click.option('--date', '-d', help='Show conference list with date.\n e.g) koconf show --date ">=YYYY-MM-DD HH-MM"')
@click.pass_context
def _show(ctx, *args, **kwargs):
    pass


@main.command('refresh', context_settings=settings, help='Refresh conference list to latest.')
@click.option('--set-auto', '-s', is_flag=True, help='Set refresh event when reboot computer.')
@click.option('--unset-auto', '-u', is_flag=True, help='Unset refresh event when reboot computer.')
@click.pass_context
def _refresh(ctx, *args, **kwargs):

    print(ctx.command.name)

    if kwargs['set_auto']:
        cron = CronTab(user=True)

        job = cron.new(command='koconf refresh')
        job.every_reboot()  

        cron.write()

    pass


@main.command('remind', context_settings=settings, help='Remind stored conference events.')
@click.option('--add', '-a', help='Add event to remind with id.\n e.g) koconf remind --add NHNFWD')
@click.option('--remove', '-r', help='Remove event to remind with id.\n e.g) koconf remind --remove NHNFWD')
@click.option('--set-background', '-s', is_flag=True, help='Set remind event when open new terminal.')
@click.option('--unset-background', '-u', is_flag=True, help='Unset remind event when open new terminal.')
@click.pass_context
def _remind(ctx, *args, **kwargs):
    pass
