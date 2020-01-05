from pwn import *
from LibcSearcher import *


class Pwn:
    def __init__(self, binary=None, libc = None, ip=None, port=None, REMOTE=False):

        self.binary = None
        self.elf = None
        self.p = None
        self.libc = None

        self.REMOTE = REMOTE

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

        if REMOTE and ip and port:
            self.ip = ip
            self.port = port
            self.p = remote(ip,port)

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



def fmt64(offset,addr,val):
    Log("not implentment")
    return None

def fmt(offset,addr,val,bits=None):
    if not bits:
        Log("please set bits as the 4th args")
        return None
    if bits == 32:
        return fmtstr_payload(offset,{addr:val})
    if bits == 64:
        return fmt64(offset,addr,val)

#log and debug
def Log(name, addr = None):
    if addr:
        log.info(name + ' ' + hex(addr))
    else:
        log.indo(name)

def debug(p,b=None):
    if p.REMOTE:
        pass
    else:
        gdb.attach(p.p,b)

#heap exp
def heap_exp():
    print(
    """
    def menu(idx):
        p.ru('Command: ')
        p.sl(str(idx))

    def add(size):
        menu(1)
        p.ru("Size: ")
        p.sl(str(size))

    def edit(idx,size, content):
        menu(2)
        p.ru("Index: ")
        p.sl(str(idx))
        p.ru("Size: ")
        p.sl(str(size))
        p.ru('Content: ')
        p.s(content)

    def delete(idx):
        menu(3)
        p.ru('Index: ')
        p.sl(str(idx))

    def show(idx):
        menu(4)
        p.ru("Index: ")
        p.sl(str(idx))
    """
    )

if __name__ == '__main__':
    pwn = Pwn("/home/msk/Desktop/work/guangwai/pwn01/pwn1")
    context.log_level = 'debug'
    print fmt(5,0xdeadbeef,0x12345678,32)
    debug(pwn)
    pwn.ia()

        
