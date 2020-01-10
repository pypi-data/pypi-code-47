#filename: fasthex.py
#author: (C) Menschel 2019
#purpose: Implement a fast way to handle hex files in python3 as the Intelhex module is notoriously slow
#license: GPL-V3
import os
import sys
import struct

IHEX_SC = ":"#0x3A #collon ":" is start code for all valid lines
#the record type that represents
IHEX_RECT_DT    = 0x0 #data 
IHEX_RECT_EOF   = 0x1 #End of File
IHEX_RECT_OADDR = 0x4 #offset address, e.g. the first part of a 32bit address


def interpret_hex_line(line):
    """
    interpret a hex line and return its contents
    @param line: a complete line from a hex file
    @return: a tuple of (byte count, line address, record type, data, checksum)
    """
    ret = None
    L = line.strip()
    if L[0] == IHEX_SC:
        Lb = bytes.fromhex(L[1:])
        cchksm = sum(Lb) & 0xFF
        if cchksm == 0:#line is ok
            bc = Lb[0]#byte count
            laddr = struct.unpack(">H",Lb[1:3])[0]#line address - big endian 16 bit
            rec_t = Lb[3]#record type - the type of information
            data = Lb[4:-1]
            chksm = Lb[-1]#we don't care
            ret = bc,laddr,rec_t,data,chksm
        else:
            raise NotImplementedError("Checksum error") 
    return ret


def calc_chksum(data):
    """
    calculates the checksum for data
    @param data: data
    @return: the checksum
    """
    return (0x100 - sum(data)) & 0xFF

def concat_hex_line(laddr,rec_t,data=b""):
    """
    concatenates a line of a hex file
    @param laddr: the line address where this data starts
    @param rec_t: the record type of this line
    @param data: the data of this line
    @return: a line of a hex file
    """
    L = bytearray()
    L.append(len(data))
    L.extend(struct.pack(">H",laddr))
    L.append(rec_t)
    L.extend(data)
    L.append(calc_chksum(L))
    return ":"+L.hex().upper()

def generate_hex_lines(addr,data,linewidth=0x20):
    """
    generates lines for a hex file
    @param addr: the address where data starts
    @param data: the data
    @param linewidth: the byte count how many bytes should be written in a single line
    @return: a list of lines
    """
    #Todo: this could be easily changed to a generator
    lines = []
    lhaddr = -1
    for idx,caddr in enumerate(range(addr,len(data)+addr,linewidth)):
        laddr = caddr & 0xFFFF #lower 16bit
        if caddr & 0xFFFF0000 != lhaddr:
            lhaddr = caddr & 0xFFFF0000 #upper 16 bit
            #write a 04 line
            lines.append(concat_hex_line(laddr=0,rec_t=IHEX_RECT_OADDR,data=struct.pack(">H",lhaddr >> 16)))
        lines.append(concat_hex_line(laddr=laddr,rec_t=IHEX_RECT_DT,data=data[idx*linewidth:(idx+1)*linewidth]))
    return lines


def interpret_hex_file_from_str(data):
    """
    interprets a hex file passed as a string for convenience
    @param data: a string containing the contents of a hex file
    @return: a list of data chunk tuples (addr,data) addr is an integer, data is a bytearray
    """    
    buff = bytearray()#the currently used buffer of bytes, we could use a bytestr instread
    buffaddr = 0#the addr where those bytes are located
    caddr = 0 #the address that we are currently are
    contents = []
    linecount = 1
    
    for line in data.split("\n"):
        try:
            linedata = interpret_hex_line(line.strip())
        except Exception as e:
            print("{0} while reading line {1}".format(e,linecount))
            sys.exit(0)
        else:
            if linedata is not None and (len(linedata) == 5):#paranoia
                bc,laddr,rec_t,data,chksm = linedata
                #print(hex(caddr),hex(laddr))
                if rec_t == IHEX_RECT_DT:
                    #check if laddr is our current addr
                    #print("data")
                    if ((caddr & 0xFFFF) != laddr):
                        if len(buff)>0:
                            raise NotImplementedError("New block without extended addr {0:08X} {1:08X}".format(caddr,laddr))
                        else:
                            caddr = (caddr & 0xFFFF0000) + laddr
                    if buffaddr is None:
                        buffaddr=caddr
                    caddr += bc
                    buff.extend(data)
                elif rec_t == IHEX_RECT_OADDR:

                    oaddr = (struct.unpack(">H",data)[0]) << 16 #upper 16 bit

                    if (caddr & 0xFFFF0000) != oaddr:
                            
                        if len(buff)>0:
                            contents.append((buffaddr,buff))
                        caddr = oaddr
                        buffaddr = None
                        buff = bytearray()

                elif rec_t == IHEX_RECT_EOF:
                    if len(buff)>0:
                        contents.append((buffaddr,buff))
                    break
                else:
                    raise NotImplementedError("rec_t {0} is not handled".format(rec_t))

        linecount += 1
    return contents


class intelhex():

    def __init__(self,fpath=None):
        """
        intelhex class constructor
        @param fpath: the file path where to read from
        """
        self.contents = []#contents will be a list of (addr,bytearray)-tupples
        if fpath is not None:
            self.read_hex_file(fpath=fpath)
        
        
    def read_hex_file(self,fpath):
        """
        read a hex file - updates the objects contents
        @param fpath: the file path
        """
        with open(fpath) as f:
            data = f.read()
        return self.from_str(data)

    def from_str(self,data):
        """
        read a hex file passed as a string - updates the objects contents
        @param data: a data string
        """
        self.contents = interpret_hex_file_from_str(data)
        return

    def to_str(self):
        """
        concats the object contents to be written to a hex file
        @return: a multi line string
        """
        lines = []
        for addr,data in self.contents:
            lines.extend([line for line in generate_hex_lines(addr,data)])
        lines.append(concat_hex_line(laddr=0,rec_t=IHEX_RECT_EOF))
        return "\n".join(lines)
    
    def print_blocks(self):
        """
        print the blocks / chunks of data we have as object contents
        this is basically a lazy way to find out if our hex file has gaps,
        what the flash block sizes are etc.
        """
        for idx in range(len(self.contents)):
            addr,data = self.contents[idx]
            print("Block {0} - Addr {1:08X} - Len {2:08X}".format(idx,addr,len(data)))
        return

    def getz(self,baddr,blen):
        """
        gets a byte string from the object contents
        @param baddr: the byte address from where the bytestring should start
        @param blen: the byte length how long the bytestring should be
        @return: a byte string starting at baddr of size blen
        """
        ret = None
        for addr,data in self.contents:
            if (addr < baddr) and ((addr+len(data)) > (baddr+blen)):
                offset = baddr-addr
                ret = data[offset:offset+blen]
                break
        if ret is None:
            raise ValueError("baddr {0:08X} to baddr+blen {1:08X} not in blocks".format(baddr,baddr+blen))
        return ret

    def putz(self,baddr,data):
        """
        puts a byte string at a given address
        @param baddr: the byte address where to put data
        @param data: the data to be put
        """
        blen = len(data)
        for addr,_data_ in self.contents:
            if (addr < baddr) and ((addr+len(_data_)) > (baddr+blen)):
                offset = baddr-addr
                _data_[offset:offset+blen] = data
                break
        return

    def write_hex_file(self,fpath):
        """
        write a hex file to a given path
        @param fpath: the file path
        """
        with open(fpath,"w") as f:
            f.write(self.to_str())
        return
                
            
#convenience function
def intelhex_from_str(data):
    """
    create and return an intelhex object from string data
    @param data: the string data contents of a hex file
    @return: an intelhex object
    """
    h = intelhex()
    h.from_str(data)
    return h
