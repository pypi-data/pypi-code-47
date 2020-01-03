from __future__ import print_function

import os
import sys
import boto3
import logging
import argparse

from pyperclip import copy

try:
    from configparser import NoOptionError, NoSectionError, DEFAULTSECT, RawConfigParser, ParsingError
except ImportError:
    from ConfigParser import NoOptionError, NoSectionError, DEFAULTSECT, RawConfigParser, ParsingError

logger = logging.getLogger('aws-rds')

PARAMS = ['hostname', 'username', 'region', 'port']
AWS_RDS_CONFIG_PATH = '%s/.aws/rdsconfig' % os.path.expanduser('~')


def main():
    args = get_arg()
    cfg = read_cfg(AWS_RDS_CONFIG_PATH)

    setup_logger(max(2 - args.verbose_count, 0) * 10)
    check_config()

    if args.list:
        generate_rds_list(cfg)
    elif args.default:
        set_defaults(args, cfg)
    else:
        generate_rds_token(args, cfg)


def set_defaults(args, cfg):
    dict_args = vars(args)

    for field in PARAMS:
        if dict_args[field]:
            cfg.set(DEFAULTSECT, field, dict_args[field])

    write_cfg(cfg, AWS_RDS_CONFIG_PATH)
    logger.info('default values stored')


def generate_rds_token(args, cfg):
    name = args.rds_name

    if not cfg.has_section(name) or args.setup:
        setup_rds(name, args, cfg)

    hostname = cfg.get(name, 'hostname')
    username = cfg.get(name, 'username')
    region = cfg.get(name, 'region')
    port = cfg.get(name, 'port')

    client = get_rds_client(region)
    token = client.generate_db_auth_token(hostname, port, username, region)
    if args.to_clipboard:
        copy(token)
        logger.info('Token copied to clipboard')
    else:
        print(token, end='' if args.no_return else '\n')


def generate_rds_list(cfg):
    for section in cfg.sections():
        if section != DEFAULTSECT:
            print(section)


def get_arg():
    parser = argparse.ArgumentParser()
    section = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument('-v', '--verbose', dest='verbose_count', action='count', default=0,
                        help='increases log verbosity for each occurrence')

    parser.add_argument('-s', '--setup', action='store_true', required=False,
                        help='setup a new rds configuration or modify an existing one')
    parser.add_argument('-c', '--to-clipboard', action='store_true', required=False,
                        help='copy returned value to clipboard')
    parser.add_argument('-n', '--no-return', action='store_true', required=False,
                        help='do not print the trailing newline character')

    parser.add_argument('-t', '--hostname', required=False,
                        help='set the hostname')
    parser.add_argument('-u', '--username', required=False,
                        help='set the username')
    parser.add_argument('-r', '--region', required=False,
                        help='set the region')
    parser.add_argument('-p', '--port', required=False,
                        help='set the port')

    section.add_argument('rds_name', metavar='rds-name', nargs='?',
                         help='name of the rds of which a token is required')
    section.add_argument('--default', action='store_true', required=False,
                         help='set default values')
    section.add_argument('-l', '--list', action='store_true', required=False,
                         help='print saved rds list, no other arguments are allowed')

    args = parser.parse_args()

    check_args(args, parser)

    return args


def get_rds_client(region):
    try:
        return boto3.client('rds', region_name=region)
    except NoOptionError as e:
        logger.error(e)
        sys.exit(1)


def read_cfg(path):
    cfg = RawConfigParser()
    try:
        cfg.read(path)
    except ParsingError:
        e = sys.exc_info()[1]
        logger.error('There was a problem reading or parsing your configuration file: %s' % e.args[0])
        sys.exit(1)

    return cfg


def write_cfg(cfg, path):
    with open(path, 'w') as file:
        cfg.write(file)


def setup_rds(name, args, cfg):
    if not cfg.has_section(name):
        cfg.add_section(name)

    print('Setting up %s rds\n'
          'Leave blank to use the value in parenthesis, if any' % name)

    dict_args = vars(args)

    console_input = prompter()

    for field in PARAMS:
        fallback = dict_args[field] or cfg.get(name, field, fallback='') or cfg.get(DEFAULTSECT, field, fallback='')
        value = console_input('Insert a value for %s (%s): ' % (field, fallback)) or fallback
        if value:
            cfg.set(name, field, value)
        else:
            logger.warning('no value defined for required field %s, aborting' % field)
            sys.exit(1)

    write_cfg(cfg, AWS_RDS_CONFIG_PATH)


def setup_logger(level=logging.DEBUG):
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    stdout_handler.setLevel(level)

    logger.addHandler(stdout_handler)
    logger.setLevel(level)


def check_config():
    if not os.path.isfile(AWS_RDS_CONFIG_PATH):
        console_input = prompter()
        create = console_input('Could not locate rds config file at %s, '
                               'would you like to create one? '
                               '[y/n]' % AWS_RDS_CONFIG_PATH)
        if create.lower() == 'y':
            with open(AWS_RDS_CONFIG_PATH, 'a'):
                pass
        else:
            logger.error('Could not locate rds config file at %s' % AWS_RDS_CONFIG_PATH)
            sys.exit(1)


def check_args(args, parser):
    if args.list:
        dict_args = vars(args)
        for key in dict_args:
            if dict_args[key] and key not in ['list', 'verbose_count']:
                parser.error('illegal argument --%s used with --list' % key)


def prompter():
    try:
        console_input = raw_input
    except NameError:
        console_input = input

    return console_input


if __name__ == '__main__':
    main()
