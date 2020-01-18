"""
通用标准指令集
"""
import time
import socket
import requests
import json
import re
import platform
if platform.system() == "Linux":
    from ddcmaker.linux.armv7l import get_equipment_type as ge
else:
    from ddcmaker.confusion import err_system as ge

