import argparse
from .main import testaton


def main(args=None):
    parser = argparse.ArgumentParser(description='Test file')

    parser.add_argument('configuration_file', action='store', type=str,
                        help='The JSON file defining the Dtest, Spark, and tests configurations')

    args = parser.parse_args()

    testaton(config_file=args.configuration_file)
