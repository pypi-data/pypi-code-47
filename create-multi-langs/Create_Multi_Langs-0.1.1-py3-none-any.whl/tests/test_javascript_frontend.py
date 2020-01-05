from __future__ import absolute_import
from create_multi_langs.creater.javascript_frontend import CreaterJavaScriptFrontEnd  # noqa: E501
from . import JAVASCRIPT_FRONTEND_OUTPUT, JAVASCRIPT_FRONTEND_EXPECT_FILE, create_and_compare, ROOT_DIR  # noqa: E501
import os
from subprocess import call


def test_create_python_file():
    create_and_compare(
        CreaterJavaScriptFrontEnd,
        JAVASCRIPT_FRONTEND_OUTPUT,
        JAVASCRIPT_FRONTEND_EXPECT_FILE)

    return_code = call([
        "node",
        "--experimental-modules",
        "tests/javascript/generated_frontend.test.mjs"])
    assert return_code == 0

    print('[passed] remove typescript frontend output: ',
          JAVASCRIPT_FRONTEND_OUTPUT)
    os.remove(JAVASCRIPT_FRONTEND_OUTPUT)

    os.chdir(ROOT_DIR)
