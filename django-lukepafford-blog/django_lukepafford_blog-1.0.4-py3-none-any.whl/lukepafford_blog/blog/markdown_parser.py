import yaml
import re


class MarkdownParsingError(Exception):
    pass


def parse_yaml_post(file):
    """
    Returns a dictionary of headers, and
    the body
    """
    data = file.read().decode("utf8")
    pattern = re.compile(
        r"^---\n(?P<headers>.*?)---\n(?P<body>.*$)", re.MULTILINE | re.DOTALL
    )
    match = re.match(pattern, data)

    if match:
        headers = yaml.safe_load(match.group("headers"))
        body = match.group("body")
        return {**headers, "body": body}

    else:
        raise MarkdownParsingError
