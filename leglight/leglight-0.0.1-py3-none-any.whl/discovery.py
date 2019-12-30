"""Module for discovery of Elgato devices on the local network"""

from zeroconf import ServiceBrowser, Zeroconf
from time import sleep, time
import socket
from typing import cast
from . import LegLight
import requests

def discover(timeout=5):
    lights = []
    class thelistener:
        def remove_service(self, zeroconf, type, name):
            #print("Service %s removed" % (name,))
            pass

        def add_service(self, zeroconf, type, name):   
            info = zeroconf.get_service_info(type, name)
            ip = socket.inet_ntoa(info.addresses[0])
            port = cast(int, info.port)
            lname = info.name
            server = info.server
            lights.append(LegLight(lname, ip, port, server))


    zeroconf = Zeroconf()
    listener = thelistener()
    browser = ServiceBrowser(zeroconf, "_elg._tcp.local.", listener)

    try:
        # We're gonna loop for a bit waiting for discovery
        start = time()
        while True and (time() - start) < timeout:
            sleep(0.1)
    finally:
        # This sometimes takes a litteral second or two
        zeroconf.close()
    return(lights)