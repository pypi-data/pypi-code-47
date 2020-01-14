from __future__ import print_function
import getpass
import platform
import sys
import traceback
import signal

from passmanager.cli import parse_args
from passmanager.manager import create_profile
from passmanager.password import generate_password
from passmanager.clipboard import copy, get_system_copy_command

signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))


def main(args=sys.argv[1:]):
    args = parse_args(args)
    if args.clipboard and not get_system_copy_command():
        print(
            "ERROR To use the option -c (--copy) "
        )
        sys.exit(3)

    if args.prompt:
        args.site = getpass.getpass("Site: ")
        args.login = getpass.getpass("Login: ")
    if not args.site:
        print("ERROR : SITE is not given")
        sys.exit(4)

    if not args.master_password:
        args.master_password = getpass.getpass("Master Password: ")
    if not args.master_password:
        print("ERROR : MASTER_PASSWORD is required ")
        sys.exit(5)

    profile, master_password = create_profile(args)
    generated_password = generate_password(profile, master_password)

    if args.clipboard:
        try:
            copy(generated_password)
            print("Copied to clipboard")
        except Exception as e:
            print("@" * 80)
            print("Copy issue occured on %s" % platform.system())
            print("Can you send us an email at sayanmondal2098@gmail.com\n")
            traceback.print_exc()
            print("_" * 80)
    else:
        print(generated_password)


if __name__ == "__main__":
    main()