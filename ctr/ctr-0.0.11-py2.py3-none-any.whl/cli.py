"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mctr` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``ctr.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``ctr.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse

import ctr

parser = argparse.ArgumentParser(description='Concatenate headered files into output file (first file).')
parser.add_argument('outfile', type=str, help='Output file.')
parser.add_argument('infiles', nargs=argparse.REMAINDER,
                    help="Headered files to concat.")


def main(args=None):
    args = parser.parse_args(args=args)
    ctr.concat(args.infiles, args.outfile)
