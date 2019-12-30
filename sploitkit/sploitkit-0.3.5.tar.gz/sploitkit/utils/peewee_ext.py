# -*- coding: UTF-8 -*-
import re
from ipaddress import ip_address
from peewee import *


__all__ = ["IPAddressField", "MACAddressField"]


class IPAddressField(BigIntegerField):
    """ IPv4/IPv6 address database field. """
    def db_value(self, value):
        if isinstance(value, (str, int)):
            try:
                return int(ip_address(value))
            except Exception:
                pass
        raise ValueError("Invalid IPv4 or IPv6 Address")

    def python_value(self, value):
        return ip_address(value)


class MACAddressField(BigIntegerField):
    """ MAC address database field. """
    def db_value(self, value):
        if isinstance(value, int) and 0 <= value <= 0xffffffffffffffff:
            return value
        elif isinstance(value, str):
            if re.search(r"^([0-9a-f]{2}[:-]){5}[0-9A-F]{2}$", value, re.I):
                return int("".join(re.split(r"[:-]", value)), 16)
        raise ValueError("Invalid MAC Address")

    def python_value(self, value):
        try:
            return ":".join(re.findall("..", "%012x" % value))
        except Exception:
            raise ValueError("Invalid MAC Address")
