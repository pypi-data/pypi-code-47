#!/usr/bin/env python

from __future__ import print_function
import sys
import locale

from tail_loader import TailLoader
from censor import Censor
from maileater import MailLogEater

LOGPATH = "/var/log/maillog"

# Reset locale for parsing timestamp in logs
locale.setlocale(locale.LC_ALL, "C")


def main():
    if len(sys.argv) < 2:
        usage(sys.argv[0])
        sys.exit(1)
    duration = int(sys.argv[1])
    logpath = LOGPATH
    if len(sys.argv) >= 3:
        logpath = sys.argv[2]
    loader = TailLoader(logpath, duration)
    censor = Censor()
    eater = MailLogEater()
    for rawline in loader.readlines():
        line = censor.censor(rawline)
        eater.eat(line)
    print(eater)


def usage(name):
    print("Usage: %s SECOND [LOGPATH]" % name)


if __name__ == "__main__":
    main()
