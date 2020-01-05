import os
import sys
from subprocess import Popen


def main(as_module=False):
    print('sys.argv', sys.argv)
    Popen('python3 serve.py')


if __name__ == "__main__":
    main(as_module=True)