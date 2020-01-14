'''
Created on Apr 17, 2019

@author: reynolds
'''

from PyQt5.QtCore import pyqtSignal

from wrtdk.io.streamer.streamer import LoggingStreamer
from wrtdk.parser.nmea.nmea import gpgga, gprmc

import time,os,sys,struct
import numpy as np
from _ast import Try
from wrtdk.data.buffer.buffer import byte_buffer

class tcp_streamer(LoggingStreamer):
    '''
    a streamer for streaming and logging TCP data
    Based largely off of Randals Serial_streamer
    '''
    EOL = bytes([10])
    new_msg = pyqtSignal(list,'QString',int,int)
    new_timeout = pyqtSignal()

    def __init__(self,port=None):
        '''
        Constructor
        '''
        self.buffer=byte_buffer()
        super().__init__()
        self.port = port
        self._logging = False
        self.gga = gpgga()
        self.rmc = gprmc()
        self.mcu_s = 0
        self.mcu_ms = 0
        self.gpsid = struct.pack('4sss',b'$GPS',bytes(0),bytes(0))
        self.fid = np.uint16(0)
        self.p1 = np.uint16(1)
        
    def setMCU(self,mcu=0):
        ''' sets the mcu time to write to the file '''
        self.mcu_s = int(mcu)
        self.mcu_ms = int( (mcu - self.mcu_s) * 1000 )
        
    def run(self):
        if self.port is not None: self._running = True
        
        while self._running:
            try:
                #Read in the msg. might be more than 1
                msg,addr = self.port.read(1024)
                
            except Exception as e:
                #self.new_msg.emit([time.time(),])
                exc_type, _, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print('%s:%s in %s at %d'%(exc_type.__name__,str(e), fname, exc_tb.tb_lineno))
                self.new_timeout.emit()
                if exc_type.__name__ == 'AttributeError': time.sleep(1)
                #self.new_msg.emit(['$ERROR',time.time(),addr,np.nan],'ND',0,0)# send an error message
                continue
            
            # if an empty mesage is received then skip it
            if msg is None: continue
            if len(msg) < 1: 
                self.new_msg.emit(['$EMPTY',time.time(),addr,np.nan],'ND',0,0)# send an error message
                continue
            #add the new data to the buffer
            self.buffer.append(msg)
            # write the data to a file
            if self.isLogging():
                string = msg.decode().strip().encode()
                if msg[0] == 36: wrapper = struct.pack('>6s4H2s5I%ds' % len(string),
                                                       self.gpsid,0,0,0,self.fid,b'AG',
                                                       self.mcu_s,self.mcu_ms,0,len(string),0,string)
                else: wrapper = struct.pack('>6s4H2s5I%ds' % len(string),
                                                       b'$COUNT',0,0,0,self.fid,b'AG',
                                                       self.mcu_s,self.mcu_ms,0,len(string),0,string)
                if msg[-1] is not 10: msg = msg + b'\n'# add a new line if necessary
                self.writer.write(wrapper)
            
            # parse the messages
            m=self.parse()
            self.new_msg.emit([m],'AG',self.buffer.pos,self.buffer.len)
            new_msg = pyqtSignal(list,'QString',int,int)
    def parse(self):
        if self.buffer.is_empty(): return
        try:
            b = bytes([self.buffer.get()])
        except Exception as e:
            print('error',str(e),self.buffer)
            return
        #find the first new line
        while(not self.is_eol(b) and not self.buffer.is_empty()):
            b = bytes([self.buffer.get()])
        #move forward 1
        buff=bytes()
        i=0
        while not self.buffer.is_empty():
            b = bytes([self.buffer.get()])
            buff = buff + b
            
            # check if the message is full
            if self.is_eol(b):
                self.buffer.remove_head()
                self.buffer.clear()
                return buff
            
        
        self.buffer.reset_position()
        
        if self.buffer.get_length() > 2000: self.buffer.clear()
    def is_eol(self,b):
        return b in self.EOL
        