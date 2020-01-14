import argparse
import os
import passmanager.clipboard

def range_type(value_string):
    value = int(value_string)
    if value not in range(5, 35+1):
        raise argparse.ArgumentTypeError("%s is out of range, choose in [5-35]" % value)
    return value


def parse_args(args):
    parser = argparse.ArgumentParser(
        usage="passmanager SITE [LOGIN] [MASTER_PASSWORD] [OPTIONS]",
        description='passmanager is an independent Open Source, Password Manager python library which implements a cli tools to create password for site and store it'
        # epilog=EXAMPLES + COPYRIGHT,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-v", "--version", action="version", version='0.0.1'
    )
    parser.add_argument(
        "site", nargs="?", help="site used in the password generation (required)"
    )
    parser.add_argument(
        "login", nargs="?", help="login used in the password generation. Default to ''."
    )
    parser.add_argument(
        "master_password",
        default=os.environ.get("passmanager_MASTER_PASSWORD", None),
        nargs="?",
        help="master password used in password generation.",
    )
    parser.add_argument(
        "-L",
        "--length",
        default=10,
        choices=range(5, 35+1),
        type=range_type,
        help="password length (default: 10, min: 5, max: 35)",
        metavar='[5-35]'
    )
    parser.add_argument(
        "-C", "--counter", default=1, type=int, help="password counter (default: 1)"
    )
    parser.add_argument(
        "-p",
        "--prompt",
        dest="prompt",
        action="store_true",
        help="prompt for values interactively",
    )
    parser.add_argument(
        "-c",
        "--copy",
        dest="clipboard",
        action="store_true",
        help="copy the password to clipboard",
    )

    lowercase_group = parser.add_mutually_exclusive_group()
    lowercase_group.add_argument(
        "-l",
        "--lowercase",
        help="add lowercase in password",
        dest="l",
        action="store_true",
    )
    lowercase_group.add_argument(
        "--no-lowercase",
        help="remove lowercase from password",
        dest="nl",
        action="store_true",
    )

    uppercase_group = parser.add_mutually_exclusive_group()
    uppercase_group.add_argument(
        "-u",
        "--uppercase",
        dest="u",
        help="add uppercase in password",
        action="store_true",
    )
    uppercase_group.add_argument(
        "--no-uppercase",
        dest="nu",
        help="remove uppercase from password",
        action="store_true",
    )

    digits_group = parser.add_mutually_exclusive_group()
    digits_group.add_argument(
        "-d", "--digits", dest="d", help="add digits in password", action="store_true"
    )
    digits_group.add_argument(
        "--no-digits",
        dest="nd",
        help="remove digits from password",
        action="store_true",
    )

    symbols_group = parser.add_mutually_exclusive_group()
    symbols_group.add_argument(
        "-s", "--symbols", dest="s", help="add symbols in password", action="store_true"
    )
    symbols_group.add_argument(
        "--no-symbols",
        dest="ns",
        help="remove symbols from password",
        action="store_true",
    )
    return parser.parse_args(args)