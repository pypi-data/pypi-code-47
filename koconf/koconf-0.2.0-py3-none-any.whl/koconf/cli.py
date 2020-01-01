import click

from koconf.db import DataBaseManager
from koconf.task import BashManager, CronManager

entry_command = 'koconf'
settings = {
    'max_content_width': 180,
    'help_option_names': ['--help', '-h'],
}


@click.group(help='Korea IT conference manager with terminal.')
def main():
    pass


@main.command('show', context_settings=settings, help='Show searched conference list.')
@click.option('--id', '-i', help='Show conference list with id.')
@click.option('--title', '-t', help='Show conference list with title.')
@click.option('--city', '-c', help='Show conference list with city.')
@click.option('--tag', '-g', help='Show conference list with tag.')
@click.option('--apply', '-a', multiple=True, help='Show conference list with apply date.\ne.g) koconf show --apply ">=YYYY-MM-DD HH:MM" [-a "..."]')
@click.option('--applicable', is_flag=True, help='Show all applicable conference list.')
@click.option('--event', '-e', multiple=True, help='Show conference list with event date.\ne.g) koconf show --event ">=YYYY-MM-DD HH:MM" [-e "..."]')
@click.pass_context
def _show(ctx, *args, **kwargs):
    try:
        with DataBaseManager() as db:
            if kwargs['id']:
                result = db.show_by_id(kwargs['id'])
            elif kwargs['title']:
                result = db.show_by_title(kwargs['title'])
            elif kwargs['city']:
                result = db.show_by_city(kwargs['city'])
            elif kwargs['tag']:
                result = db.show_by_tag(kwargs['tag'])
            elif kwargs['apply']:
                result = db.show_by_applies(kwargs['apply'])
            elif kwargs['applicable']:
                result = db.show_by_applicable()
            elif kwargs['event']:
                result = db.show_by_events(kwargs['event'])
            else:
                result = db.show()

            click.echo(result)

    except Exception as e:
        click.echo(str(e))


@main.command('refresh', context_settings=settings, help='Refresh conference list to latest.')
@click.option('--with-clean', '-c', is_flag=True, help='Refresh conference list to latest.\nThis option will remove all saved information.')
@click.option('--only-expired', '-e', is_flag=True, help='Refresh conference list which is only expired.')
@click.option('--set-auto', '-s', is_flag=True, help='Set refresh event when reboot computer.')
@click.option('--unset-auto', '-u', is_flag=True, help='Unset refresh event when reboot computer.')
@click.pass_context
def _refresh(ctx, *args, **kwargs):
    try:
        if not kwargs['set_auto'] and not kwargs['unset_auto']:
            with DataBaseManager() as db:
                if kwargs['with_clean']:
                    click.echo('Remove old data ... ', nl=False)
                    db.clean()
                    click.echo('Success')

                if not kwargs['only_expired']:
                    click.echo('Fetch remote data ... ', nl=False)
                    db.refresh()
                    click.echo('Success')

                click.echo('Remove expired data ... ', nl=False)
                db.expire()
                click.echo('Success')
        else:
            with CronManager() as cron:
                command = '%s %s' % (entry_command, ctx.command.name)

                if kwargs['set_auto']:
                    cron.set_reboot_task(command=command)
                    click.echo('refresh when computer reboot [ON]')
                elif kwargs['unset_auto']:
                    cron.unset_reboot_task(command=command)
                    click.echo('refresh when computer reboot [OFF]')

    except Exception as e:
        click.echo(str(e))


@main.command('remind', context_settings=settings, help='Remind stored conference events.')
@click.option('--add', '-a', help='Add event to remind with id.\n e.g) koconf remind --add NHNFWD')
@click.option('--remove', '-r', help='Remove event to remind with id.\n e.g) koconf remind --remove NHNFWD')
@click.option('--set-background', '-s', is_flag=True, help='Set remind event when open new terminal.')
@click.option('--unset-background', '-u', is_flag=True, help='Unset remind event when open new terminal.')
@click.pass_context
def _remind(ctx, *args, **kwargs):
    try:
        if not kwargs['set_background'] and not kwargs['unset_background']:
            with DataBaseManager() as db:
                if kwargs['add']:
                    db.add_remind(kwargs['add'])
                    click.echo('[%s] is add to remind list !' % kwargs['add'])
                elif kwargs['remove']:
                    db.remove_remind(kwargs['remove'])
                    click.echo('[%s] is remove from remind list !' % kwargs['remove'])
                else:
                    click.echo(db.remind())
        else:
            with BashManager() as bash:
                command = '%s %s' % (entry_command, ctx.command.name)

                if kwargs['set_background']:
                    bash.set_terminal_task(command=command)
                    click.echo('remind when terminal open [ON]')
                elif kwargs['unset_background']:
                    bash.unset_terminal_task(command=command)
                    click.echo('remind when terminal open [OFF]')

    except Exception as e:
        click.echo(str(e))
