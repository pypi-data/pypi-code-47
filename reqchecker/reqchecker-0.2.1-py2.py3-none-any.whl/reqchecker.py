# -*- coding: utf-8 -*-

import json
import os
import coloredlogs
import logging
from sys import exit
from copy import deepcopy

"""Main module."""

def checklist(options, logger):
    """Make check_list.

    {'local': {'snowav': '/home/mark/wkspace/code/snowav',
               'awsm': '/home/mark/wkspace/code/nwrc/awsm'}}

    """

    # Initialize what will get checked
    check_list = {}

    if options['file'] is not None:
        file = options['file']

    else:
        file = "reqchecker/defaults.json"

    # Get defaults
    try:
        with open(os.path.abspath(file)) as f:
            defaults = json.load(f)

    except:
        logger.error(" Failed reading reqchecker/defaults.json, may be a "
            "formatting error")
        exit()

    # Check formating
    check_format(defaults, logger)

    section = options['section']

    # Check that the given section exists
    if section not in defaults.keys():
        logger.error(" Section '{}' is not "
            "in reqcheck/defaults.json".format(section, defaults.keys()))
        exit()

    # Check option requirements
    source = [*defaults[section].keys()][0]

    # Will overwrite as necessary from cli args
    check_list = deepcopy(defaults[section])

    # First check the source
    if options['source'] is not None:
        source = options['source']
        check_list[source] = check_list.pop([*check_list.keys()])
        check_list['source'] = source
        logger.debug(" source: '{}' from cli".format(source))

    if source == 'github':

        if not "credentials" in [*defaults[section].keys()]:
            logger.error(" Must supply path to github credentials in "
                "specified defaults.json section")
            exit()

        else:
            path = defaults[section]["credentials"]

            try:
                with open(path) as f:
                    credentials = json.load(f)

            except:
                logger.error(" Could not open {}".format(path))
                exit()

            check_list["credentials"] = credentials["token"]
            check_list["user"] = credentials["user"]

    # Overwrite 'local' from cli args
    if options['packages'] is not None and options['locations'] is not None:

        # remove old
        check_list[source] = {}

        # assign new
        for package, location in zip(options['packages'], options['locations']):
            check_list[source][package] = location
            logger.debug(" package: {} from cli".format(package))
            logger.debug(" location: {} from cli".format(location))

    # Overwrite 'github' from cli
    if options['packages'] is not None and options['branches'] is not None:

        # remove old
        check_list[source] = {}

        # assign new
        for package, branch in zip(options['packages'], options['branches']):
            check_list[source][package] = branch
            logger.debug(" package: {} from cli".format(package))
            logger.debug(" location: {} from cli".format(branch))

    return check_list

def check_format(defaults, logger):
    """Simple .json format checking."""

    sources = ["local", "github", "credentials"]
    sections = [*defaults.keys()]

    for section in sections:

        for key in [*defaults[section].keys()]:

            if key not in sources:
                logger.warning(" In .json, key: '{}' in section {} must be one "
                    "of {}, this may error later".format(key, section, sources))

            if key == "local":
                for path in [*defaults[section][key].values()]:
                    if not os.path.isdir(path) and not os.path.isfile(path):
                        logger.warning(" In .json, path '{}' is "
                            "not a valid file or path, will error if "
                            "using 'local' option".format(path))

            if key == 'github':
                if "credentials" == [*defaults[section].keys()][0]:
                    logger.warning(" In .json, 'credentials' section should "
                        "follow 'github', this may error later")

                if "credentials" not in [*defaults[section].keys()]:
                    logger.warning(" In .json, 'github' also requires "
                        "'credentials' section, will error if using 'github'"
                        "option")

def empty_requirements(check_list):
    """Make a blank requirements list."""

    requirements = deepcopy(check_list)
    source = [*requirements.keys()][0]

    for loc in [*requirements[source].keys()]:
        requirements[source][loc] = []

    return requirements


def logsetup(flag):
    """Set up logging."""

    if flag:
        lvl = logging.DEBUG
    else:
        lvl = logging.INFO

    level_styles = {'info': {'color': 'green'},
                    'error': {'color': 'red'},
                    'debug': {'color': 'green'},
                    'warning': {'color': 'yellow'}}

    field_styles =  {'hostname': {'color': 'magenta'},
                     'programname': {'color': 'cyan'},
                     'name': {'color': 'grey'},
                     'levelname': {'color': 'white', 'bold': False},
                     'asctime': {'color': 'green'}}

    fmt = '%(levelname)s:%(module)s:%(message)s'

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(level=lvl)
    coloredlogs.install(level=lvl, fmt=fmt, level_styles=level_styles,
                        field_styles=field_styles)

    return logging
