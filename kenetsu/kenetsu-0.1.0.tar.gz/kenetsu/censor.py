import re


class Censor():
    EMAIL_REGEX = r'<\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*>'
    EMAIL_DUMMY = "<censored@example.org>"

    def __init__(self):
        self.regex = re.compile(Censor.EMAIL_REGEX)

    def censor(self, line):
        """Returns censored string
        """
        return self.regex.sub(Censor.EMAIL_DUMMY, line)
