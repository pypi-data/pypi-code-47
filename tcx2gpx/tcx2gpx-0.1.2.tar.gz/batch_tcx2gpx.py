"""
Batch convert tcx to gpx files.
"""
import logging
from pathlib import Path
import argparse as arg
from multiprocessing import Pool

from tcx2gpx.tcx2gpx import TCX2GPX

# pylint: disable=logging-format-interpolation

LOGGER = logging.getLogger('batch tcx2gpx')


def create_parser():
    """
    Parse arguments for smooth scoring
    """

    parser = arg.ArgumentParser()
    parser.add_argument('-d', '--directory',
                        default='.',
                        help='Directory containing tcx files for conversion',
                        required=False)
    parser.add_argument('-j', '--cores',
                        default='4',
                        help='Number of processors to use.',
                        required=False)
    return parser.parse_args()


def process_tcx(file_path):
    """
    Wrapper to convert individual tcx files to gpx.
    """
    to_convert = TCX2GPX(file_path)
    to_convert.convert()


if __name__ == '__main__':

    PARSER = create_parser()
    TCX_DIR = Path(PARSER.directory)
    LOGGER.info('Searching for files in          : {}'.format(TCX_DIR))
    TCX_FILES = sorted(TCX_DIR.glob('*.tcx'))

    LOGGER.info('Found {} files, processing...'.format(len(TCX_FILES)))
    POOL = Pool(int(PARSER.cores))
    POOL.map(process_tcx, TCX_FILES)
