import click
from .command import hello, define, cmd


@click.group(name='cmd')
def group() -> click.Command:
    pass


group.add_command(hello)
group.add_command(define)
group.add_command(cmd)
