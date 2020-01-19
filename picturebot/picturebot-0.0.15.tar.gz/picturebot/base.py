import sys
import os
import json
import shutil
import subprocess
import click
import picturebot as pb
from picturebot.helper import Helper as helper
import picturebot.poco as poco
import generalutils.guard as grd
import picturebot.workspace as ws
from picturebot.directory import Directory as directory
import re

class Base():
    def __init__(self, ctx, index):
        '''Base class constructor
        
        Args:
            ctx (object): Global context object
            index (int): Index of the selected workspace configuration
        '''

        self.ctx = ctx
        self.index = int(index)
        self.basename = ""
        self.cwd = ""
        self.shoot = ""
    
    def Backup(self, path):
        '''Backup a single picture in the backup flow
        
        Args:
            path (string): Path to the picture
        '''

        # Check whether the script is runned from the base flow directory
        self.__PathToBaseFlow()
        # Copy a single file in the backup flow
        self._CopyFile(path)

    def MassBackup(self):
        '''Backup all the pictures within the base flow in the backup flow'''

        # Check whether the script is runned from the base flow directory
        self.__PathToBaseFlow()
        # Copy all pictures within the base flow in the backup flow
        self.__CopyFilesFromBaseToBackup()

    def Rename(self, index, path):
        '''Rename a file accordingly to the shootname (<name>_<data>_<index>)
        
        Args:
            index (string): Picture index number
            path (string): Path to the picture
        '''

        # Check whether the script is runned from the base flow directory
        self.__PathToBaseFlow()
        shoot = self.NewShootName()
        self._r(path,shoot, index)

    def MassRename(self):
        '''Rename all the files within a flow'''

        # Check whether the script is runned from the base flow directory
        self.__PathToBaseFlow()
        self.__Rename()
    
    def Convert(self, path, quality):
        '''Convert a raw picture to a jpg format and store it within the preview flow
        
        Args:
            path (string): Path of the picture
            quality (string): Quality of the converted picture
        '''

        # Check whether the script is runned from the base flow directory
        self.__PathToBaseFlow()
        self.__ConvertImage(path, quality)

    def __ConvertImage(self, path, quality):
        '''Convert a raw picture to a jpg format and store it within the preview flow
        
        Args:
            path (string): Path of the picture
            quality (string): Quality of the converted picture
        '''

        # Obtain the basename of the path
        basename = os.path.basename(path)
        # Obtain the basename without an extension
        basenameWithoutExtension = basename.split('.')[0]
        # Create the output storage path
        output = os.path.join(self.ctx.Config[self.index].Workspace, self.shoot, self.ctx.Config[self.index].Preview, f"{basenameWithoutExtension}.jpg")
        
        # magick convert "<path>" -quality <quality>% -verbose "<outputPath>"
        command = f"magick convert \"{path}\" -quality {quality}% -verbose \"{output}\""

        # Execute command
        os.system(command)

    def __PathToBaseFlow(self):
        '''Check whether the script is runned within the baseflow directory'''

        # Get the current working directory of where the script is executed
        self.cwd = os.getcwd()
        self.shoot = re.search('(\w+\s+\d+-\d+-\d+)', self.cwd).group(0)

        # Check whether the current working directory exists
        grd.Filesystem.PathExist(self.cwd)

        # Obtain the name of the base flow of the current shoot
        self.basename = os.path.basename(self.cwd)

        # Obtain the path to the base flow project
        if grd.Filesystem.IsPathCwd(self.basename, self.cwd):
            pathToBaseflowProject = helper.FullFilePath(self.ctx.Config[self.index].Workspace, self.shoot, self.basename)
            
            # Check whether the the path to the base flow project exists
            grd.Filesystem.PathExist(pathToBaseflowProject)
            # Check whether you're within the backup flow directory
            grd.Filesystem.PathCwdExists(pathToBaseflowProject, self.cwd, True)
        
    def __CopyFilesFromBaseToBackup(self):
        '''Copy all files from the base flow to the backup flow'''

        pictures = os.listdir(self.cwd)

        counter = 0

        for picture in pictures:
            pathToBackupFlow = self._CopyFile(picture)

            click.echo(f'Copying: {picture} -> {pathToBackupFlow} [{counter + 1}/{len(pictures)}]')

            counter += 1

        click.echo(f"Copied files: {counter}")

    def _CopyFile(self, path):
        '''Copy a file to the backup flow
        
        Args:
            path (string): Path to the picture
        
        Returns:
            (string): Backup flow path
        '''

        # Obtain the filename from a specified path
        filename = os.path.basename(path)

        # Obtain the path to the baseflow directory
        pathToBaseflow = helper.FullFilePath(self.ctx.Config[self.index].Workspace, self.shoot, self.basename)
        # Check whether the baseflow directory exists
        grd.Filesystem.PathExist(pathToBaseflow)

        # Obtain the path the source picture within the baseflow directory
        pathToPictureSource = helper.FullFilePath(pathToBaseflow, filename)
        # Check whether the source picture path exists
        grd.Filesystem.PathExist(pathToPictureSource)

        # Obtain the path to the backupflow directory
        pathToBackupFlow = helper.FullFilePath(self.ctx.Config[self.index].Workspace, self.shoot, self.ctx.Config[self.index].Backup)
        # Check whether the backupflow directory exists
        grd.Filesystem.PathExist(pathToBackupFlow)

        # Obtain the full path name to the picture's destition path
        pathToPictureDestination = helper.FullFilePath(pathToBackupFlow, filename)
        
        # Copying picture from source to destination including the metadata
        shutil.copy2(pathToPictureSource, pathToPictureDestination)

        # Check whether the file is successfully copied
        grd.Filesystem.PathExist(pathToPictureDestination)

        return pathToBackupFlow

    def __Rename(self):
        '''Rename the picture'''

        counter = 0

        shoot = self.NewShootName()

        # Obtain the original picture name within a flow directory
        pictures = os.listdir(self.cwd)
        # sort by date
        pictures.sort(key=os.path.getctime)

        count = len(pictures)

        # Loop over every picture withing the flow directory
        for index, picture in enumerate(pictures, 1):
            self.__RenamePicture(picture, shoot, index)
        click.echo(f"Renamed files: {count}")

    def NewShootName(self):
        '''Create the shootname
        
        Returns:
            (string): Returns the formated shootname
        '''

        newShoot = ''

        # Loop over every word of the flow name directory
        for i in self.shoot.split(' '):
            # Append the individual words to an '_'
            newShoot += f'{i}_'
        return newShoot

    def _RenamePicture(self, path, shoot, index):
        '''Rename a picture
        
        Args:
            path (string): Path to the picture
            shoot (string): Shootname of the picture
            index (string): Picture index number
        '''

        # Get the extension of the original picture
        extension = path.split('.')[1]

        # Get absolute path to the picture
        pathToPicture = os.path.join(self.cwd, path)

        # Check whether the absolute path to the picture is existing
        grd.Filesystem.PathExist(path)

        # Get the new name for the picture
        newName = f"{shoot}{str(index).zfill(5)}.{extension}"

        # Obtain the absolute path to the new picture name
        pathToNewPicture = os.path.join(self.cwd, newName)
        
        # Only rename the changed files
        if not pathToNewPicture == pathToPicture:
            # Rename the picture file
            os.rename(pathToPicture, pathToNewPicture)

            # Check whether the new picture file exists after renaming
            grd.Filesystem.PathExist(pathToNewPicture)
