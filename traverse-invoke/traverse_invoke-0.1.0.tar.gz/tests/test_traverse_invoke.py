#!/usr/bin/env python

"""Tests for `traverse_invoke` package."""

import pytest

from click.testing import CliRunner

from traverse_invoke import traverse_invoke
from traverse_invoke import cli

import pprint as pp
pprint = pp.pprint

entry = traverse_invoke.entry_traverse
import pprint as pp

invocations = []

def _genfunc(fname):
    def x(**args):
        invocations.append((fname, args))
        print(f">>In {fname} have {pp.pformat(args)}")
    return x

def test_liblike():
    _modules = {
        'basemod':_genfunc('basemod'),
        'installed':{
            'testfoo1':_genfunc('testfoo1'),
            'testfoo2':_genfunc('testfoo2'),
        },
        'lib':{
            'sys':_genfunc('sys')
        }
    }

    funcs = {
        'log_config':_genfunc('log_config'),
        'entry':{
            'pre':_genfunc('pre'),
            'modules':_modules,
            'post':_genfunc('post')
        },
        'infolib':_genfunc('infolib')
    }

    modspec = 'log_config.entry.pre.modules.basemod.{}.post'
    path1 = modspec.format('installed.testfoo1')
    path2 = modspec.format('installed.testfoo2')

    libspec = 'log_config.entry.pre.modules.basemod.lib.{}.post'
    syspath = libspec.format('sys')

    def gen_config():
        config = {
            'everywhere':'happiness',
            'modules':{
                'clash':'post-spec', 
            },
            'testfoo1':{
                'foospec':12,
                'clash':'foo-spec'
                # in Descent case, this will overwrite var in modules
                # and we'll have it in post
            },
            'log_config':{
                'param': 'log nicely, please',
                'clash': 'log-spec'
            }
        }
        return config


    entry(gen_config(), syspath.split('.'), funcs)
    fnames = [i[0] for i in invocations]
    assert fnames == ['log_config', 'pre', 'basemod', 'sys', 'post']
    invocations.clear()

    entry(gen_config(), path1.split('.'), funcs)
    param = {k:v for k,v in invocations}
    assert param['testfoo1']['clash']=='foo-spec'
    assert param['post']['clash']=='log-spec'
    invocations.clear()

    path1 += '.modules.installed.testfoo2.post.log_config.entry.pre'
    entry(gen_config(), path1.split('.'), funcs)

def test_silly():
    funcs = {
        'print':lambda **x: print(x),
        'foo':lambda **x: print('>>foo',x),
        'bar':lambda **x: print('>>Bar',x)
    }

    path = ['print', 'foo', 'ba']
    config = {
        'print':{
            'foo':{
                'bar':{
                    'x':1,
                    'y':2
                },
                'default':7
            }
        }
    }

    entry(config, path, funcs)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['sys'])
    assert result.exit_code == 0
    assert 'sys' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
