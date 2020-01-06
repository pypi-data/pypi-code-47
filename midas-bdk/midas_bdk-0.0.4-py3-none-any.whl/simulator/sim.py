import os
import sys
import logging

sys.path.append('..')

from midasbdk.data.dataloader import DataLoader

class Simulator(object):
    def __init__(self):
        self.brains = []
 
    def registerBrain(self, brain, ratio):
        self.brains.append({'brain':brain, 'ratio':ratio})

    def configLogger(self, name):
        logging.basicConfig(filename=name, filemode='w', level=logging.INFO, format='%(message)s')

    def run(self):
 
        for brain in self.brains:
            codes = brain['brain'].getCandidates()
            loader = DataLoader()

            cnt = 0
            for code in codes:	
                loader.setStock(code)
                loader.loadAll()
            
                cnt = cnt + 1
                print('({}/{}'.format(cnt,len(codes)))
                max_len = loader.getLength()
                req_len = brain['brain'].getRequiredSeqLen()
                brain['brain'].resetPosition()
                for i in reversed(range(max_len-req_len)):   # hard-coded
                    data = loader.getSequence(i,max_len-i)
                    brain['brain'].preprocessor(data)
                    brain['brain'].doTrade(data,code)

            brain['brain'].reportBrainOperation()
			
    def getData(self, market, item, domain, seqLen):
        pass

