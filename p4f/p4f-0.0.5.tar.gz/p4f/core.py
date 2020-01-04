from pwn import *
from LibcSearcher import *


class Pwn:
    def local_run(self):
        self.p = process(self.binary)

    def remote_run(self):
        self.p = remote(ip, port)

    def __init__(self, binary=None, libc = None, ip=None, port=None, remote=False):

        self.binary = None
        self.elf = None
        self.p = None
        self.libc = None

        self.remote = False

        self.libcbase = 0
        self.stackbase = 0
        self.codebase = 0

        if not binary and not ip:
            log.info("input binary path or ip and port")

        if binary:
            self.binary = binary
            elf = ELF(self.binary)

        if libc:
            self.libc = ELF(libc)

        if ip and port and remote:
            self.ip = ip
            self.port = port
            self.p = remote(ip.port)

        elif binary:
            self.p = process(self.binary)
    
    #short use
    def s(self,a):
        return self.p.send(a)
    def sl(self,a):
        return self.p.sendline(a)
    def sla(self,a,b):
        return self.p.sendlineafter(a,b)
    def r(self):
        return self.p.recv()
    def rn(self,n):
        return self.p.recvn(n)
    def ru(self,n):
        return self.p.recvuntil(n)
    def rl(self):
        return self.p.recvline()
    def ia(self):
        return self.p.interactive()
    def c(self):
        return self.p.close()

    #leak libc
    def leakLibc(self,name,addr):
        try:
            obj = LibcSearcher(name,addr)
            self.libcbase = addr - obj.dump(name)
            Log("libcbase", self.libcbase)
        except:
            pass
    
    def one(self,version=None):
        if not version:
            Log("one(version) version can be int 16 or 18")
            Log("16 -> glibc 2.23")
            Log("18 -> glibc 2.27")
        elif version == 16:
            l = [0x45216,0x4526a,0xf02a4,0xf1147]
        elif version == 18:
            l = [0x4f2c5,0x4f322,0x10a38c]
        return l


def Log(name, addr = None):
    if addr:
        log.info(name + ' ' + hex(addr))
    else:
        log.indo(name)

def debug(p,b=None):
    gdb.attach(p.p,b)



if __name__ == '__main__':
    pwn = Pwn("./pwn")
    context.log_level = 'debug'

        
