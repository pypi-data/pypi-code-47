import os
import sys
import generalutils.guard as grd

class Directory:
    '''Guard class containing static methods to easily check filesystem functions'''
    
    @staticmethod
    def CreateFolder(path):
        '''Create And test whether the folder is successfully created
        
        Args:
            path (string): Folder that is going to get created
        '''

        # If folder doesn't exists create a new one
        if not grd.Filesystem.IsPath(path):
            # Create folder
            os.mkdir(path)

            # Check whether creation was successfull
            grd.Filesystem.PathExist(path)