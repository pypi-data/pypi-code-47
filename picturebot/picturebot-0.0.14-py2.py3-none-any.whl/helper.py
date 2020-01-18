import os
import sys
import hashlib
import generalutils.guard as grd
import picturebot.poco as poco

class Helper:
    '''Static class containing helper methods'''

    @staticmethod
    def FullFilePath(*items):
        '''Get the full path to a folder or directory
        Args:
            items (list): List of folders and subfolders
        
        Returns:
            (string) Full file name
        '''

        # Get the current working directory
        path = os.path.dirname(os.path.abspath(__file__))

        # Loop over every folder and subfolders
        for item in items:
            path = os.path.join(path, item)

        return path

    @staticmethod
    def HashFileMd5(file):
        '''Create a md5 hash from a file

        Args:
            file (file): File where a hash is created from
        Returns:
            (string) Md5 hash
        '''
        bufSize = 32768 # Read file in 32kb chunks
        md5 = hashlib.md5()

        with open(file, 'rb') as f:
            while True:
                data = f.read(bufSize)

                if not data:
                    break

                md5.update(data)
                
            return md5.hexdigest()

    @staticmethod
    def Context(context):
        return poco.Context(context.obj['config'], context.obj['workspaceObj'])
