import xmltodict
import json

from Spitzer import host
from Spitzer.config import config
from Spitzer.chache import chache
from Spitzer.scanner import nmapper, masscanner
from Spitzer.print import print_error

#scanner class to combine the nmap and the masscanner class

def scan():
    #get configurations
    times = int(config.get_config('times'))
    rate = config.get_config('rate')
    hosts = config.get_config('ip')
    scan = config.get_config('ports')

    #scan options:
    #list: all from the exploit list
    #all: all ports
    #top1: top thousand from nmap
    #top10: top tenthousand from nmap
    #or you can add your own ports
    ports = ''
    if scan == 'list':
        port = config.get_data('services')
        for p in port:
            ports += str(p) + ','
        ports = '-p' + ports[:-1] #remove last comma
    elif scan == 'all':
        ports = '-p 0-65535'
    elif scan == 'top1':
        ports = '--top-ports=1000'
    elif scan == 'top10':
        ports = '--top-ports=10000'
    else:
        ports = '-p' + scan

    #run masscan x times
    #get results from masscan and create one list of hosts with ports
    if times != 0:
        result = {}
        for i in range(times):
            print('[-] Starting Masscan ' + str(i+1))
            masscanner.scan(hosts, ports, rate)
            xml = chache.read_file('sweep.xml')
            if xml == '':
                print_error('Scan '+str(i+1)+' failed! running nmap')
                return nmapper.run_nmap(hosts, ports)

            print('[-] Masscan '+str(i+1)+' done')

            mass = json.loads(json.dumps(xmltodict.parse(xml, attr_prefix='')))
            result = host.merge(mass, result)
            chache.remove_file('sweep.xml')
            
        #run nmap once to confirm scan (masscan has some false positives)

        print('[*] All masscans are done, found: ')
        #ugly lil sort method
        r = []
        for h in result:
            r.append(h)
        r.sort()
        for h in r:
            print(r)

        return nmapper.scan(result)
    else:
        return nmapper.run_nmap(hosts, ports)