#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keepfresh.observer import Observer
from keepfresh.restart_handler import RestartHandler
from argparse import ArgumentParser
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = ArgumentParser()
    parser.add_argument('-d', type=str, help='Directory (if not specified, defaults to current directory)', default='.')
    parser.add_argument('-e', type=str, nargs='+', help='Excluded directories')
    parser.add_argument('-x', type=str, nargs='+', help='File extensions to watch (if not specified, all are watched)')

    subparsers = parser.add_subparsers(title='actions')

    logging_parser = subparsers.add_parser('log', help='Run the logging monitor', parents=[parser], add_help=False)
    logging_parser.add_argument('-i', type=int, help='Interval', required=True)
    logging_parser.set_defaults(action='log')

    command_parser = subparsers.add_parser('auto-restart', help='Run the command auto-restarter', parents=[parser], add_help=False)
    command_parser.add_argument('-c', type=str, nargs='+', help='Command', required=True)
    command_parser.set_defaults(action='auto-restart')

    args = parser.parse_args()

    observer = Observer(
        base_dir=args.d,
        excluded_dirs=args.e if args.e else [],
        file_extensions=args.x if args.x else []
    )

    if args.action == 'log':
        try:
            observer.log(interval=args.i)
        except KeyboardInterrupt:
            sys.exit(0)

    elif args.action == 'auto-restart':
        handler = RestartHandler(
            observer=observer,
            command=args.c
        )
        try:
            handler.run()
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        parser.error("No action selected")

if __name__=='__main__':
    main()
