"""PR Man!

Usage:
  prman config get <key>
  prman config set <key> <value>
  prman [-m <message>|--message <message>]
  prman (-h | --help)
  prman --version
"""
from docopt import docopt


def read_args(version):
  return docopt(__doc__, version=version)
