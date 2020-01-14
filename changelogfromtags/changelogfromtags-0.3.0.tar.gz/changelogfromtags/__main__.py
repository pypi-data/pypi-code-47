""" Entry point for changelogfromtags.

Generate a changelog from git tags.
"""

import argparse
from datetime import datetime
import logging
import re
import shlex
import subprocess


def get_cmd_output(cmd):
    """ Execute a command and returns the output.

    :param str cmd: Command to execute.
    :returns: Command stdout content.
    :raises: ValueError with stderr content if their is one.
    """
    logging.debug(cmd)
    args = shlex.split(cmd)
    process = subprocess.Popen(args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, strerr = process.communicate()
    logging.debug(stdout)
    if strerr:
        raise ValueError(strerr)
    return stdout.decode()


def get_readable_timestamp(timestamp):
    """
    :param int timestamp:
    :returns: string
    """
    return datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y")


class Changelog:
    """ Changelog representation. """

    def __init__(self, title, prefix):
        self.title = title
        self.prefix = prefix
        self.entries = []

    def add_entry(self, tag, timestamp, message):
        self.entries.append((tag, timestamp, message))

    def _format_changelog_entry(self, index):
        tag, timestamp, message = self.entries[index]
        entry = f"{tag} ({get_readable_timestamp(timestamp)})"
        entry += "\n" + "-"*len(entry) + "\n"
        for line in message.split("\n"):
            line = line.strip()
            # prepend prefix if not present
            if line and self.prefix and not line.startswith(self.prefix):
                line = self.prefix + line
            entry += line + "\n"
        return entry

    def __repr__(self):
        """ Dump the changelog content.  """
        out = self.title
        out += "\n" + "="*len(self.title) + "\n\n"
        for index, entry in enumerate(self.entries):
            logging.debug(entry)
            out += self._format_changelog_entry(index)
        return out


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
    parser.add_argument(
        "-t",
        "--title",
        nargs='?',
        help="Title in the header",
        default="Changelog"
    )
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    logging.basicConfig(level={
        1: "INFO",
        2: "DEBUG"
    }.get(args.verbose, "WARNING"))
    logging.debug(args)

    changelog = Changelog(args.title, args.prefix)

    logs = get_cmd_output("git log "
                          "--date-order "
                          "--tags "
                          "--simplify-by-decoration "
                          "--pretty=format:'%at %h %d'")
    log_line_reg = r"(?P<timestamp>\d+) (?P<commit>.*) \(.*tag: (?P<tag>.*?)(,.*)?\)"
    for i, log_line in enumerate(logs.split("\n")):
        result = re.search(log_line_reg, log_line)
        if result is None:
            continue
        groups = result.groupdict()

        # commit = groups["commit"]
        tag = groups["tag"]
        timestamp = int(groups["timestamp"])
        tag_msg = get_cmd_output(f"git tag {tag} -n500")
        try:
            _, message = tag_msg.split(tag, 1)
        except ValueError:
            continue

        changelog.add_entry(tag, timestamp, message)

    print(str(changelog))


if __name__ == '__main__':
    main()
