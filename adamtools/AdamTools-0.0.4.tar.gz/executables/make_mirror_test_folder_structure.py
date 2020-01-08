"""
Created by adam on 6/1/18
"""
__author__ = 'adam'

import os, sys


def make_mirror_directories( inputpath, outputpath ):
    """Walks the input path directories and creates empty
    corresponding folders in output path.
    If the folder already exists, it prints a message and does nothing
    to the existing folder.

    If called from the commandline, inputpath should be the first argument
    and output path, the second.
    """

    # check that we have properly formated directories
    inputpath = inputpath if inputpath[-1:] == '/' else inputpath + '/'
    outputpath = outputpath if outputpath[-1:] == '/' else outputpath + '/'

    for dirpath, dirnames, filenames in os.walk( inputpath ):
        structure = os.path.join( outputpath, dirpath[ len( inputpath ): ] )
        if not os.path.isdir( structure ):
            os.mkdir( structure )
        else:
            print( "Folder %s already exits" % structure )


if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    make_mirror_directories( input_path, output_path )
