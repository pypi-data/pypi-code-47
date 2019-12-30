import argparse
from .process import ProcessInput


def main(options):
    package = options.package
    input_file = options.input_file
    output_file = options.output_file
    latest = options.latest
    greater = options.greater
    all_versions = options.all

    if not any([input_file, package]):
        raise Exception("Pass either package or requirements.txt file")

    ProcessInput(input_file, output_file, package, all_versions, latest, greater)


def run():
    """
    Parse the options to run with the debug mode, and the port number"
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r",
        "--requirements",
        nargs="?",
        help="Pass the requirements.txt file",
        dest="input_file",
    )

    parser.add_argument(
        "-p", "--package", nargs="?", help="Pass the package name", dest="package"
    )

    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        help="Pass the output file name",
        dest="output_file",
    )

    parser.add_argument(
        "-l",
        "--latest",
        nargs="?",
        help="Filter only the latest version. By default it is True.",
        dest="latest",
        default=True,
    )

    parser.add_argument(
        "-a",
        "--all",
        nargs="?",
        help="To get all version of the package. By default it is False.",
        dest="all",
        default=False,
    )

    parser.add_argument(
        "-g",
        "--greater",
        nargs="?",
        help="To get all versions greaterthan the given package version. \
              By default it is False.",
        dest="greater",
        default=False,
    )

    options = parser.parse_args()
    main(options)


if __name__ == "__main__":
    run()
