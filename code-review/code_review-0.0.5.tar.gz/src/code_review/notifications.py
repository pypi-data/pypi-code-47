import re
import webbrowser

from github import Github

URL_REPLACEMENTS = {'/api.': '/', 'repos/': '', 'pulls': 'pull'}


def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)


def adapt_url(notification):
    return replace(notification, URL_REPLACEMENTS)


class NotificationViewer:
    def __init__(self, token):
        self.g = Github(token)
        self.notifications = self.g.get_user().get_notifications()

    def stdout(self):
        for notification in self.notifications:
            print(notification.reason, notification.subject.title, adapt_url(notification.subject.url))

    def open(self):
        webbrowser.get()
        for notification in self.notifications:
            webbrowser.open_new_tab(adapt_url(notification.subject.url))
