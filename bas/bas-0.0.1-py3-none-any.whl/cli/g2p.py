import click
from bas.services import g2p as service

@click.command()
@click.argument('text')
@click.option('--language', default='eng-US', show_default=True, type=click.Choice(service.LANGUAGE))
@click.option('--outformat', default='bpf', show_default=True, type=click.Choice(service.OUTFORMAT))
def g2p(text, language, outformat):
    output = service.g2p(open(text, 'r').read(), language, outformat)
    print(output)