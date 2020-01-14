import logging
from pathlib import Path
from typing import Optional
from operator import attrgetter

import click
from more_itertools import groupby_transform

from .demos import load_unity_demo


@click.group()
def cli():
    pass


@cli.group()
def demonstrations():
    pass


@demonstrations.command()
@click.argument("source", type=click.Path(exists=True, file_okay=True, dir_okay=True))
@click.argument(
    "destination", type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
@click.option("--meta", type=click.File())
def transpile(source, destination, meta=None):
    """
    transpile unity demonstrations from SOURCE to ariadne demonstrations at DEST.
    if source is a file, then that file will be transpiled. If source is a folder,
    then all the .demo files will be transpiled. If a .toml file exists with the
    same stem as the .demo, then it will be used for meta data.
    """
    source = Path(str(source))
    destination = Path(str(destination))
    files = []
    try:
        files.extend(source.iterdir())
    except NotADirectoryError:
        files.append(source)
    files.sort(key=str)

    for stem, paths in groupby_transform(files, attrgetter('stem') ):
        paths = list(paths)
        demo:Optional[Path] = next((path for path in paths if path.suffix == '.demo'), None)
        if demo is None:
            logging.warning(f'Found stem {stem} but no files with ".demo" extension.')
            continue
        metadata = demo.with_suffix('.toml')
        metadata = metadata.is_file() and metadata or meta
        try:
            traj = load_unity_demo(demo, metadata)
            destination.parent.mkdir(parents=True, exist_ok=True)
            traj.dump((destination/demo.name).with_suffix('.trajectory'))
        except:
            logging.warning(f'Unable to load file {demo}')
            continue