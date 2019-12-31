import click
from pathlib import Path
from click_default_group import DefaultGroup
from docutils.core import publish_file
from . import __version__
from .core.config import load_config, load_default_config
from .core.readers import Reader
from .core.writers import Writer
from .core.loaders import load_skills


@click.group(cls=DefaultGroup, default="run", default_if_no_args=True)
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    click.echo(f"{__name__.split('.')[0]} {__version__}")


@cmd.command()
@click.argument(
    "targets", type=click.Path(exists=True), nargs=-1,
)
def run(targets):
    """Lint files.
    """
    config_path: Path = Path.cwd() / "setup.cfg"
    if config_path.exists():
        config = load_config(config_path)
    else:
        config = load_default_config()
    reader = Reader()
    for skill in load_skills(config):
        reader.add_skill(skill)
    # Collect files
    collected = []
    for target in targets:
        t = Path(target)
        if t.is_file():
            collected.append(target)
            continue
        # TODO: lint other extension files?
        for f in t.glob("**/*.rst"):
            collected.append(f)
    # Lint all files
    for target in collected:
        publish_file(source_path=target, reader=reader, writer=Writer())


def main():
    cmd()
