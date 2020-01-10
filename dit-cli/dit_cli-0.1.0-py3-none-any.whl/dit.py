"""The CLI for dit"""


import click


from dit_cli import addition


@click.group()
def cli():
    pass


@click.command()
@click.argument('num1')
@click.argument('num2')
def add(num1, num2):
    click.echo('Result: {}'.format(addition.add(num1, num2)))


@click.command()
@click.argument('num1')
@click.argument('num2')
def multiply(num1, num2):
    click.echo('Result: {}'.format(addition.multiply(num1, num2)))


cli.add_command(add)
cli.add_command(multiply)

if __name__ == '__main__':
    cli()
