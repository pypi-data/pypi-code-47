import argparse

from bioplottemplates.libs import libcli, libio
from bioplottemplates.plots import label_dots


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
    
    data, labels = libio.extract_labels_data(*data_csv)
    
    plotvars = plotvars or dict()
    plotvars.setdefault('series_labels', data_csv)
    print(plotvars['series_labels'])
    label_dots.plot(
        labels,
        data,
        **plotvars,
        )

    pass


if __name__ == '__main__':
    maincli()
