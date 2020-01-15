import argparse

import numpy as np

from bioplottemplates.libs import libcli, libio
from bioplottemplates.plots import param


ap = libcli.CustomParser(
    description=__doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

ap.add_argument(
    'data_csv',
    help='The CSVs files to plot',
    nargs='+',
    )


ap.add_argument(
    '-v',
    '--plotvars',
    help=(
        'Plot variables. '
        'Example: -v xlabel=frames ylabel=RMSD color=red.'
        ),
    nargs='*',
    action=libcli.ParamsToDict,
    )


def maincli():
    cmd = load_args()
    main(**vars(cmd))


def main(data_csv, plotvars, **kwargs):
    
    data_series = []
    for data in data_csv:
        data_series.append(np.loadtxt(data, delimiter=',', comments='#')[:,1])

    plotvars = plotvars or dict()
    print(plotvars)

    param.plot(
        list(range(len(data_series[0]))),
        data_series,
        **plotvars,
        )

    pass


if __name__ == '__main__':
    maincli()
