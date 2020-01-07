'''
Created on Nov 19, 2019

@author: reynolds
'''

import os, sys, struct

from wrtdk.parser.parser import parser

class confv3(parser):
    '''
    classdocs
    '''
    
    LENGTH = 24
    VERSION = 3
    
    PREAMBLE = b'CONF'

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.reset()
        
    def reset(self):
        self._fid = self._minus1()
        self._svn = self._minus1()
        self._hdr = self._minus1()
        self._glb = self._minus1()
        self._tot = self._minus1()
        self._txs = self._minus1()
        self._sys = self._minus1()
        self._tme = self._minus1()
        self._cnt = self._minus1()
        self._hld = self._minus1()
        self._rxs = self._minus1()
        self._axs = self._minus1()
        self._bns = self._minus1()
        
    def get_bins(self):
        return self._bns
        
    def parse(self,msg):
        self.reset()
        
        try:
            m = struct.unpack('>4sHHBBBBHHxxHBBBB',msg[0:self.LENGTH])
            if m[0] != self.PREAMBLE: 
                raise('CONFFormatException',
                      'This is not an em configuration message')
            
            self._fid = m[1]
            self._svn = m[2]
            self._hdr = m[3]
            if self._hdr != self.VERSION: 
                raise Exception('CONFVersionException',
                                'This is not the proper version.')
            self._glb = m[4]
            self._tot = m[5]
            self._txs = m[6]
            self._sys = m[7]
            self._tme = m[8]
            self._cnt = m[9]
            self._hld = m[10]
            self._rxs = m[11]
            self._axs = m[12]
            self._bns = m[13]
        except Exception as e:
            self._error = True
            exc_type, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('%s:%s in %s at %d. MSG:%s'%(exc_type.__name__,str(e), fname, exc_tb.tb_lineno,msg))  
        
    def getData(self):
        ''' returns the data from the conf message
        0) FID
        1) SVN Revision
        2) Version Number
        3) Globals
        4) Duty States Total
        5) Duty States Tx
        6) System Timer
        7) Sample Timer
        8) Total Sample Count
        9) Holdoff
        10) Cube Count
        11) Axis Count
        12) Bin Count
        '''
        return [self._fid,self._svn,self._hdr,self._glb,
                self._tot,self._txs,self._sys,self._tme,
                self._cnt,self._hld,self._rxs,self._axs,
                self._bns]