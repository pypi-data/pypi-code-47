'''Scrip for source indexing McAfee builds
Author: Uri Mann
email: Uri_Mann@mcafee.com
@IMPORTANT: Requires Python version 3.6 or above
'''
# Python modules
import os
import sys
import enum
import argparse
# Source index modules
from . import indexer


def main(argv=sys.argv[1:]):
    class ArgumentParser(argparse.ArgumentParser):
        '''Configuration file loader
        '''
        def convert_arg_line_to_args(self, arg_line):
            return arg_line.split()

    class Action(enum.IntEnum):
        INDEX = 1
        REINDEX = 2

        # magic methods for argparse compatibility

        def __str__(self):
            return self.name.lower()

        def __repr__(self):
            return str(self)

        @staticmethod
        def argparse(s):
            try:
                return Action[s.upper()]
            except KeyError:
                return s

    parser = ArgumentParser(fromfile_prefix_chars='@')
    # Configuration file with command line parameters
    # @NOTE: Any command line switch can be added to override the configuration
    #        if it appears later on the command line
    parser.add_argument('-p', '--pdb',        help='Path to .PDB file')
    parser.add_argument('-b', '--build-base', help='Build directory path',   default=os.getcwd())
    parser.add_argument('-P', '--pdbs',       help='Paths to .PDB directories (relative to --build-base)', nargs='*')
    parser.add_argument('-o', '--output',     help='Output file',            default=sys.stdout, type=argparse.FileType('w'))
    parser.add_argument('-g', '--github',     help='GitHub URL',             default='github.com')
    parser.add_argument('-r', '--repo',       help='Git repository branch')
    parser.add_argument('-s', '--srcsrv',     help='SRCSRV tools directory', default=r'C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\srcsrv')
    parser.add_argument('-a', '--action',     help='Action type',            default=Action.INDEX, type=Action.argparse, choices=list(Action))
    parser.add_argument('-x', '--hexsha',     help='Git repository branch hash')
    parser.add_argument('-X', '--extensions',help='Semicolon separated list of source extensions (default:cpp;c;h)', default='cpp;c;h')
    # Diagnosis options
    parser.add_argument('-k', '--keep',       help='Keep temporary artifacts', action='store_true')
    parser.add_argument('-n', '--no-process', help='Donnot change .PDB files', action='store_true')
    parser.add_argument('-l', '--log',        help='Path to log file',       default=None)

    args = parser.parse_args(args=argv)
    if not os.path.isdir(args.srcsrv):
        raise FileNotFoundError(f'directory {args.srcsrv} does not exist')

    indexer.Indexer(args).process()


if __name__ == '__main__':
    main()


