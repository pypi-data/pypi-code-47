"""
Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""
import sys
from .docparser import new_docopt

__version__ = '1.0.2'
version_msg = "Naval Fate {}".format(__version__)


if __name__ == '__main__':
    # As default, Docopt display the __doc__ if the option '--help' is asked
    arguments = new_docopt.docopt(__doc__, argv=sys.argv, version=version_msg)
    """if arguments['--version']:
        print(version_msg)"""
