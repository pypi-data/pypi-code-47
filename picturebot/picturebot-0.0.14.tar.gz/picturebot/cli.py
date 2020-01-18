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
        lstConfig = []
        for d in data:
            lstConfig.append(poco.Config(d['workspace'], d['workflow'], d['baseflow'], d['backup'], d['selection'], d['edited'], d['preview'], d['editing'], d['instagram']))
        c = 1

        # Load the config data in the context variable
        #x = poco.Config(data['workspace'], data['workflow'], data['baseflow'], data['backup'], data['selection'], data['edited'], data['preview'], data['editing'], data['instagram'])
        #context.obj['config'] = poco.Config(data[c]['workspace'], data[c]['workflow'], data[c]['baseflow'], data[c]['backup'], data[c]['selection'], data[c]['edited'], data[c]['preview'], data[c]['editing'], data[c]['instagram'])
        context.obj['config'] = lstConfig
        # Load the workspace object into the context variable
        context.obj['workspaceObj'] = ws.Workspace(pathToConfig, context)

        # print(data[1]['workspace'])
        # print(context.obj['config'])

@main.command()
@click.option('--create', '-c', nargs=1, help='Create a new workspace')
@click.pass_context
def workspace(context, create):
    '''Create a new workspace
    
    Args:
        context (object): Global context object
        create (object): Create a new workspace
    '''

    ctx = helper.Context(context)
    # Get the current working directory of where the script is executed
    cwd = os.getcwd()

    #Check whether the current working directory exists
    grd.Filesystem.PathExist(cwd)

    if create:
        ctx.WorkspaceObj.Create(create[0])   

@main.command()
@click.option('--backup', '-b', nargs=2, type=str, help='Make a copy of a picture in the backup flow')
@click.option('--massbackup', '-mb', nargs=1, type=str, help='Make a copy of all pictures within the base flow and copy them to the backup flow')
@click.option('--rename', '-r', nargs=3, type=str, help='Rename a picture within the baseflow accordingly to it\'s shootname')
@click.option('--massrename', '-mr', nargs=1, help='Rename all pictures within the baseflow accordingly to it\'s shootname')
@click.option('--convert', '-c', nargs=3, type=str, help='Convert a raw picture within the base flow to a jpg format and store it within the preview flow')
@click.pass_context
def base(context, backup, massbackup, rename, massrename, convert):
    '''Method to backup files from the baseflow project

    Args:
        context (object): Global context object
        backup (object): Make a copy of a picture in the backup flow
        massbackup (object): Make a copy of all pictures within the base flow and copy them to the backup flow
        rename (object): Rename a picture within the baseflow accordingly to it's shootname
        massrename (object): Rename all pictures within the baseflow accordingly to it's shootname
        convert (object): Convert a raw picture within the base flow to a jpg format and store it within the preview flow
    '''

    ctx = helper.Context(context)

    if backup:
        bs = baseflow.Base(ctx, backup[0])
        bs.Backup(backup[1])
    elif massbackup:
        bs = baseflow.Base(ctx, massbackup[0])
        bs.MassBackup()
    elif rename:
        bs = baseflow.Base(ctx, rename[0])
        bs.Rename(rename[1], rename[2])
    elif massrename:
        bs = baseflow.Base(ctx, massrename[0])
        bs.MassRename()
    elif convert:
        bs = baseflow.Base(ctx, convert[0])
        bs.Convert(convert[1], convert[2])

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
@click.option('--new', '-n', nargs=3, type=str, help='Create a new shoot')
@click.pass_context
def shoot(context, new):
    '''Shoot option allows modification of a shoot within the workspace

    Args:
        context (object): Global context object
        new (object): Option to create a new shoot (<name> <date>) 
    '''

    ctx = helper.Context(context)

    if new:
        newShoot = f'{new[1]} {new[2]}'
        # Create a shoot object
        s = sht.Shoot(ctx, new[0], newShoot)
        # Creates the shoot
        s.Create()

if __name__ == "__main__":
    main() # pragma: no cover
