import os
import pathlib
import pandas as pd
import xlrd

class Reader:
    """ It reads a set of excel files in a directory and returns a dataframe with all tables appended

    Attributes:
        directory_path: directory where the excel files are located

    Requirements: 
        (1) The headers of all files have to be in the first row of the table; (2) The possible file extensions are: '.xls', '.xlsx', '.csv', '.xlsm', '.xlsb'
    """
    
    # this is a class variable, in order to use it in the code, prefix it with .self.
    _xl_extensions_list = ['.xls', '.xlsx', '.csv', '.xlsm', '.xlsb']

    def __init__(self, directory_path):
        self.directory_path = directory_path

    def list_excel_files(self):
        """List of excel files in a directory

        Returns:
            list: list of all file names
        """

        # Checks if directory/file exists
        if os.path.exists(self.directory_path) == False:
            return 'Directory could not be found'

        try:
            all_files = os.listdir(self.directory_path)
            xl_files = [f for f in all_files if pathlib.Path(f).suffix in Reader._xl_extensions_list]
        except Exception as e:
            return ('Something unexpected happened - %s' % e) 

        return xl_files


    def get_worksheets(self, file_names):
        """Get all corresponding worksheets of the files of interest

        Parameters:
            file_name (list): list with the name of all files to get their worksheet names

        Returns:
            dict: the keys are the file names and the values are a list of all worksheets in the corresponding file
        """

        # checks if all files exist
        for file in file_names:
            if os.path.exists(self.directory_path + '\\' + file) == False:
                return ('File %s could not be found' % file)

        path_file_names = [self.directory_path + "\\" + file for file in file_names]
        file_sheets = []
        file_sheets_list = []

        try:
            for file in path_file_names:
                book = xlrd.open_workbook(file)
                for sheet in book.sheets():
                    file_sheets.append(sheet.name)

                file_sheets_list.append(file_sheets.copy())
                file_sheets.clear()

            result_dict = dict(zip(file_names, file_sheets_list))
        except Exception as e:
            return ('Something unexpected happened when dealing with the file %s - %s' % (file, e)) 

        return result_dict



    def read_files(self, file_names): 
        """Read all tables and append them to each other, returning one single talbe with the data of all specified files

        Parameters:
            file_names (dict): the keys are only the file names (not the full path) and the values are the worksheet names (only one value is acceptable, not a list)

        Returns:
            dataframe: all data appended to one single table
        """

        # TO DO: run a check to see if worksheet exists, now it's throwing an error when this happens, i can be almost in the last file. 

        if isinstance(file_names, dict) == False:
            return 'The parameter file_names must be a dictionary'

        for key, val in file_names.items():
            if os.path.exists(self.directory_path + '\\' + key) == False:
                return ('The file %s could not be found' % key)
            if isinstance(val, str) == False:
                return 'The values in the dictionary must be strings'

        try:
            df = pd.DataFrame()

            for file_name, worksheet_name in file_names.items():
                data = pd.read_excel(self.directory_path + "\\" + file_name, worksheet_name)
                data['file_name'] = file_name
                df = df.append(data)

            return df
        except Exception as e:
            return ('Something unexpected happened when dealing with the file %s - %s' % (file_name, e)) 


