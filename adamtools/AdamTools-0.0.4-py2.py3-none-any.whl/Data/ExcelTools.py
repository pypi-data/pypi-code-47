import os
import xlrd


class ExcelFiles:
    """
    Calling this class automatically loads all the files in the target folder named source
    """
    def __init__(self, source):
        self.source = source
        self.makeDataFileList()
        #self.makeFieldList()
    
    def makeDataFileList(self):
        """
        Make a list of all files in the source directory
        so that each file has its path appended to it.
        Store that list in datafiles
        """
        self.datafiles = []
        self.sourceFolder = os.walk(self.source)
        for f in self.sourceFolder:
            filelist = f[2]
            for fl in filelist:
                loc = self.source + '/' + str(fl)
                self.datafiles.append(loc)
    
    def makeFieldList(self):
        self.list_of_fields = []
        for d in self.datafiles:
            try:
                self.wb = xlrd.open_workbook(d)
                #Get the first sheet by index
                self.sh = self.wb.sheet_by_index(0)
                try:
                    for f in self.sh.row_values(0):
                        self.list_of_fields.append(f)
                except Exception as exc:
                    sys.exit( "make field list failed; %s" % str(exc) ) # give a error message
                    print('error', f)
            except Exception as exc:
                sys.exit( "make field list failed; %s" % str(exc) ) # give a error message
                print('error', d)
        self.list_of_fields = set(self.list_of_fields)
        self.list_of_fields = list(self.list_of_fields)
        self.list_of_fields.sort()
    
    def makeRowDicts(self):
        self.rowData = []
        for d in self.datafiles:
            try:
                self.wb = xlrd.open_workbook(d)
                #Get the first sheet by index
                self.sheet = self.wb.sheet_by_index(0)
                self.numRows = self.sheet.nrows
                for i in range(self.numRows):
                    if i > 0:
                        keys = self.sheet.row_values(0)
                        values = self.sheet.row_values(i)
                        dictionary = dict(list(zip(keys, values)))
                        self.rowData.append(dictionary)
            except Exception as exc:
                print(( "make row dicts failed; %s" % str(exc) )) # give a error message
                print('error', d)
    
    def makeSheet(self, fileName):
        self.wb = xlrd.open_workbook(fileName)
        #Get the first sheet by index
        self.sheet = self.wb.sheet_by_index(0)