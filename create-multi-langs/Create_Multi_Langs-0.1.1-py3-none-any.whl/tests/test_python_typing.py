from __future__ import absolute_import
from create_multi_langs.creater.python_typing import CreaterPythonTyping
from . import PYTHON_TYPING_OUTPUT, PYTHON_TYPING_EXPECT_FILE, create_and_compare, ROOT_DIR  # noqa: E501
import os
from subprocess import call


def test_create_python_file():
    create_and_compare(
        CreaterPythonTyping,
        PYTHON_TYPING_OUTPUT,
        PYTHON_TYPING_EXPECT_FILE)

    return_code = call(["pytest", "tests/python/generated_typing_t.py"])
    assert return_code == 0

    print('[passed] remove python typing output: ', PYTHON_TYPING_OUTPUT)
    os.remove(PYTHON_TYPING_OUTPUT)

    os.chdir(ROOT_DIR)
