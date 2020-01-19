import os
import argparse
from time import sleep
from clifier import Clifier
version = '0.0.1'  # version of your packages


def main() -> None:
    config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cli.yaml")
    cli = Clifier(config_path, prog_version=version)
    parser = cli.create_parser()
    args = parser.parse_args()
    print(args)
    print(type(args))
    example_logic(args)


def example_logic(args: argparse.Namespace) -> None:
    if 'game' in args:
        times = args.count if 'count' in args else ''
        times_str = f' {times} times' if times else ''
        print(f'You want to play \'{args.game}\'{times_str}')
    if 'sleep' in args:
        print(f'Sleep for {args.sleep} sec')
        sleep(args["sleep"])


if __name__ == '__main__':
    main()
