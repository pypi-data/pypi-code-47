"""Manage inbound ON command from device."""
from .. import broadcast_handler
from .broadcast_command import BroadcastCommandHandlerBase
from ...topics import OFF
from ...address import Address


class OffInbound(BroadcastCommandHandlerBase):
    """Off Level command inbound."""

    def __init__(self, address, group):
        """Init the OffInbound class."""
        self._address = Address(address)
        self._group = group
        super().__init__(topic=OFF, address=self._address, group=self._group)

    @broadcast_handler
    def handle_command(self, cmd1, cmd2, target, user_data):
        """Handle the OFF command from a device."""
        self._call_subscribers(on_level=0)
