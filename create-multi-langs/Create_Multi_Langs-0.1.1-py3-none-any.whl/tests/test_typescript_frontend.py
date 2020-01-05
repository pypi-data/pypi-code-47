from __future__ import absolute_import
from create_multi_langs.creater.typescript_frontend import CreaterTypeScriptFrontEnd  # noqa: E501
from . import TYPESCRIPT_FRONTEND_OUTPUT, TYPESCRIPT_FRONTEND_EXPECT_FILE, create_and_compare, ROOT_DIR  # noqa: E501
import os
from subprocess import call


def test_create_python_file():
    create_and_compare(
        CreaterTypeScriptFrontEnd,
        TYPESCRIPT_FRONTEND_OUTPUT,
        TYPESCRIPT_FRONTEND_EXPECT_FILE)

    return_code = call([
        "ts-node",
        "tests/typescript/generated_frontend.test.ts"])
    assert return_code == 0

    print('[passed] remove typescript frontend output: ',
          TYPESCRIPT_FRONTEND_OUTPUT)
    os.remove(TYPESCRIPT_FRONTEND_OUTPUT)

    os.chdir(ROOT_DIR)
