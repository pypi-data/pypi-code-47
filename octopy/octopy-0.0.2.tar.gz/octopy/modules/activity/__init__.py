from .event import Event
from .feed import Feed
from .notification import Notification
from .starring import Starring
from .watch import Watch


class Activity:

    """
    Official documentation in Github: https://developer.github.com/v3/activity/
    """

    """
    API Documentation: https://github.com/monzita/octopy/wiki/Activity.md
    """

    def __init__(self, url, headers, **kwargs):
        self.events = Event(url, headers)
        self.feeds = Feed(url, headers)
        self.notifications = Notification(url, headers)
        self.starring = Starring(url, headers)
        self.watching = Watch(url, headers)
