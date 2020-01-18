import time
import os
import sqlite3 as sql
import platform
if platform.system() == "Linux":
    from ddcmaker.linux.armv7l import get_equipment_type as ge
    from ddcmaker.public.hwax import HWAX
else:
    from ddcmaker.confusion import err_system as ge
    # ge = get_equipment_type()
from ddcmaker.public import SerialServoCmd as ssc
from ddcmaker.public import config_serial_servo
import threading

