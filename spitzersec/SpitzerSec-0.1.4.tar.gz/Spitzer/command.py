import subprocess
import os

from Spitzer.config import config
from Spitzer.print import print_error


#runs shell command

def run(cmd, capture_output=False, check=True, verbose=None):#TODO fix verbose to be boolean
    print(cmd)
    if verbose is not None:
        if verbose == -1:
            capture_output = True
        if verbose > 0:
            v = '-'
            for _ in range(verbose):
                v += 'v'
            cmd.append(v)

    pipe = None
    if capture_output:
        pipe = subprocess.PIPE
    process = subprocess.Popen(cmd, stdout=pipe, bufsize=1000000)
    code = process.wait()
    if check and code != 0:
        print_error('Error in executing ' + cmd[0])#TODO logging?
        #print(process)

    r = process.communicate()[0]
    if r is not None: #TODO check if bytes, instead of none
        return r.decode("utf-8")
    else:
        return r
