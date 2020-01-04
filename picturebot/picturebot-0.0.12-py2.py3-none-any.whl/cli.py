"""Console script for picturebot."""

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
import picturebot.shoot as sht

@click.group()
@click.pass_context
def main(context):
    '''Main method where config data and workspace object are initialized
    
    Args:
        context (object): Global context object
    '''

    pathToConfig = helper.FullFilePath("config.json")

    # Check whether the path to the confile exists
    grd.Filesystem.PathExist(pathToConfig)

    with open(pathToConfig) as f:
        # if conext isn't initialized created a new dictionary
        if context.obj is None:
            context.obj = dict()

         # Load data from file
        data = json.load(f)
        
        # Load the config data in the context variable
        context.obj['config'] = poco.Config(data['workspace'], data['workflow'], data['baseflow'], data['backup'], data['selection'], data['edited'], data['preview'], data['editing'], data['instagram'])
        # Load the workspace object into the context variable
        context.obj['workspaceObj'] = ws.Workspace(pathToConfig, context)

@main.command()
@click.option('--create', '-c', is_flag=True, help='Create a new workspace and initialize the workspace')
@click.option('--init', '-i', is_flag=True, help='Initialize the pre-configured workspace')
@click.pass_context
def workspace(context, create, init):

    ctx = helper.Context(context)
    # Get the current working directory of where the script is executed
    cwd = os.getcwd()

    #Check whether the current working directory exists
    grd.Filesystem.PathExist(cwd)

    if init:
        #Check whether the workplace folder exists    
        grd.Filesystem.PathExist(ctx.Config.Workspace)

        ctx.WorkspaceObj.Initialize(cwd)

    elif create:
        ctx.WorkspaceObj.Create()   

@main.command()
@click.option('--backup', '-b', nargs=1, type=str, help='Make a copy of a picture in the backup flow')
@click.option('--massbackup', '-mb', is_flag=True, help='Make a copy of all pictures within the base flow and copy them to the backup flow')
@click.option('--rename', '-r', nargs=2, type=str, help='Rename a picture within the baseflow accordingly to it\'s shootname')
@click.option('--massrename', '-mr', is_flag=True, help='Rename all pictures within the baseflow accordingly to it\'s shootname')
@click.option('--convert', '-c', nargs=2, type=str, help='Convert a raw picture within the baseflow to a jpg format and store it within the preview flow')
@click.pass_context
def base(context, backup, massbackup,rename, massrename, convert):
    '''Method to backup files from the baseflow project
    Args:
        config (Config): Config data object
    '''

    ctx = helper.Context(context)

    bs = baseflow.Base(ctx)

    if backup:
        bs.Backup(backup)
    elif massbackup:
        bs.MassBackup()
    elif rename:
        bs.Rename(rename[0], rename[1])
    elif massrename:
        bs.MassRename()
    elif convert:
        #pb base -c "C://fsdfds" 10%
        bs.Convert(convert[0], convert[1])

@main.command()
@click.option('--show', '-s', is_flag=True, help='Open config file in an editor')
@click.option('--location', '-l', is_flag=True, help='Print config file location')
@click.option('--version', '-v', is_flag=True, help='Print picturebot script version')
@click.pass_context
def config(context, show, location, version):
    '''CLI command that handles the configuration file operations
    
    Args:
        context (object): Global context object
        view (object): Option that opens the configuration file
        location (object): Option that prints the configuration file location within the filesystem
    '''
    ctx = helper.Context(context)

    if show:
        ctx.WorkspaceObj.ShowConfig()
    elif location:
        ctx.WorkspaceObj.PrintConfig()
    elif version:
        ctx.WorkspaceObj.Version()

@main.command()
@click.option('--completed', '-c', is_flag=True, help='View config file')
@click.option('--edited', '-e', is_flag=True, help='View config file')
@click.pass_context
def flow(context, completed, edited):
    ctx = helper.Context(context)

    fw = otherflow.Flow(ctx)
    if completed:
        fw.Completed()
    elif edited:
        fw.Edited()

@main.command()
@click.option('--new', '-n', nargs=2, type=str, help='Create a new shoot')
@click.pass_context
def shoot(context, new):
    ctx = helper.Context(context)

    if new:
        newShoot = f'{new[0]} {new[1]}'
        s = sht.Shoot(ctx, newShoot)
        print(f'main: {newShoot}')
        s.Create()

if __name__ == "__main__":
    main() # pragma: no cover
