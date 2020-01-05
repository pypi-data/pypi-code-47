import click
from bas.services import subtitle as service

@click.command()
@click.argument('transcription')
@click.argument('bpf')
@click.option('--maxlength', default=10, show_default=True)
@click.option('--marker', default='newline', show_default=True, type=click.Choice(service.MARKER))
@click.option('--outformat', default='srt', show_default=True, type=click.Choice(service.OUTFORMAT))
def subtitle(transcription, bpf, maxlength, marker, outformat):
    output = service.subtitle(open(transcription, 'r').read(), open(bpf, 'r').read(), maxlength, marker, outformat)
    print(output)