""" Entry point for changelogfromtags.

Generate a changelog from git tags.
"""

import argparse
import re
import shlex
import subprocess
from datetime import datetime


def get_cmd_output(cmd):
    """ Execute a command and returns the output.

    :param str cmd: Command to execute.
    :returns: Command stdout content.
    :raises: ValueError with stderr content if their is one.
    """
    args = shlex.split(cmd)
    process = subprocess.Popen(args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, strerr = process.communicate()
    if strerr:
        raise ValueError(strerr)
    return stdout.decode()


def print_changelog_entry(tag, timestamp, message, prefix=None):
    """ Print a format an changelog entry.

    :param str tag: "1.2.3"
    :param int timestamp: date time of tag
    :param int message: tag message
    :param str prefix: optional prefix to append at on each line if its not here
    """
    readable_tmp = datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y")
    header = f"{tag} ({readable_tmp})"
    print(header)
    print("-"*len(header))
    for line in message.split("\n"):
        entry = line.strip()
        # prepend prefix if not present
        if entry and prefix and not entry.startswith(prefix):
            entry = prefix + entry
        print(entry)


def main():
    """ Main. """
    parser = argparse.ArgumentParser(
        description='Generate a change log from git tags.'
    )
    parser.add_argument(
        "-p",
        "--prefix",
        nargs='?',
        help="Append a charachter before each "
        "line of the message tag if it is not present.",
        )
    args = parser.parse_args()

    logs = get_cmd_output("git log "
                          "--date-order "
                          "--tags "
                          "--simplify-by-decoration "
                          "--pretty=format:'%at %h %d'")
    log_line_reg = r"(?P<timestamp>\d+) (?P<commit>.*) \(.*tag: (?P<tag>\d.\d.\d).*\)"

    for i, log_line in enumerate(logs.split("\n")):
        result = re.search(log_line_reg, log_line)
        if result is None:
            continue
        groups = result.groupdict()

        timestamp = int(groups["timestamp"])
        # commit = groups["commit"]
        tag = groups["tag"]

        tag_msg = get_cmd_output(f"git tag {tag} -n500")
        try:
            _, message = tag_msg.split(tag, 1)
        except ValueError:
            continue

        if i == 0:
            print("Change Log")
            print("==========\n")
        print_changelog_entry(tag, timestamp, message, prefix=args.prefix)


if __name__ == '__main__':
    main()
