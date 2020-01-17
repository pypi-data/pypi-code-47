# -*- coding: ISO-8859-15 -*-
#-------------------------------------------------------------------------------
# $Id$
#
# Copyright 2018 Jean-Luc PLOIX
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
#from _modelcontainer import lst
'''
Created on 25 fvr. 2018

@author: jeanluc
'''

import os, sys
from pandas import DataFrame, read_excel, ExcelFile
from ._excel import ExcelCsv  #, Excel, ExcelXP
from .excelsource import dataiterator, monalExcelError
from metaphor.nntoolbox.utils import splitVartUnit, floatEx, concatenateList


class dataReadingError(Exception):
    pass

class modelDataFrame(object):
    '''Frame of data for statistical model training.
    '''

    def __init__(self, dataframe=None, data=None, index=None, columns=None, dtype=None, copy=False):  #
        '''Constructor
         - dataframe : optional pandas DataFrame. If present, it is copied in the modelDataFrame instance, and all other parameters are discarded.
         - data
         - index
         - columns
         - dtype
         - copy
        '''
        super(modelDataFrame, self).__init__()
        self.dtypes = None
        self._datagroups = None
        self._datacounts = None
        self._units = None
        if dataframe is None:
            self._frame = DataFrame(data, index, columns, dtype, copy)
        else:
            self._frame = dataframe.copy()
    
    def copy(self):
        result = modelDataFrame(self._frame)
        result._datagroups = self._datagroups
        result._datacounts = self._datacounts
        result._units = self._units
        return result
    
    def __getattr__(self, attrname):
        if hasattr(self._frame, attrname):
            return self._frame.__getattr__(attrname)
        else:
            try:
                return self.__getattribute__(attrname)
            except:
                return None
    
    def __repr__(self):
        return self._frame.__repr__()

    def __str__(self):
        return self._frame.__str__()
    
    def gettitles(self, withindex=True):
        lst = list(self.columns)
        if withindex:
            lst = [self.index.name] + lst
        return lst
    
    def iterData(self, titlesFirst=True, withindex=True):
        if titlesFirst:
            yield self.gettitles(withindex)
        for indstr, row in self._frame.iterrows():
            lst = list(row)
            if withindex:
                lst = [indstr] + lst
            yield lst
    
    def indexesOf(self, groupname):
        if not groupname in self.dataGroups:
            return []
        index = self.dataGroups.index(groupname)
        return self.dataFields[index]
    
    def fieldsOf(self, groupname):
        if not groupname in self.dataGroups:
            return []
        index = self.dataGroups.index(groupname)
        lst = self.dataFields[index]
        res = [self.columns[i] for i in lst]
        return res  
    
    def varDescriptor(self):
        outlst = []
        for grp in res.dataGroups:
            outlst.append(grp)
            lst = res.groupcolumns(grp)
            for col in lst:
                typ = res.dtypes[col]
                unit = res.units[col]
                st = "\t{0}\t{1}\t{2}".format(col, unit, typ)
                outlst.append(st)
        return "\n".join(outlst)
    
    def typesAnalysis(self):
        self.dtypes = {}
        newcol = {}
        self._units = {}
        for col in self._frame.columns:
            ncol, unitcol = splitVartUnit(col)
            fcol = self._frame.get(col)
            if all([isinstance(val, (float, int, bool)) for val in fcol]):
                self.dtypes[ncol] = float
            elif any([isinstance(val, str) for val in fcol]):
                self.dtypes[ncol] = str
            else:
                self.dtypes[ncol] = fcol.dtype
            newcol[col] = ncol
            self._units[ncol] = unitcol
        self._frame.rename(columns=newcol, copy=False, inplace=True)
        return self.dtypes
    
    def groupcolumns(self, key, byName=True):
        try:
            ind = self._datagroups.index(key)
        except:
            return []
            #raise IndexError("Bad index in group list")
        decal = sum(self._datacounts[:ind])
        iterator = range(decal, self._datacounts[ind] + decal)
        if byName:
            return [self._frame.columns[index] for index in iterator]
        else:
            return list(iterator)
    
    @property
    def units(self):
        return self._units
                
    @property
    def dataGroups(self):
        return self._datagroups
                
    @property
    def dataFields(self):
        return self._datafields
                
    @property
    def dataCounts(self):
        return self._datacounts
    
    def compactDataFields(self, indexdict=None):
        ind = 0
        res = []
        for ffs in self._datafields:
            resloc = []
            for ff in ffs:
                if indexdict is not None:
                    indexdict[ind] = ff
                resloc.append(ind)
                ind += 1
            res.append(resloc)
        self._datafields = res
        return indexdict
                
def get_modelDataframe(filename, datarange="", datafields=[], 
        datagroups=[], sheetname=None, filetype='', indexfield=-1, 
        drop=False, withindexdict=False):
    """Return a Pandas DataFrame from an Excel file.
    datarange and sheetname are mutually ecxclusives.
    
    First line carry the titles.
    
    If datarange is empty and sheetname is None, return a list of pandas DataFrame,
    one for each worksheet.
    
    File designed by filename must be an Excel or csv-like file.
    """
    indexdict = {}
    titlelist = []
    if datafields is not None and (len(datafields) > 1) and not isinstance(datafields[0], list):
        if len(datafields) == 2:
            datafields = [[datafields[0]], [datafields[1]]]
            datagroups = ['inputs', 'outputs']
        elif datafields is not None and len(datagroups) == 2:
            if datagroups[-1] == 'outputs':
                datafields = [datafields[0:-1], [datafields[-1]]]  
            else:
                raise IndexError ("index error in 'datafields' analysis")                            
        elif datafields is not None and len(datafields) >= 3 and len(datagroups) in [0, 3]:
            datafields = [[datafields[0]], datafields[1:-1], [datafields[-1]]] 
            datagroups =  ['identifiers', 'inputs', 'outputs']          
        else:
            datafields = [[datafields[0]], [], [datafields[1]]]
            datagroups = ['inputs', 'outputs']  
    if (datagroups is not None) and ('identifiers' in datagroups):
        indexfield = datagroups.index('identifiers')
            #datafields[datagroups.index('identifiers')][0]
    if not filetype:
        try:
            filetype = os.path.splitext(filename)[1][1:]
        except: pass
    dataframe = None
    if filetype in ['csv', 'txt']:
        if len(datafields) and isinstance(datafields[0], list):
            allfields = [val for ll in datafields for val in ll]
        else:
            allfields = datafields
        with ExcelCsv(filename, load=True) as xl:
            iterator = xl.iterData(titlesfirst=True, datafmt=allfields)
            for indrow, row in enumerate(iterator):
                if not indrow:
                    titlelist = list(row)
                    dataframe = modelDataFrame(columns=row)
                else:
                    rowN = []
                    for val in row:
                        try:
                            val = floatEx(val, True)
                        except: pass
                        rowN.append(val)
                    dataframe._frame.loc[indrow-1] = rowN
    elif datarange:
        datafmt = concatenateList(datafields)
        emptydata = [None for _ in datafmt]
#         if len(datafields) and isinstance(datafields[0], list):
#             lst = [val for ll in datafields for val in ll]
#             datafmt = lst  
#         else:
#             datafmt = datafields  
        try:
            iterdata = dataiterator(filename, filetype, datarange, datafmt=datafmt)
        except Exception as err:
            raise monalExcelError("Unable to find data in file|range: {}|{}".format(filename, datarange))
        try:
            for ind, row in enumerate(iterdata):
                if row == emptydata:
                    raise dataReadingError("Empty data in line {}".format(ind))
                elif not ind:
                    titlelist = list(row)
                    dataframe = modelDataFrame(columns=row)
                else:
                    dataframe._frame.loc[ind-1] = row
        except dataReadingError:
            raise
        except ValueError as err:
            raise monalExcelError("Unable to find data in file|range: {}|{}".format(filename, datarange))

    else:
        efile = ExcelFile(filename)
        dataframe = read_excel(efile, sheetname=sheetname)
    if isinstance(dataframe, dict):
        for key, df in dataframe.items():
            if df.shape[0] > indexfield >= 0:
                indexname = df.columns[indexfield]
                df.set_index(indexname, inplace=True, drop=drop)
            dataframe[key] = modelDataFrame(df)         
    else:
        pandasframe = dataframe._frame
        if pandasframe.shape[1] > indexfield >= 0:
            indexname = pandasframe.columns[indexfield]
            pandasframe.set_index(indexname, inplace=True, drop=drop)
    if dataframe._frame.index.name is None:
        dataframe._frame.index.name = "ID"
    if dataframe is not None and datagroups is not None:
        if drop:
            dataframe._datagroups = datagroups[1:]  
            dataframe._datafields = datafields[1:]            
        else:
            dataframe._datagroups = datagroups  
            dataframe._datafields = datafields
        indexdict = dataframe.compactDataFields(indexdict)
        if len(datafields) == len(datagroups):
            dataframe._datacounts = [len(val) for val in dataframe._datafields]
    if dataframe is not None:
        dataframe.typesAnalysis()
    if withindexdict:
        return dataframe, titlelist, indexdict
    return dataframe, titlelist
        
if __name__ == "__main__":
    
    filename = "~/docker/data/BJMA270T30LVISC14SM.xlsx"
    datarange = "DATA"
    datafmt = [[0],[1,5,6],[18]]
    datagrp = ['identifiers', 'inputs', 'outputs']
    
    print(filename)
    res, _ = get_modelDataframe(filename, datarange, datafields=datafmt, datagroups=datagrp) 
    print(res.varDescriptor())            
    print(res.shape)   
    
    filename = "~/docker/data/BJMA270T30LVISC14SM.xlsx"
    datarange = "DATA"
    datafmt = [[1,5,6],[18]]
    datagrp = ['inputs', 'outputs']
    
    print(filename)
    res, _ = get_modelDataframe(filename, datarange, datafields=datafmt, datagroups=datagrp) 
    print(res.varDescriptor())            
    print(res.shape)   
    
    filename = "~/docker/data/BJMA270T30LVISC14SM.xlsx"
    datarange = "DATA"
    datafmt = [1,5,6,18]
    datagrp = ['inputs', 'outputs']
    
    print(filename)
    res, _ = get_modelDataframe(filename, datarange, datafields=datafmt, datagroups=datagrp) 
    print(res.varDescriptor())            
    print(res.shape)   
    
    filename = "~/docker/data/BJMA244_Test25_5SM.xlsx"
    datarange = "FULLDATA"
    datagrp = ['identifiers', 'inputs', 'outputs']
    datafmt = [0,1,5,6,7,8,9,10]
    
    print(filename)
    res, _ = get_modelDataframe(filename, datarange, datafields=datafmt, datagroups=datagrp) 
    print(res.varDescriptor())            
    print(res.shape)   
    
    filename = "/Users/jeanluc/docker/data/BJMA244_Test25_5SM_data.csv"
    datafmt = [1,2,6,7,8,9,10,11]
    
    print(filename)
    res, _ = get_modelDataframe(filename, datarange, datafields=datafmt, datagroups=datagrp) 
    print(res.varDescriptor())            
    print(res.shape)   
    
    filename = "/Users/jeanluc/docker/data/BJMA244_Test25_5SM_test.txt"
    datafmt = [2,3,7,8,9,10,11,12]
    
    print(filename)
    res, _ = get_modelDataframe(filename, datarange, datafields=datafmt, datagroups=datagrp) 
    print(res.varDescriptor())            
    print(res.shape)   
    
        