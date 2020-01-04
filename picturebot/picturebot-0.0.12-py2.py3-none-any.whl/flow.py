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
import picturebot.base as baseflow
import picturebot.flow as otherflow

class Flow:
    def __init__(self, context):
        self.ctx = context
    
    def Edited(self):
        # Get the current working directory of where the script is executed
        cwd = os.getcwd()

        # Check whether the current working directory exists
        grd.Filesystem.PathExist(cwd)

        # Obtain the name of the base directory of the current working directory
        shoot = os.path.basename(cwd)
    
        # Obtain the path to the base flow project
        pathToBaseflowProject = helper.FullFilePath(self.ctx.Config.Workspace, self.ctx.Config.Selection, shoot)

        # Check whether the the path to the base flow project exists
        grd.Filesystem.PathExist(pathToBaseflowProject)

        # Check whether you're within the baseflow directory
        grd.Filesystem.PathCwdExists(pathToBaseflowProject, cwd, True)

        # Obtain the absolute path to the edit flow of a shoot
        pathToShootInEditedFlow = helper.FullFilePath(self.ctx.Config.Workspace, self.ctx.Config.Edited, shoot)

        # Check whether you're within the edit flow shoot directory
        grd.Filesystem.PathExist(pathToShootInEditedFlow)

        # Open the correct edited directory
        os.system(f"explorer {pathToShootInEditedFlow}") 

    def Completed(self):
        # Get the current working directory of where the script is executed
        cwd = os.getcwd()

        # Check whether the current working directory exists
        grd.Filesystem.PathExist(cwd)
        
        # Check whether the script is executed from the workspace directory
        grd.Filesystem.PathCwdExists(self.ctx.Config.Workspace, cwd)

        # Obtain the path to the the edit root directory
        pathToEditedRoot = helper.FullFilePath(self.ctx.Config.Workspace, self.ctx.Config.Edited)

        # Check whether the path to the edit root directory exists
        grd.Filesystem.PathExist(pathToEditedRoot)

        # Loopover every shoot within the edit directory
        for shoot in os.listdir(pathToEditedRoot):
            # Obtain the path to the shoot within the edit root directory
            pathToEditedShoots = helper.FullFilePath(pathToEditedRoot, shoot)

            # Check whether the shoot exists within the edit root directory
            grd.Filesystem.PathExist(pathToEditedShoots)

            # Amount of pictures within the edit shoot directory
            shootAmountPicturesEdited = len(os.listdir(pathToEditedShoots))

            pathToSelectedShoot = helper.FullFilePath(self.ctx.Config.Workspace, self.ctx.Config.Selection, shoot)
            grd.Filesystem.PathExist( pathToSelectedShoot)

            # Amount of pictures within the selection shoot directory
            shootAmountPicturesSelection = len(os.listdir(pathToSelectedShoot))

            # Check whether the amount of pictures are equal
            if shootAmountPicturesEdited != shootAmountPicturesSelection:
                print(f'Shoot: {shoot} is not fully edited')
