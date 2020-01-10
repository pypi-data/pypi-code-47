from tritise import Tritise
import fileinput
import click
from dateutil.parser import parse as parse_date

@click.group()
def cli():
    pass

@cli.command()
@click.argument('input_files', required = False, nargs = -1, default = None)
@click.option('--database', '-d', default = 'tritise.sqlite')
@click.option('--tag', '-t', default = None)
def read(input_files, database = None, tag = None):
    """Reads data from stdin or a file into the database"""
    t = Tritise(filename=database)
    print('Reading data...')
    for line in fileinput.input(input_files):
        print('Adding line: %s' % line)
        t.add(line.split()[0], tag=tag)
    print('done')

@cli.command()
@click.option('--from', '-f', 'start_string', default = None)
@click.option('--to', '-t', 'end_string', default = None)
@click.option('--database', '-d', default = 'tritise.sqlite')
@click.option('--tag', '-t', default = None)
def dump(start_string, end_string, database = None, tag = None):
    """Dumps a timeseries from a tritise database"""
    start_stamp = parse_date(start_string) if start_string else None
    end_stamp = parse_date(end_string) if end_string else None
    t = Tritise(filename=database)
    print('Dumping tag: %s' % (tag if tag else 'default'))
    entries = t.range(start_stamp, end_stamp, tag)
    for entry in entries:
        print(entry)

@cli.command()
@click.argument('value')
@click.option('--database', '-d', default = 'tritise.sqlite')
@click.option('--tag', '-t', default = None)
def add(value, database = None, tag = None):
    """Add a value with the current timestamp"""
    t = Tritise(filename=database)
    print('Adding value %s with tag: %s' % (value ,tag if tag else 'default'))
    print(t.add(value, tag))

if __name__ == '__main__':
    cli()