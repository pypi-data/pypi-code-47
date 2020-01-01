#!/usr/bin/env python3
import sys


def main():
    print('error: this version of python has expired. shame on you!',
          file=sys.stderr)
    sys.exit(2)


if __name__ == '__main__':
    main()
