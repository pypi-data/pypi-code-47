from ptrlib.util.packing import *

class Robot(object):
    """Dynamically find function in loaded libc
    """
    def __init__(self, leak, base=0x400000, elf=None):
        self.proc_base = base
        self.libc_base = None
        self.elf = elf
        self.internal_leak = leak

        # Assertion
        if self.leak(self.proc_base, 4) != b'\x7fELF':
            logger.warn("proc base or leak function is wrong")
        else:
            logger.info("proc base is correct")
        
        # Initialize
        self.libc_base = self.libc()
        return

    def leak(self, address, size):
        output = b''
        for i in range(4):
            r = self.internal_leak(address + len(output))
            if len(r) == 0:
                logger.warn("`leak` is not working!")
                return None
            output += r
            if len(output) >= size:
                break
        return output[:size]
    
    def libc(self):
        """ Find libc base """
        if self.elf is None:
            # [TODO]
            raise NotImplementedError("Currently requires the target binary.")
        else:
            pass
        return

    def find(self, name):
        """ Find a function by name """
        address = 0
        return self.libc_base + address
    
    
