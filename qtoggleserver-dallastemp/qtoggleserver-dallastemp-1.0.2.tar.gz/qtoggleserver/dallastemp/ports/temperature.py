
import logging
import re

from typing import Optional

from qtoggleserver.lib import onewire


logger = logging.getLogger(__name__)


class DallasTemperatureSensor(onewire.OneWirePeripheral):
    TEMP_PATTERN = r't=(\d+)'

    logger = logger

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._temp: Optional[float] = None

    def get_temp(self) -> Optional[float]:
        data = self.read()
        if data:
            m = re.search(self.TEMP_PATTERN, data, re.MULTILINE | re.DOTALL)
            if m:
                self._temp = round(int(m.group(1)) / 100.0) / 10.0
                self.debug('temperature is %.1f degrees', self._temp)

        return self._temp


class Temperature(onewire.OneWirePort):
    TYPE = 'number'
    WRITABLE = False
    MIN = -55
    MAX = 125
    UNIT = u'\xb0C'  # Degrees celsius

    PERIPHERAL_CLASS = DallasTemperatureSensor
    ID = 'temperature'

    async def read_value(self) -> Optional[float]:
        return self.get_peripheral().get_temp()
