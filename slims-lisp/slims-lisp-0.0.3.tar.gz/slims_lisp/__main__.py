import click
from slims_lisp.slims import Slims

@click.group()
def cli():
    pass

@cli.command(help="Download a file from a slims experiment attachment step.")
@click.option('--url',
              default="https://slims-lisp.epfl.ch/rest/rest",
              help='Slims REST URL.',
              required=True,
              show_default=True)
@click.option('--proj',
              help='Project name (if any).',
              required=False)
@click.option('-e',
              '--exp',
              help='Experiment name.',
              required=True)
@click.option('-s',
              '--step',
              default='data_collection',
              help='Experiment step name. Default: data_collection',
              required=True,
              show_default=True)
@click.option('-a', '--attm',
              help='Attachment name.',
              required=True)
@click.option('-o', '--output',
              help='Output file name. [default: same as --attm]',
              required=False)
@click.option('-u', '--username',
              prompt="User",
              help='User name (prompted).',
              required=True)
@click.option('-p', '--pwd',
              prompt="Password",
              hide_input=True,
              help='Password (prompted).',
              required=True)
def get(url, username, pwd, proj, exp, step, attm, output):
    slims = Slims(url = url, username = username, pwd = pwd)
    slims.get_attachment(proj = proj, exp = exp, step = step, attm = attm,
                         output = output)

if __name__ == '__main__':
    cli()
