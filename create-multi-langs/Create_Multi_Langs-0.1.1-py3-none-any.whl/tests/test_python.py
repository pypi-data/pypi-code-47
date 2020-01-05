from __future__ import absolute_import
from create_multi_langs.creater.python import CreaterPython
from . import PYTHON_OUTPUT, PYTHON_EXPECT_FILE, create_and_compare, ROOT_DIR
import os
from subprocess import call


def test_create_python_file():
    create_and_compare(CreaterPython, PYTHON_OUTPUT, PYTHON_EXPECT_FILE)

    return_code = call(["pytest", "tests/python/generated_t.py"])
    assert return_code == 0

    print('[passed] remove python output: ', PYTHON_OUTPUT)
    os.remove(PYTHON_OUTPUT)

    os.chdir(ROOT_DIR)
