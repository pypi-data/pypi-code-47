import click
from bas.services import maus as service

@click.command()
@click.argument('signal')
@click.argument('bpf')
@click.option('--language', default='eng-US', show_default=True, type=click.Choice(service.LANGUAGE))
@click.option('--modus', default='align', show_default=True, type=click.Choice(service.MODUSES))
@click.option('--outformat', default='par', show_default=True, type=click.Choice(service.OUTFORMAT))
def maus(signal, bpf, language, modus, outformat):
    output = service.maus(open(signal, 'r+b').read(), open(bpf, 'r').read(), language, modus, outformat)
    print(output)