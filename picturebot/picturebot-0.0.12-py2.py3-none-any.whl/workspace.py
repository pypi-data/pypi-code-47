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

    def Initialize(self, cwd):
        '''Initialize an existing workspace with flows
        
        Args:
            cwd (string): Execution path of the program
        '''

        ctx = helper.Context(self.context)

        # Only create the flow when the script is executed from the workspace directory
        grd.Filesystem.PathCwdExists(ctx.Config.Workspace, cwd, True)

        self.__CreateFlow(ctx)

    def Create(self):
        '''Create a new workspace an initialize it with flows'''

        ctx = helper.Context(self.context)

        if not grd.Filesystem.IsPath(ctx.Config.Workspace):
            directory.CreateFolder(ctx.Config.Workspace)
            
            self.__CreateFlow(ctx)
        
        else:
            click.echo(f"Workspace {ctx.Config.Workspace} already exists")

    def Version(self):
        click.echo(f'picturebot version: {pb.__version__}')

    def ShowConfig(self):
        ctx = helper.Context(self.context)

        grd.Filesystem.PathExist(ctx.WorkspaceObj.location)
        os.system(f"start {ctx.WorkspaceObj.location}")

    def PrintConfig(self):
        ctx = helper.Context(self.context)

        click.echo(ctx.WorkspaceObj.location)

    def __CreateFlow(self, context):
        ''' Create a new flows

        Args:
            context (object): Global context object
        '''

        counter = 0

        #Loop-over the workflows
        for flow in context.Config.Workflow:
            pathToFlow = helper.FullFilePath(context.Config.Workspace, flow)

            # Only create non existing flows
            if not grd.Filesystem.IsPath(pathToFlow):
                directory.CreateFolder(pathToFlow)
                click.echo(f'Flow created: {pathToFlow}')
                counter += 1 
        
        click.echo(f"Flows created: {counter}")
