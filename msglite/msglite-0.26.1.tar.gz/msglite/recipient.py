import logging

from msglite import constants
from msglite.properties import Properties
from msglite.utils import format_party

log = logging.getLogger(__name__)


class Recipient(object):
    """Contains one of the recipients in an msg file."""

    def __init__(self, dir_, msg):
        stream = msg._getStream([dir_, '__properties_version1.0'])
        self.props = Properties(stream, constants.TYPE_RECIPIENT)
        self.email = msg._getStringStream([dir_, '__substg1.0_39FE'])
        if not self.email:
            self.email = msg._getStringStream([dir_, '__substg1.0_3003'])
        self.name = msg._getStringStream([dir_, '__substg1.0_3001'])
        self.type = self.props.get('0C150003').value
        self.formatted = format_party(self.email, self.name)

    def __repr__(self):
        return '<Recipient(%s)>' % self.formatted
