# -*- coding: ISO-8859-1 -*-
#-------------------------------------------------------------------------------
# $Id$
#
# Copyright 2017 Jean-Luc PLOIX
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------

import sys, os
import unittest
from io import StringIO
if not os.getcwd() in sys.path:
    sys.path.append(os.getcwd())
    
from nntoolbox.timetb import secToStr, splitsecs, second2str, sec2str
from nntoolbox.sqlite_numpy import getSelectQuery
from nntoolbox.modelutils import TransferModel, TransferJacobian
from nntoolbox.filetoolbox import arg_file_parse
from nntoolbox.utils import Namespace
    
class Test_utils(unittest.TestCase):
    
    def test_Namespace(self):
        dico = {"a":1, "b":2}
        r1 = Namespace(**dico)
        self.assertEqual(r1.a, 1)
        self.assertEqual(r1.b, 2)

class Test_configparsertoolbox(unittest.TestCase):
    pass

class Test_excelutils(unittest.TestCase):
    pass

class Test_filetoolbox(unittest.TestCase):
    
    def test_arg_file_parse(self):
        pass

class Test_modelutils(unittest.TestCase):
    
    def test_TransferModel(self):
        pass
    
    def test_TransferJacobian(self):
        pass

class Test_timetb(unittest.TestCase):
     
    def test_secToStr(self):
        r1 = secToStr(1584)
        self.assertEqual(r1, '26 minutes 24.000 secondes')
        r2 = secToStr(1584, 0)
        self.assertEqual(r2, '26 minutes 24 secondes')
        r3 = secToStr(21584, 0)
        self.assertEqual(r3, '5 heures 59 minutes 44 secondes')
         
    def test_splitsecs(self):
        r1 = splitsecs(21584)
        self.assertEqual(r1,  (44, 59, 5, 0))
         
    def test_second2str(self):
        r1 = second2str(21584)
        self.assertEqual(r1, '05:59:44.00')
        r1 = second2str(2221584)
        self.assertEqual(r1, '617:06:24.00')
     
    def test_sec2str(self):
        r1 = sec2str(21584)
        self.assertEqual(r1, '5 h. 59 min. 44 sec.')

class Test_sqlite_numpy(unittest.TestCase):
    
    def test_getSelectQuery(self):
#         titles, tablename, indexval=None, indexname="", comp=0, 
#         orderfield="", reverse=False, maxrec=-1, extraselect="", nullfields=[]
        res = getSelectQuery(["C1", "C2"], "tabletest")
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1")
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE C1 = a')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1", comp=1)
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE C1 >= a')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1", comp=-1)
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE C1 <= a')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1", comp=2)
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE C1 > a')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1", comp=-2)
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE C1 < a')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1", comp=3)
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE abs(C1) > a')
        res = getSelectQuery(["C1", "C2"], "tabletest", indexval="a", indexname="C1", comp=-3)
        self.assertEqual(res, 'SELECT C1, C2 FROM tabletest WHERE abs(C1) < a')
        
def runtest():
    unittest.main()

if __name__ == "__main__":
    runtest()
    
