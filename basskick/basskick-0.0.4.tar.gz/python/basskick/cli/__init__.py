
import click

from ..api import benv, packon, system


@click.group()
def basskick():
    pass

@basskick.command()
@click.option('-v', '--version', required=False)
def blender(version=None):
    system.run('blender', version)

@basskick.command()
def xxx():
    from ..packon import build
    build.xxx()

#
# benv
#

@basskick.group(name='benv')
def benv_cmds():
    pass

@benv_cmds.command(name='create')
@click.argument('name')
@click.argument('location', default='.')
def create_benv(name, location):
    '''
    Create a new benv.
    '''
    benv.create(name, location)

#
# packon
#

@basskick.group(name='packon')
def packon_cmds():
    pass

@packon_cmds.command(name='create')
@click.argument('name')
@click.option('-b', '--benv', required=False)
def create_packon(name, benv=None):
    '''
    Create a new packon in the current or specified benv.
    '''
    benv = benv or None
    packon.create(name, benv)

@packon_cmds.command(name='install')
@click.argument('names', nargs=-1)
@click.option('-b', '--benv', required=False)
@click.option('-U', '--upgrade', is_flag=True, help='Upgrade the specified packons.')
@click.option('-i', '--index-url', required=False, help='custom index url')
def install_packons(names, benv=None, upgrade=False, index_url=None):
    '''
    Install packons in the current or specified benv.
    '''
    packon.install(names, benv, upgrade, index_url)

@packon_cmds.command(name='uninstall')
@click.argument('names', nargs=-1)
@click.option('-b', '--benv', required=False)
def uninstall_packons(names, benv=None):
    '''
    Uninstall packons in the current or specified benv.
    Note that dependencies will not be uninstalled.
    '''
    packon.uninstall(names, benv)

@packon_cmds.command(name='list')
@click.option('-b', '--benv', required=False)
@click.option('-o', '--outdated', default=True, help='List outdated packons')
@click.option('-u', '--uptodate', default=True, help='List uptodate packons')
@click.option('-e', '--editable', default=True, help='List editable packons')
def list_packons(benv=None, outdated=True, uptodate=True, editable=True):
    '''
    Lists installed packons.
    '''
    packon.list(benv, outdated, uptodate, editable)


@packon_cmds.command(name='show')
@click.argument('names', nargs=-1)
@click.option('-b', '--benv', required=False)
def show_packons(names, benv=None):
    '''
    Show information about installed packons in the current or specified benv.
    '''
    packon.show(names, benv)


#
# sytem
#

@basskick.group(name='system')
def system_cmds():
    pass

@system_cmds.command()
@click.option('-s', '--set', required=False)
def install_dir(set=None):
    '''
    Show or change the install-dir.
    '''
    if set is not None:
        system.set_install_dir(set)
    print('install_dir: {!r}'.format(system.get_install_dir()))

@system_cmds.command()
@click.option('-v', '--version', required=False)
@click.option('-r', '--repair', is_flag=True, help='Replace the pre-installed version with a fresh one.')
@click.option('-u', '--url', required=False, help='Use custom repository url for zip download.')
def install(version=None, repair=False, url=None):
    '''
    Download and install a Blender version in the install-dir.
    '''
    system.install(version, repair, url)


@system_cmds.command()
@click.argument('app', default='blender')
@click.option('-v', '--version', required=False)
def run(app, version=None):
    '''
    Run the given App at the given version.
    '''
    system.run(app, version)


