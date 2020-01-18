import json
import subprocess
import time
import os
import base64
from ddcmaker.code_check.code_safety import settime
import platform
if platform.system() == "Linux":
    from ddcmaker.linux.armv7l import get_equipment_type as ge
else:
    from ddcmaker.confusion import err_system as ge




