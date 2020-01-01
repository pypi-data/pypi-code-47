#!/usr/bin/env python
# encoding: utf-8

"""
Feeding latex templates and compiling it
"""

import logging
import math as m
import subprocess
import random as rd
from pathlib import Path
import os
from .texenv import *
from .latex_error_parser import generic_sink, filter_errors

formatter = logging.Formatter('%(name)s :: %(levelname)s :: %(message)s')
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)
# création de l'objet logger qui va nous servir à écrire dans les logs
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(steam_handler)


EXPORT_DICT = {}
EXPORT_DICT.update(m.__dict__)
EXPORT_DICT.update(rd.__dict__)
EXPORT_DICT.update(__builtins__)


def update_export_dict(new_dict):
    """Update global variable with new_dict

    It allows to import new functions (or modules) inside templates.

    :param new_dict: needed tools across all template renders
    """
    EXPORT_DICT.update(new_dict)


def feed(template, data, output="", force=0):
    """ Feed template with data to output

    :param template: jinja2 template with texenv environment
    :param data: Data dictionnary
    :param output: name of the output file
    (by default: tpl is replaced by a 2 digits number)
    :param force: Override is the output already exists

    :return: name of fed template
    """
    logger.info(f"Getting template {template}")
    tpl = texenv.get_template(str(template))

    if not output:
        num = 1
        output_p = Path(template.replace('tpl', f'{num:02d}'))
        while output_p.exists() and not force:
            logger.debug(f"{output_p} exists. Try next one")
            num += 1
            output_p = Path(template.replace('tpl', f'{num:02d}'))
    else:
        output_p = Path(output)
        if not force and output_p.exists():
            logger.error(f"{output} exists. Use force=1 do override it")
            raise ValueError(f"{output} exists. Use force=1 do override it")

    output_dir = output_p.parent
    if output_dir and not output_dir.exists():
        logger.debug(f"Creating output dir {output_dir}")
        output_dir.mkdir(exist_ok=True)

    with open(output_p, "w") as output_f:
        output_f.write(tpl.render(**EXPORT_DICT, **data))
    logger.info(f"{template} has been rendered to {output}.")
    return output_p


def pdflatex(tex_filename, output_dir=""):
    """ Compile a latex file with pdflatex

    If output_dir is not set, it produce it next to the latex file.
    """
    latex_file = Path(tex_filename)
    if not output_dir:
        output_dir = latex_file.parent.resolve()
    logger.debug(f"output_dir for pdflatex is {output_dir}")

    prev_cwd = Path.cwd()
    os.chdir(output_dir)
    compilation = subprocess.Popen(
        [
            "pdflatex",
            f"-output-directory={output_dir}",
            # "-halt-on-error",
            "-interaction=nonstopmode",
            "-shell-escape",
            str(latex_file.name),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        # shell=True
        )

    latex_error_logger = filter_errors(generic_sink(logger.error))
    for line in compilation.stdout:
        latex_error_logger.send(line.decode("latin-1").rstrip('\r\n'))
    compilation_status = compilation.wait()

    logger.debug(f"{latex_file.name} has been compiled in {output_dir}")

    os.chdir(prev_cwd)


def clean(dirname="", garbages=["*.aux", "*.log"]):
    """ Clean the directory from aux and log latex files """
    if not dirname:
        dirname = Path("./")
    for g in garbages:
        g_files = Path(dirname).glob(g)
        logger.debug(f"Remove {g_files}")
        for g_file in g_files:
            g_file.unlink()

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del
