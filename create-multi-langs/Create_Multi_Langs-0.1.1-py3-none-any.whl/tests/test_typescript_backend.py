from __future__ import absolute_import
from create_multi_langs.creater.typescript_backend import CreaterTypeScriptBackEnd  # noqa: E501
from . import TYPESCRIPT_BACKEND_OUTPUT, TYPESCRIPT_BACKEND_EXPECT_FILE, create_and_compare, ROOT_DIR  # noqa: E501
import os
from subprocess import call


def test_create_python_file():
    create_and_compare(
        CreaterTypeScriptBackEnd,
        TYPESCRIPT_BACKEND_OUTPUT,
        TYPESCRIPT_BACKEND_EXPECT_FILE)

    return_code = call([
        "ts-node",
        "tests/typescript/generated_backend.test.ts"])
    assert return_code == 0

    print('[passed] remove typescript frontend output: ',
          TYPESCRIPT_BACKEND_OUTPUT)
    os.remove(TYPESCRIPT_BACKEND_OUTPUT)

    os.chdir(ROOT_DIR)
