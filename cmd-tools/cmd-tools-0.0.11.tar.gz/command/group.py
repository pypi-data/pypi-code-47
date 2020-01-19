import click
from .command import hello, define, cmd, open_url


@click.group(name='cmd')
def group() -> click.Command:
    pass


group.add_command(hello)
group.add_command(define)
group.add_command(cmd)
group.add_command(open_url)
