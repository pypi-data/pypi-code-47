"""Manage inbound OFF All-Link Cleanup command to a device."""

from .. import inbound_handler
from .all_link_cleanup_command import AllLinkCleanupCommandHandlerBase
from ...topics import ON
from ...address import Address


class OnAllLinkCleanupInbound(AllLinkCleanupCommandHandlerBase):
    """Off All-Link Cleanup command inbound."""

    def __init__(self, address, group):
        """Init the OffAllLinkCleanupAckInbound class."""
        self._address = Address(address)
        self._group = group
        super().__init__(topic=ON, address=self._address, group=self._group)

    @inbound_handler
    def handle_command(self, cmd1, cmd2, target, user_data):
        """Handle the ON All-Link Cleanup from a device."""
        self._call_subscribers()
