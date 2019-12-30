"""Manage the inbound messages that trigger a variable state's on level."""
from datetime import datetime, timedelta
from ..subscriber_base import SubscriberBase
from ..address import Address
from ..handlers.from_device.on_level import OnLevelInbound
from ..handlers.from_device.off import OffInbound
from ..handlers.from_device.on_fast import OnFastInbound
from ..handlers.from_device.off_fast import OffFastInbound
from ..handlers.from_device.on_level_all_link_cleanup import OnAllLinkCleanupInbound
from ..handlers.from_device.off_all_link_cleanup import OffAllLinkCleanupInbound
from ..handlers.to_device.on_all_link_cleanup_ack import OnAllLinkCleanupAckCommand
from ..handlers.to_device.off_all_link_cleanup_ack import OffAllLinkCleanupAckCommand

TIMEOUT = 5  # number of seconds to define duplicate time inteval


class OnLevelManager:
    """Manage the inbound messages that trigger a variable state's on level.

    The manager is used in all variable state devices. These include:
        - Category 0 devices such as Mini-Remotes
        - All category 1 dimmable devices
        - etc

    This manager handles inbound broadcast messages that identify a state change of
    a device. It also handles inbound clean up messages that follow the broadcast
    message. Finally, it is responsible to deduplicate messages to ensure multiple
    broadcast and cleanup messages to the same group for the same state change
    only trigger once.
    """

    class Subscriber(SubscriberBase):
        """Internal class to trigger notification of events or state values."""

        def call_subscribers(self, on_level):
            """Call subscribers to this manager for the event type."""
            self._call_subscribers(on_level=on_level)

    def __init__(self, address, group, default_on_level=0xFF):
        """Init the OnLevelManager class."""
        self._address = Address(address)
        self._group = int(group)
        self._default_on_level = default_on_level
        self._last_event = datetime(1, 1, 1, 1, 1, 1)

        # Setup event managers that will manange the subscribers to specific events
        self._on = self.Subscriber(
            "subscriber_{}_on_{}_broadcast".format(self._address.id, self._group)
        )
        self._off = self.Subscriber(
            "subscriber_{}_off_{}_broadcast".format(self._address.id, self._group)
        )
        self._on_fast = self.Subscriber(
            "subscriber_{}_on_fast_{}_broadcast".format(self._address.id, self._group)
        )
        self._off_fast = self.Subscriber(
            "subscriber_{}_off_fast_{}_broadcast".format(self._address.id, self._group)
        )

        # Register the handlers to listen to
        self._on_handler = OnLevelInbound(self._address, self._group)
        self._off_handler = OffInbound(self._address, self._group)
        self._on_fast_handler = OnFastInbound(self._address, self._group)
        self._off_fast_handler = OffFastInbound(self._address, self._group)
        self._on_cleanup_handler = OnAllLinkCleanupInbound(self._address, self._group)
        self._off_cleanup_handler = OffAllLinkCleanupInbound(self._address, self._group)

        # Subscribe to events
        self._on_handler.subscribe(self._on_event)
        self._off_handler.subscribe(self._off_event)
        self._on_fast_handler.subscribe(self._on_fast_event)
        self._off_fast_handler.subscribe(self._off_fast_event)
        self._on_cleanup_handler.subscribe(self._on_cleanup_event)
        self._off_cleanup_handler.subscribe(self._off_cleanup_event)

    def subscribe(self, callback):
        """Subscribe to all events (ON, OFF, ON FAST, OFF FAST)."""
        self._on.subscribe(callback)
        self._off.subscribe(callback)
        self._on_fast.subscribe(callback)
        self._off_fast.subscribe(callback)

    def subscribe_on(self, callback):
        """Subscribe to ON events."""
        self._on.subscribe(callback)

    def subscribe_off(self, callback):
        """Subscribe to OFF events."""
        self._off.subscribe(callback)

    def subscribe_on_fast(self, callback):
        """Subscribe to ON FAST events."""
        self._on_fast.subscribe(callback)

    def subscribe_off_fast(self, callback):
        """Subscribe to OFF FAST events."""
        self._off_fast.subscribe(callback)

    def _on_event(self, on_level):
        self._process_event(on_level=on_level)

    def _off_event(self, on_level):
        self._process_event(on_level=0)

    def _on_fast_event(self, on_level):
        self._process_event(on_level=on_level)

    def _off_fast_event(self, on_level):
        self._process_event(on_level=0)

    def _on_cleanup_event(self):
        OnAllLinkCleanupAckCommand(self._address, self._group).send()
        self._process_event(on_level=self._default_on_level)

    def _off_cleanup_event(self):
        OffAllLinkCleanupAckCommand(self._address, self._group).send()
        self._process_event(on_level=0)

    def _process_event(self, on_level):
        last_event = self._last_event
        self._last_event = now = datetime.now()
        if (now - last_event) < timedelta(0, TIMEOUT):
            return
        self._on.call_subscribers(on_level=on_level)
