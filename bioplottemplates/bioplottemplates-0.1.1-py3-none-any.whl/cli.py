import sys

from bioplottemplates import log
from bioplottemplates import cli_labeldots
from bioplottemplates import cli_param
from bioplottemplates.libs import libcli


def load_args():
    ap = libcli.CustomParser()

    subparsers = ap.add_subparsers(title='Plotting routines')

    ap_param = subparsers.add_parser(
        'param',
        help='Plots a parameter.',
        parents=[cli_param.ap],
        add_help=False,
        )
    ap_param.set_defaults(func=cli_param.main)

    ap_labeldots = subparsers.add_parser(
        'label_dots',
        help='Plots multiple series with labeled X axis.',
        parents=[cli_labeldots.ap],
        add_help=False,
        )
    ap_labeldots.set_defaults(func=cli_labeldots.main)
    
    if len(sys.argv) < 2:
        ap.print_help()
        ap.exit()
    
    cmd = ap.parse_args()
    return cmd


def maincli():
    args = load_args()
    log.debug(args)
    args.func(**vars(args))


if __name__ == '__main__':
    maincli()
