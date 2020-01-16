"""Console script for {{cookiecutter.project_name}}."""

{%- if 'y' in cookiecutter.command_line_interface|lower %}
import argparse


def main():
    """Console script for {{cookiecutter.project_name}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_name}}.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

{%- endif %}
