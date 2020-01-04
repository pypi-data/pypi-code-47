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
    def __init__(self, ctx):
        self.ctx = ctx
        self.basename = ""
        self.cwd = ""
        self.shoot = ""
    
    def Backup(self, path):
        self.__PathToBaseFlow()
        self._CopyFile(path)

    def MassBackup(self):
        self.__PathToBaseFlow()
        self.__CopyFilesFromBaseToBackup()

    def Rename(self, index, path):
        self.__PathToBaseFlow()
        shoot = self.NewShootName()
        self._r(path,shoot, index)

    def MassRename(self):
        self.__PathToBaseFlow()
        self.__Rename()
    
    def Convert(self, path, quality):
        self.__PathToBaseFlow()
        self.__ConvertImage(path, quality)

    def __ConvertImage(self, path, quality):
        basename = os.path.basename(path)
        basenameWithoutExtension = basename.split('.')[0]
        output = os.path.join(self.ctx.Config.Workspace, self.shoot, self.ctx.Config.Preview, f"{basenameWithoutExtension}.jpg")
        
        command = f"magick convert \"{path}\" -quality {quality}% -verbose \"{output}\""
        os.system(command)

    def __PathToBaseFlow(self):
        # Get the current working directory of where the script is executed
        self.cwd = os.getcwd()
        self.shoot = re.search('(\w+\s+\d+-\d+-\d+)', self.cwd).group(0)

        # Check whether the current working directory exists
        grd.Filesystem.PathExist(self.cwd)

        # Obtain the name of the base directory of the current working directory
        self.basename = os.path.basename(self.cwd)
        print(self.basename)
        # Obtain the path to the base flow project
        if grd.Filesystem.IsPathCwd(self.basename, self.cwd):
            pathToBaseflowProject = helper.FullFilePath(self.ctx.Config.Workspace,self.shoot, self.basename)
            # Check whether the the path to the base flow project exists
            grd.Filesystem.PathExist(pathToBaseflowProject)

            # Check whether you're within the backup flow directory
            grd.Filesystem.PathCwdExists(pathToBaseflowProject, self.cwd, True)

    def __CreateBackupFolder(self):
        # Loop-over all workflows
        for flow in self.ctx.Config.Workflow:
            # Obtain the path to the project flow
            pathToFlowProject = helper.FullFilePath(self.ctx.Config.Workspace, flow, self.basename)

            # Check if folder exists and whether the flow is the backup flow
            if (not grd.Filesystem.IsPath(pathToFlowProject)) and (flow == self.ctx.Config.Backup):
                directory.CreateFolder(pathToFlowProject)

                click.echo(f'Backup project created: {pathToFlowProject}\r\n')
    
    def __CreateFlows(self, backup):
        # Loop-ver the workflows and add an project directory to each flow
        for flow in self.ctx.Config.Workflow:
            # Obtain the path to the project flow
            pathToFlowProject = helper.FullFilePath(self.ctx.Config.Workspace, flow, self.basename)

            if backup:
                # Check if folder exists and whether the flow is the backup flow
                if (not grd.Filesystem.IsPath(pathToFlowProject)) and (flow == self.ctx.Config.Backup):
                    directory.CreateFolder(pathToFlowProject)

                    click.echo(f'Backup project created: {pathToFlowProject}\r\n')
            else:
                # Check if folder exists and whether the directory isn't the backup flow
                if (not grd.Filesystem.IsPath(pathToFlowProject)) and (flow != self.ctx.Config.Backup):
                    directory.CreateFolder(pathToFlowProject)

                    click.echo(f'Project created: {pathToFlowProject}')
        click.echo('\r\n')
    
    def __CopyFilesFromBaseToBackup(self):
        pictures = os.listdir(self.cwd)

        counter = 0

        for picture in pictures:
            pathToBackupFlow = self._CopyFile(picture)
            click.echo(f'Copying: {picture} -> {pathToBackupFlow} [{counter + 1}/{len(pictures)}]')
            counter += 1

        click.echo(f"Copied files: {counter}")

    def _CopyFile(self, path):
        # Obtain the filename from a specified path
        filename = base=os.path.basename(path)

        # Obtain the path to the baseflow directory
        pathToBaseflow = helper.FullFilePath(self.ctx.Config.Workspace, self.shoot, self.basename)
        # Check whether the baseflow directory exists
        grd.Filesystem.PathExist(pathToBaseflow)

        # Obtain the path the source picture within the baseflow directory
        pathToPictureSource = helper.FullFilePath(pathToBaseflow, filename)
        # Check whether the source picture path exists
        grd.Filesystem.PathExist(pathToPictureSource)

        # # Obtain the path to the backupflow directory
        pathToBackupFlow = helper.FullFilePath(self.ctx.Config.Workspace, self.shoot, self.ctx.Config.Backup)

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
        counter = 0

        shoot = self.NewShootName()

        # Obtain the original picture name within a flow directory
        pictures = os.listdir(self.cwd)
        # sort by date
        pictures.sort(key=os.path.getctime)

        count = len(pictures)

        # Loop over every picture withing the flow directory
        for index, picture in enumerate(pictures, 1):
            self._r(picture, shoot, index)
        click.echo(f"Renamed files: {count}")

    def NewShootName(self):
        newShoot = ''

        # Loop over every word of the flow name directory
        for i in self.shoot.split(' '):
            # Append the individual words to an '_'
            newShoot += f'{i}_'
        return newShoot

    def _r(self, path, shoot, index):
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

            #output = f'Renaming: {picture} -> {newName} [{counter + 1}/{len(pictures)}]'
