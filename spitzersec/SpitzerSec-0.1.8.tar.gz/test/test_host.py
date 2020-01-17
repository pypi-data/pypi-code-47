import unittest
import sys
import io
sys.path.append('../')
from Spitzer import host

class test_search(unittest.TestCase): 


    def test_extract_nmap(self):
        nmap = {
            'scan':{
                '192.168.1.0':{
                    'tcp':[21,22,25]
                },
                '192.168.1.2':{
                    'tcp':[12,54]
                }
            }
        }

        expected = {
            '192.168.1.0':[21,22,25],
            '192.168.1.2':[12,54]
        }

        result = host.extract_hosts_nmap(nmap)
        self.assertDictEqual(result, expected)

    def test_extract_xml(self):
        nmap = {
            'nmaprun':{
                'host':[{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'21'}}
                    },{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'22'}}
                    },{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'25'}}
                    },{
                        'address':{'addr':'192.168.1.2'},
                        'ports':{'port':{'portid':'12'}}
                    },{
                        'address':{'addr':'192.168.1.2'},
                        'ports':{'port':{'portid':'54'}}
                    }]
            }
        }

        expected = {
            '192.168.1.0':['21','22','25'],
            '192.168.1.2':['12','54']
        }

        result = host.extract_hosts_xml(nmap)
        self.assertDictEqual(result, expected)

    def test_merge(self):
        nmap1 = {
            'nmaprun':{
                'host':[{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'21'}}
                    },{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'25'}}
                    },{
                        'address':{'addr':'192.168.1.2'},
                        'ports':{'port':{'portid':'12'}}
                    }]
            }
        }

        nmap2 = {
            'nmaprun':{
                'host':[{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'22'}}
                    },{
                        'address':{'addr':'192.168.1.0'},
                        'ports':{'port':{'portid':'25'}}
                    },{
                        'address':{'addr':'192.168.1.2'},
                        'ports':{'port':{'portid':'54'}}
                    }]
            }
        }

        expected = {
            '192.168.1.0':['21','22','25'],
            '192.168.1.2':['12','54']
        }

        result = host.merge(nmap1, nmap2)
        self.assertDictEqual(result, expected)

if __name__ == '__main__':    
    unittest.main()