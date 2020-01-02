import os


class STRINGS:
    """ Class to encapsulate string literal values to remove 'magic strings'"""

    SLACK_API_TOKEN_ENV = "SLACK_API_TOKEN"


SLACK_API_TOKEN = os.getenv(STRINGS.SLACK_API_TOKEN_ENV)
