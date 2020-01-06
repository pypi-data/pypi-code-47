
'''
Module to control the GlobalCache iTach IP to IR devices.

Models and specifications are available here: https://www.globalcache.com/products/itach/models2/.

The model tested is the IP2IR. This device has a wired Ethernet connection
and can support up to 3 IR outputs.

See the Global Cache support site (https://globalcache.com/downloads/) for 
software utilities and API documentation.
'''

import socket
import time

class ITachIRBlaster():
    '''
    Class to control the GlobalCache iTach IP to IR devices.

    This class is intended to be a parent class for platform specific
    remote control classes that include IR codes (e.g. MediaFirstRemoteControl).
    '''

    def __init__(self, hostname, port=4998):
        self.host = hostname
        self.port = port

    def send_command(self, code, delay=0.5):
        '''
        Use the Global Cache TCP API to send a command to an iTach IP to IR device.

        The Global Cache TCP API documentation is available on the Global Cache
        support site: https://globalcache.com/support

        Commands are in the format: 
            <command>,<module>:<port>,<parameter1>,<parameter2>,...

        The iLearn utility, also available on the Global Cache support site, can 
        learn IR codes from an existing remote control device and save them in 
        this format. Note, however, that the port is included in the learned command.
        If you want to send commands to a different port, you will need to change
        the learned command accordingly.
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(code.encode())
            resp = s.recv(1024)
            #print(resp)
        time.sleep(delay)