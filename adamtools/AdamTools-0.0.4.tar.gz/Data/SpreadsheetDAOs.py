import os as os
import sys
import xlrd as xlrd
from openpyxl import Workbook


class ExcelFiles:
    """
	Base class for loading excel data
	Calling this class automatically loads all the files in the target folder.
	The source var passed in defines the relevant folder.
	This is a generic base class to be used in many programs
	"""

    def __init__( self, source, quiet=False ):
        """
		@param source string The location of the folder containing files
		@param quiet string Whether to print messages at every step
		"""
        self.quiet = quiet
        self.source = source
        self.makeDataFileList()

    # self.makeFieldList()

    def makeDataFileList( self ):
        """
        Make a list of all files in the source directory
        so that each file has its path appended to it.
        Store that list in datafiles
        """

        self.datafiles = [ ]
        self.sourceFolder = os.walk( self.source )
        for f in self.sourceFolder:
            filelist = f[ 2 ]
            for fl in filelist:
                loc = self.source + '/' + str( fl )
                self.datafiles.append( loc )

    def makeFieldList( self ):
        """
		Store an alphabetically sorted list of all the fields in self.list_of_fields.
		Also makes a list of with unique fields in self.list_of_unique_fields
		self.field_sources list Contains tuples of the field name and datafile is is from
		"""
        self.list_of_fields = [ ]
        self.field_sources = [ ]
        for d in self.datafiles:
            try:
                self.wb = xlrd.open_workbook( d )
                # Get the first sheet by index
                self.sh = self.wb.sheet_by_index( 0 )
                try:
                    for f in self.sh.row_values( 0 ):
                        self.list_of_fields.append( f )
                        self.field_sources.append( (f, d) )
                except:
                    print( ('error', f) )
            except:
                print( ('error', d) )
        self.list_of_unique_fields = set( self.list_of_fields )
        self.list_of_unique_fields = list( self.list_of_fields )
        self.list_of_fields.sort()
        self.list_of_unique_fields.sort()

    def makeRowDicts( self ):
        """
		Makes a dictionary from the data of each row with the first row's values as keys
		"""
        self.rowData = [ ]
        for d in self.datafiles:
            try:
                self.wb = xlrd.open_workbook( d )
                # Get the first sheet by index
                self.sheet = self.wb.sheet_by_index( 0 )
                self.numRows = self.sheet.nrows
                for i in range( self.numRows ):
                    if i > 0:
                        keys = self.sheet.row_values( 0 )
                        values = self.sheet.row_values( i )
                        dictionary = dict( list( zip( keys, values ) ) )
                        self.rowData.append( dictionary )
                if self.quiet == False:
                    print( ('Loaded %s' % d) )
            except:
                print( ('error', d) )

    def makeSheet( self, fileName ):
        self.wb = xlrd.open_workbook( fileName )
        # Get the first sheet by index
        self.sheet = self.wb.sheet_by_index( 0 )


class ExcelWriter:
    """
	Makes an excel file out of data held in list of dictionaries
	"""

    def __init__( self, dataList, rowHeaderKey, valuesKey ):
        """
		@param dataList list The list of dictionaries
		@param rowHeaderKey string This should be a string corresponding to the name of the dictionary key which holds the value to be inserted in row0
		@param valuesKey string This should be a string corresponding to the name of the dictionary key which holds the list of values
		"""
        self.wb = Workbook()
        self.ws = self.wb.get_active_sheet()
        self.data = dataList
        self.rowHeaderKey = rowHeaderKey
        self.valuesKey = valuesKey

    def write( self ):
        numCol = len( self.data )
        i = 0
        for p in self.data:
            self.cellFiller( 0, i, p[ self.rowHeaderKey ] )
            row_count = 1
            for f in p[ self.valuesKey ]:
                self.cellFiller( row_count, i, f )
                row_count = row_count + 1
            i = i + 1

    def cellFiller( self, rw, col, data ):
        cell = ws.cell( row=rw, column=col )
        cell.value = data

    def save( self, sourceDir, fileName ):
        fn = sourceDir + fileName
        self.wb.save( fn )
