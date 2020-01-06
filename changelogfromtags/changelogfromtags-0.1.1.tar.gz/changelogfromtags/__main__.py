""" Entry point for changelogfromtags.

Generate a changelog from git tags.
"""

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


def print_changelog_entry(tag, timestamp, message):
    """ Print a format an changelog entry.

    :param str tag: "1.2.3"
    :param int timestamp: date time of tag
    :param int message: tag message
    """
    readable_tmp = datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y")
    header = f"{tag} ({readable_tmp})"
    print(header)
    print("-"*len(header))
    for line in message.split("\n"):
        print(line.strip())


def main():
    """ Main. """
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
        print_changelog_entry(tag, timestamp, message)


if __name__ == '__main__':
    main()
