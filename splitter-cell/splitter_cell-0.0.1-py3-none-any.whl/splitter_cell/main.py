import click

@click.command()
@click.option('--folder', prompt='Which folder?', help='The person to greet.')
@click.option('--glob', prompt='What glob command do you plan on using?', help='The files youre trying to join')
def hello(folder, glob):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"We're going to use the folder here: {folder}")
    click.echo(f"Glob search will be ... {glob}")

if __name__ == '__main__':
    hello()