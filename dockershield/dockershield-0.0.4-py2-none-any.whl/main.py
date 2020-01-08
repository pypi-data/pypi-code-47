"""
    main: Handles the command-line interface to the tool
"""

import socket
import sys
import os

from .interface import DockerShield
from .arguments import parse_argv

def main(argv):
    """
    Run with command line arguments
    NOTE: If not passing sys.argv, remember to include equivalent of sys.argv[0] even though we ignore it
    """
    while True:
        args = parse_argv(argv)
        with DockerShield(args) as shield:
            shield.run()
        if not shield.restart_requested:
            break
