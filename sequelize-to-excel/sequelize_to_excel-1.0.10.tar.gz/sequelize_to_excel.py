# -*- coding: utf-8 -*-
#
# MIT License
# Copyright (c) 2020 Darshan Bharat
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import  re
import json;
import pandas as pd;
import logging
from pandas.io.json import json_normalize

class SequelizeToExcel(object):

    def __init__(self,node_model_filename=None):
        self.node_model_filename = node_model_filename

    """ 
        This module will help you extract info from your standard 
        sequelize file to excel format , consisiting column name , field name ,
        auto increment etc 
    """
    def extract_and_export(self,export_type="excel"):
        """ 
            This function accepts filename , removes noise and 
            maps field to columns of excel

            Args:
                filename : command line input for file name
            
            Returns :
                Saves excel at the same location
        """
        try:
            # request for filename
            if self.node_model_filename == None:
                filename = input("pls enter the filename w/o extn :-> ")
            else:
                filename = self.node_model_filename
            # Reads the file
            f = open(filename+".js","r")

            txt = f.read()

            # uses regex to clear noise
            x = re.sub("^\/*.*\n","",txt)
            x2 = re.sub("^module.*\n..*',","[",x.strip())
            x3 = x2.replace(");","")
            x3 = x3.replace("};","]")
            x3 = re.sub(r'DataTypes.',r'',x3)
            x3 = re.sub("'",r'',x3)
            x3 = re.sub(r'(\w+)',r'"\1"',x3)
            x3 = x3.replace(" ","")

            jsonObj = json.loads(x3)

            listRows = []
            # defines excel header and maps value
            lstColumnHeader = ["name","type","allowNull","primaryKey","autoIncrement","field","defaultValue","references.model","references.key","tableName","version"]
            for (k,v) in jsonObj[0].items():
                listColumns = []
                listColumns.append(k)
                listColumns.append(v.get("type","na"))
                listColumns.append(v.get("allowNull","na"))
                listColumns.append(v.get("primaryKey","na"))
                listColumns.append(v.get("autoIncrement","na"))
                listColumns.append(v.get("field","na"))
                listColumns.append(v.get("defaultValue","na"))
                #listColumns.append(v.get("references","na"))
                if v.get("references","na") != "na":
                    listColumns.append(v.get("references").get("model","na"))
                    listColumns.append(v.get("references").get("key","na"))
                else:
                    listColumns.append("na")
                    listColumns.append("na")
                listColumns.append(jsonObj[1].get("tableName","na"))
                listColumns.append(jsonObj[1].get("version","na"))
                listRows.append(listColumns)

            if export_type == "excel":
                df = pd.DataFrame(listRows,columns=lstColumnHeader)
                df.to_excel(filename+".xlsx")
            else
                return listRows
        except FileNotFoundError as fe:
            logging.error(" File name passed is not present at the location ",stack_info=True)
        except ValueError as ve:
            logging.error(" attributes in the model are unknown ",stack_info=True)
        except Exception as e:
            logging.error(e)
