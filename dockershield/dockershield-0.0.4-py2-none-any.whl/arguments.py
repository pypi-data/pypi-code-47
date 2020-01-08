"""
    This module contains command line argument and configuration file parsing.
    FIXME: The name arguments.py might be confusing since it also has configuration file?
"""

from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter

import os
import sys

# PyYAML
from yaml import load, dump

# As recommended, try to use the C YAML parser if it exists
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

CONFIGURATION_FILE = os.path.realpath(os.path.join(os.path.dirname(__file__), "config", "dockershield.yml"))

from .systemd.systemd import SYSTEMD_POSTINSTALL_FILE, SYSTEMD_PREINSTALL_FILE

global config

def get_config(config_file=CONFIGURATION_FILE):
    with open(config_file, "r") as f:
        config = load(f, Loader=Loader)
    return config

def dump_config(config_object=None):
    global config
    if config_object is None:
        config_object = config
    output = dump(config_object, Dumper=Dumper)
    return output


def get_argparser(argv, parents=None, conflict_handler="resolve"):
    """
    Returns argparse compatible parser
    NOTE: This tool should always run successfully with no arguments.
            Default values are parsed from the CONFIGURATION_FILE

        Inputs:
            argv: Currently ignored. Might be used to patch argparse functionality.
            parents: Parent argparse Parsers. Use at own risk.
            conflict_handler: How to resolve conflicts with parent parsers. Use at own risk.
        Outputs:
            argparse.ArgumentParser instance
    """
    if parents is None:
        parents = []

    parser = ArgumentParser(
        description="Wraps the docker unix socket with some filtering to deny non-whitelisted commands"
        ". You may find it more convenient to edit the values in %s" % (CONFIGURATION_FILE,),
        parents=parents,
        conflict_handler=conflict_handler,
        # Use this class to show the default values. By default argparse does not show default.
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    # Self documenting arguments?
    global config
    config = get_config()

    parser.add_argument(
        "--blacklist",
        type=str,
        help="URL regexes to blacklist",
        nargs="*",
        default=config.get("filters", {}).get("url", {}).get("blacklist", [])
    )
    parser.add_argument(
        "--whitelist",
        type=str,
        help="URL regexes to whitelist. NOTE: Only whitelists if the blacklist did not match.",
        nargs="*",
        default=config.get("filters", {}).get("url", {}).get("whitelist", [])
    )


    parser.add_argument(
        "--docker-socket-path",
        type=str,
        help="Path to the docker unix socket.",
        default=os.path.realpath(config.get("docker_socket_path","/var/run/docker.sock"))
    )

    parser.add_argument(
        "--filtered-socket-path",
        type=str,
        help="Path to the sanitised socket, which clients can connect to.",
        default=os.path.realpath(config.get("filtered_socket_path", "dockershield.sock"))
    )

    parser.add_argument(
        "--blacklist-method",
        type=str,
        help="Methods to blacklist",
        nargs="*",
        default=config.get("filters", {}).get("method", {}).get("blacklist", [])
    )
    parser.add_argument(
        "--whitelist-method",
        type=str,
        help="Methods to whitelist. NOTE: Only whitelists if the blacklist did not match.",
        nargs="*",
        default=config.get("filters", {}).get("method", {}).get("whitelist", [])
    )

    parser.add_argument(
        "--filter-includes-version",
        action="store_true",
        help="Does the URL filtering include the API version string?",
        default=config.get("filters", {}).get("url", {}).get("include_version")
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Verifies that the script could run, but stops immediately."
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Prints all levels of logging messages to stdout.",
        default=config.get("verbose", False)
    )
    parser.add_argument(
        "--silent",
        action="store_true",
        help="Hide all logging messages, including warnings and errors. Incompatible with --verbose",
        default=config.get("silent", False)
    )

    parser.add_argument(
        "--watch_config",
        action="store_true",
        help="If set, will periodically poll the config file at %s for changes and restart on a change.",
        default=config.get("watch_config", False)
    )

    parser.add_argument(
        "--systemd-install",
        action="store_true",
        help="Installs this tool as a systemd service. The unit file is copied from %s to %s."
            % (SYSTEMD_PREINSTALL_FILE, SYSTEMD_POSTINSTALL_FILE)
    )
    parser.add_argument(
        "--systemd-uninstall",
        action="store_true",
        help="DANGER: Removes any installed systemd service at %s." % (SYSTEMD_POSTINSTALL_FILE,)
    )

    parser.add_argument(
        "--edit-config",
        action="store_true",
        help="Edit the YAML config file at %s in your favourate text editor." % (CONFIGURATION_FILE,)
    )

    return parser


def parse_argv(argv):
    """
    Parses command line arguments in argv
    NOTE: argv is assumed to include a excecutable name, so argv[0] is ignored
    """
    parser = get_argparser(argv)
    # argparse parsers ignore argv[0]
    return parser.parse_args(argv[1:])

config = get_config()
