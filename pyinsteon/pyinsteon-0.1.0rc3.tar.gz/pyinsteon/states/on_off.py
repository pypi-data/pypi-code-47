"""On / Off state."""
from . import StateBase
from ..address import Address


class OnOff(StateBase):
    """On / Off state."""

    def __init__(
        self, name: str, address: Address, group: int = 0, default: int = None
    ):
        """Init the OnLevel class."""
        super().__init__(name, address, group, default, value_type=int)

    # pylint: disable=arguments-differ
    def set_value(self, on_level):
        """Set the value of the state from the handlers."""
        self.value = 0xFF if on_level else 0


class LowBattery(StateBase):
    """Low battery state."""

    def __init__(
        self, name: str, address: Address, group: int = 0, default: int = None
    ):
        """Init the LowBattery class."""
        super().__init__(name, address, group, default, value_type=bool)

    # pylint: disable=arguments-differ
    def set_value(self, low_battery):
        """Set the value of the state from the handlers."""
        self.value = bool(low_battery)


class Heartbeat(StateBase):
    """Heartbeat state."""

    def __init__(
        self, name: str, address: Address, group: int = 0, default: int = None
    ):
        """Init the Hearbeat class."""
        super().__init__(name, address, group, default, value_type=bool)

    # pylint: disable=arguments-differ
    def set_value(self, heartbeat):
        """Set the value of the state from the handlers."""
        self.value = bool(heartbeat)
