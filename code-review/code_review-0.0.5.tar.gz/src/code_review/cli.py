"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcode_review` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``code_review.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``code_review.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import os

from code_review.notifications import NotificationViewer

parser = argparse.ArgumentParser(description='Command description.', epilog='made by sage smith')
parser.add_argument('-o', '--open', action='store_true', help="Opens new code review updates in default browser")
parser.add_argument('-s', '--stdout', action='store_true', help='Prints code review updates')
parser.add_argument('-t', '--token', type=str, help='Token to use when checking for updates')


def main(args=None):
    args = parser.parse_args(args=args)
    token = os.getenv("GIT_TOKEN")
    if args.token:
        if os.getenv(args.token):
            token = os.getenv(args.token)
        else:
            token = args.token
    if token:
        cr = NotificationViewer(token)
        if args.open:
            cr.open()
            return
        if args.stdout:
            cr.stdout()
            return
    print("Please supply a git token by either making an env var called GIT_TOKEN, "
          "or passing in a token or env var name with the -t option")
    parser.print_help()
