import unittest
import sys
import io
sys.path.append('../')
from Spitzer.searchsploit import find

class test_search(unittest.TestCase): 

    nmap = {
        '192.168.1.0':{
            'tcp':{
                '21':{
                    'product':'ftpd', #one sploit
                    'version': '2.3.4'
                },
                '22':{
                    'product':'openssh', #three sploits
                    'version':'2.3'
                },
                '23':{
                    'product':'smpt', #no sploits
                    'version':'42'
                },
                '25':{
                    'product':'psftpd', #two sploits
                    'version':''
                },
                '30':{
                    'product':'', #no sploits (duh)
                    'version':''
                }
            }
        }
    }


    def test_search(self):
        #first, capture the stdout
        output = io.StringIO()
        sys.stdout = output
        find('192.168.1.0', self.nmap)
        sys.stdout = sys.__stdout__
        #expected output:
        expected = [
        '[-] Found 2 exploits for ftpd 2.3.4 on 192.168.1.0',
        '[-] Found 4 exploits for openssh 2.3 on 192.168.1.0',
        '[-] Found 3 exploits for psftpd  on 192.168.1.0'
        ]
        output = output.getvalue()
        self.assertTrue(len(output.splitlines()) == 3)
        
        for line in expected:
            if line not in output:
                raise RuntimeError

if __name__ == '__main__':    
    unittest.main()