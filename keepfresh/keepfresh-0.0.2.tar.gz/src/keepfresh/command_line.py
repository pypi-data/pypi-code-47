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
    parser.add_argument('-i', type=int, help='Interval')
    parser.add_argument('-d', type=str, help='Directory')
    parser.add_argument('-e', type=str, nargs='+', help='Excluded directories')
    parser.add_argument('-a', action='store_true', help="Auto restart")
    parser.add_argument('-c', type=str, nargs='+', help='Command')
    parser.add_argument('-l', action='store_true', help='Run the logging monitor')
    args = parser.parse_args()

    if not args.d:
        logger.error("-d option to specify directory is required")
        sys.exit(1)

    if not args.i:
        logger.error("-i option to specify polling interval in seconds is required")
        sys.exit(1)

    observer = Observer(
        base_dir=args.d,
        excluded_dirs=args.e if args.e else []
    )

    if args.l:
        try:
            observer.log(interval=args.i)
        except KeyboardInterrupt:
            sys.exit(0)

    if args.a and args.c:
        handler = RestartHandler(
            observer=observer,
            interval=args.i,
            command=args.c
        )
        try:
            handler.run()
        except KeyboardInterrupt:
            sys.exit(0)

    logger.warning("Either -l or (-a and -c with a command) needs to be specified")

if __name__=='__main__':
    main()
