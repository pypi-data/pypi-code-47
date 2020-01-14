import subprocess
import sys
import time

from Spitzer.config.config import get_config
from Spitzer.chache.chache import get_path


def run(command, hosts, ports=None):
    #get stuff from config
    threads = get_config('threads')

    ports = convert(ports)
    path = get_path()
    convert(command, seperator='\n', path=path + 'commands.txt')
    convert(hosts, seperator='\n', path=path + 'targets.txt')
        
    cmd = ['interlace', '-threads', threads, '-cL', path+'commands.txt', '-tL', path+'targets.txt', '-o', get_path() ] 

    if ports is not None:
        cmd += ['-p', ports]
    execute(cmd)

def execute(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
    while True:
        output = process.stdout.readline()
        
        if output == '' and process.poll() is not None:
            #stopped
            break
        if 'it/s' in output and output[2] == '%':
            print(output, end='\r')

    print('\n')
    sys.stdin = sys.__stdin__

def convert(var, typ=list, seperator=',', path=None):
    result = var
    if isinstance(var, typ):
        result = ''
        for v in var:
            result += v + seperator
        result = result[:-len(seperator)]

    if path is not None:
        open(path, 'w+').write(result)

    return result