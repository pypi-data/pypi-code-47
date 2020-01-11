"""
The unit test module for config.
"""
# pylint:disable=unused-import
import argparse
import yaml

import pytest
from testfixtures import TempDirectory

from lorien import main
from lorien.configs import CONFIG_GROUP, make_config_parser, read_args_from_files
from lorien.logger import get_logger

log = get_logger('Unit-Test')


def test_definition():
    # pylint:disable=missing-docstring, redefined-outer-name

    # Check main entry.
    assert 'top' in CONFIG_GROUP

    # Check subparsers and sub-module entries.
    for parser in CONFIG_GROUP.values():
        subparsers = [p for p in parser._actions if isinstance(p, argparse._SubParsersAction)]
        if len(subparsers) == 1:
            # If the parser has a subparser, it has to be required.
            assert subparsers[0].required
        elif not subparsers:
            # If no sub-commands, then this parser has to define "entry" as the default function.
            assert parser.get_default('entry') is not None
        else:
            # Not allowed to have more than one subparsers.
            assert False


def test_config():
    # pylint:disable=missing-docstring, redefined-outer-name

    # Call make config parser only once to avoid redundent registrations.
    with pytest.raises(SystemExit):
        make_config_parser([])

    top_config_parser = CONFIG_GROUP['top']

    with pytest.raises(SystemExit):
        top_config_parser.parse_args(['generate'])
        top_config_parser.parse_args(['generate', 'extract', 'gcv'])

    args = top_config_parser.parse_args([
        'generate', 'extract', 'gcv', '--model', 'alexnet', '-o', 'output.yaml', '--target', 'llvm'
    ])
    assert len(args.model) == 1 and args.model[0] == 'alexnet'
    assert args.output == 'output.yaml'

    args = top_config_parser.parse_args(['rpc-server', '--port', '12345'])
    assert args.port == 12345

    args = top_config_parser.parse_args([
        'tune', '--workload', 'a.json', '--workload', 'b.json', '--rpc',
        '"llvm -mcpu=core-avx2: [0.0.0.0:18871]"', '--db', 'http://0.0.0.0:10020', '-t', 'random',
        '-n', '10'
    ])
    assert len(args.workload) == 2
    assert args.workload[0] == 'a.json'
    assert args.workload[1] == 'b.json'
    assert len(args.rpc) == 1
    assert args.rpc[0] == '"llvm -mcpu=core-avx2: [0.0.0.0:18871]"'
    assert args.db == 'http://0.0.0.0:10020'
    assert args.tuner == 'random'
    assert args.ntrial == 10
    assert args.test == 5


def test_read_args_from_files():
    # pylint:disable=missing-docstring, redefined-outer-name

    args = read_args_from_files(['a', 'b', 'c'])
    assert len(args) == 3

    with TempDirectory() as temp_dir:
        config_file = '{}/cfg.yaml'.format(temp_dir.path)
        with open(config_file, 'w') as filep:
            filep.write(yaml.dump({'model': ['a', 'b', 'c']}))
        args = read_args_from_files(['p', '@{}'.format(config_file)])
        assert args == ['p', '--model', 'a', '--model', 'b', '--model', 'c']
