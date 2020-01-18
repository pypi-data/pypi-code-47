import sys
import os
import click
from picturebot.helper import Helper as helper
import picturebot.poco as poco
import generalutils.guard as grd
from picturebot.directory import Directory as directory
import picturebot as pb

class Workspace:
    def __init__(self, location, context):
        '''Constructor For the workspace class
        
        Args:
            location (string): Configuration file location 
            context (object): Global context object        '''

        self.location = location
        self.context = context

    def Create(self, index):
        '''Create a new workspace an initialize it with flows'''
        
        index = int(index)

        ctx = helper.Context(self.context)

        if not grd.Filesystem.IsPath(ctx.Config[index].Workspace):
            directory.CreateFolder(ctx.Config[index].Workspace)
        
        else:
            click.echo(f"Workspace {ctx.Config.Workspace} already exists")

    def Version(self):
        '''Print script version'''

        click.echo(f'picturebot version: {pb.__version__}')

    def ShowConfig(self):
        '''Open the config location within an editor'''

        ctx = helper.Context(self.context)

        grd.Filesystem.PathExist(ctx.WorkspaceObj.location)
        os.system(f"start {ctx.WorkspaceObj.location}")

    def PrintConfig(self):
        '''Print the configuration path location'''
        
        ctx = helper.Context(self.context)

        click.echo(ctx.WorkspaceObj.location)
