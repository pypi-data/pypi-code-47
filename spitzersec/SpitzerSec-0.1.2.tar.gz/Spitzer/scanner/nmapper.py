import nmap
import os
import multiprocessing
import datetime
import re
import time
from tqdm import tqdm

from Spitzer.config import config
from Spitzer.print import print_error
from Spitzer import command
from Spitzer.chache.chache import get_path
from Spitzer import interlace
from Spitzer import command
from Spitzer.host import get_hosts, get_ports
from Spitzer.result.result import add
#runs nmap, not much further to say...

nm = nmap.PortScanner()

def run_nmap(ip, ports):
    print('[-] Starting nmap')

    script = find_scripts(ports)
    flags = config.get_config('nmapFlags')

    cmd = ['nmap', flags, '-Pn', '-sV', ports, ip, '-oX', 
    get_path() + 'scan_'+ip.split('/')[0]+'.xml','-oN',  get_path() + 'scan_'+ip.split('/')[0]+'.txt']

    if script != '':
        cmd += script
    result = command.run(cmd, capture_output=True, verbose=int(config.get_config('verbose')))
    if '0 hosts up' in result:
        print_error('Nothing found')
        return None
    return get_results()

def scan(hosts):
    print('[-] Starting nmap')
    for host, ports in tqdm(hosts.items()):
        script = find_scripts(ports)
        txt = ['-oN', get_path() + 'scan_' + host + '.txt'] #TODO Fix working with hostnames
        xml = ['-oX', get_path() + 'scan_' + host + '.xml']
        arguments = ['nmap', config.get_config('nmapFlags'), '-Pn', '-sV', '-p', stringify_ports(ports), host] + txt + xml

        if script != '':
            arguments.append(script)
        command.run(arguments, verbose=int(config.get_config('verbose')))
    return get_results()



def get_results():
    result = {}
    text = ''
    
    try:
        os.mkdir('xml')
    except FileExistsError:
        pass

    for file in os.listdir(get_path()):
        if file.startswith('scan_') and file.endswith('.xml'):
            try:
                xml_result = parse_xml(open(get_path() + file, 'r').read())
            except nmap.PortScannerError:
                print_error('Error with scanning host: ' + file.replace('scan_', '').replace('.xml', ''))
                os.system('stty sane')
                continue

            host = file.replace('scan_', '').replace('.xml', '')
            result[host] = xml_result['scan'][host]
            f = open('xml/' + file, 'a+')
            f.write(open(get_path() + file, 'r').read())
            f.close()

        if file.startswith('scan_') and file.endswith('.txt'):
            text +=  open(get_path() + file, 'r').read() + '\n\n'
            add(file.replace('scan_', '').replace('.txt', ''), 'nmap scan', open(get_path() + file, 'r').read())

    open(os.getcwd() + '/scan.txt', 'w+').write(text)
    return  result


def parse_xml(xml):
    result = nm.analyse_nmap_xml_scan(xml)
    if 'error' in result['nmap']['scaninfo']:
        print_error('[!]' + result['nmap']['scaninfo']['error'])
        raise RuntimeError
    return result

def stringify_ports(ports):

    port = ''
    if isinstance(ports, list):
        for p in ports:
            port += str(p) + ','
    else:
        return str(ports)

    return port[:-1]

def find_scripts(ports):

    result = ''
    scripts = config.get_data('services')

    for port in ports:
        if port not in scripts:
            continue

        if len(scripts[port]) > 1 and scripts[port][1] != '':
            result += scripts[port][1] + ','
    if result != '':
        return '--script=' +result[:-1]
    else:
        return ''
