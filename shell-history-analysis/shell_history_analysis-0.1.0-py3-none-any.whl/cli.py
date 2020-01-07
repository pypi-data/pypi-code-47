#!/usr/bin/env python

"""Analyze a shell history."""

import click

from shell_history_analysis.analyze import main


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("--shell", type=click.Choice({"zsh", "fish", "bash"}))
def cli(filename: str, shell: str):
    main(filename, shell)
