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

class Shoot:
        
    def __init__(self, context, index, name):
        '''Shoot class constructor
        
        Args:
            context (object): Global context object
            index (int): Index of the selected workspace configuration
            name (string): Shootname containing the date
        '''        
        
        self.index = int(index)
        self.ctx = context
        self.name = name
    
    def Create(self):
        '''Creates a shoot within the workspace directory'''

        # Obtain the root directory of the new shoot
        shootRootPath = helper.FullFilePath(self.ctx.Config[self.index].Workspace, self.name)

        # Check whether the root directory of the new shoot exists
        if not grd.Filesystem.IsPath(shootRootPath):
            # Create a new shoot
            directory.CreateFolder(shootRootPath)
            # Check whether the shoot is successfully created
            grd.Filesystem.PathExist(shootRootPath)
        else:
            print('Path already exists')

        self.__CreateFlow(shootRootPath)

    def __CreateFlow(self, root):
        ''' Create all flows configured in the config file

        Args:
            root (string): Root directory of the newly created shoot
        '''

        counter = 0

        #Loop-over the workflows
        for flow in self.ctx.Config[self.index].Workflow:
            pathToFlow = helper.FullFilePath(root, flow)

            # Only create non existing flows
            if not grd.Filesystem.IsPath(pathToFlow):
                directory.CreateFolder(pathToFlow)
                click.echo(f'Flow created: {pathToFlow}')
                counter += 1 
        
        click.echo(f"Flows created: {counter}")
