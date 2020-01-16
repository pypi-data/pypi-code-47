import io
import json
from pathlib import Path
import pytest
import requests
import os
import subprocess
from zipfile import ZipFile

from pytest_tezos.TestTypes import AbstractTestType

URL = 'https://gitlab.com/ligolang/ligo/-/jobs/artifacts/dev/download?job=build-and-package-ubuntu-18-04'


class Contract:
    def __init__(self, ligo, path):
        self.ligo = ligo
        self.code = json.loads(subprocess.check_output(f'''
            {ligo.bin} compile-contract --michelson-format=json {path} main
        '''.strip(), shell=True))

    def originate(self, client, expr):
        return client.origination(dict(
            code=self.code,
            storage=self.ligo.compile(expr),
        )).autofill().sign()


class Ligo:
    @property
    def bin(self):
        own = Path(os.getenv('HOME')) / '.local' / 'bin' / 'ligo'
        if own.exists():
            return str(own)

        try:
            return subprocess.check_output('which ligo', shell=True).decode('utf8').strip()
        except subprocess.CalledProcessError:
            print('ligo not available, try install.sh')

    def compile(self, arg):
        if isinstance(arg, AbstractTestType):
            cmd = [
                self.bin,
                'compile-expression',
                'cameligo',
                '--michelson-format=json',
                arg.__repr__(),
            ]
            res = subprocess.check_output(cmd).decode('utf8')
            return json.loads(res)
        else:
            return Contract(self, arg)


@pytest.fixture
def ligo():
    return Ligo()
