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
    def __init__(self, context, name):
        self.ctx = context
        self.name = name
    
    def Create(self):
        # Obtain the path to the base flow project
        pathToBaseflowProject = helper.FullFilePath(self.ctx.Config.Workspace, self.name)

        # Check whether the the path to the base flow project exists
        if not grd.Filesystem.IsPath(pathToBaseflowProject):
            directory.CreateFolder(pathToBaseflowProject)
            grd.Filesystem.PathExist(pathToBaseflowProject)
        else:
            print('Path already exsists')

        self.__CreateFlow(pathToBaseflowProject)

    def __CreateFlow(self, name):
        ''' Create a new flows

        Args:
            context (object): Global context object
        '''

        counter = 0

        #Loop-over the workflows
        for flow in self.ctx.Config.Workflow:
            pathToFlow = helper.FullFilePath(name, flow)

            # Only create non existing flows
            if not grd.Filesystem.IsPath(pathToFlow):
                directory.CreateFolder(pathToFlow)
                click.echo(f'Flow created: {pathToFlow}')
                counter += 1 
        
        click.echo(f"Flows created: {counter}")