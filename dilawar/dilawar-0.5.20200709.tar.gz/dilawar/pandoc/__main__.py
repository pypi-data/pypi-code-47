__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2019-, Dilawar Singh"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"

import sys
import dilawar.pandoc.utils as pu

def main():
    args = sys.argv[1:]
    if not args:
        args = [ '-h' ]
    pu.execute_pandoc(args)

if __name__ == '__main__':
    main()

