import subprocess
import threading

from Spitzer.config import config
from Spitzer import command


#runs masscanner twice and writes the output into a xml file in the chache folder
chache = __file__[:-21] + 'chache/' 
def scan(hosts, ports, rate):
    print()
    cmd = [
        'masscan',
        hosts,
        '-oX',chache + 'sweep.xml',
        '-e', config.get_config('interface'),
        '--wait=0',
        '--rate=' + rate,
        ports
        ]

    command.run(cmd, verbose=int(config.get_config('verbose')))
    