from __future__ import absolute_import
from create_multi_langs.creater.javascript_backend import CreaterJavaScriptBackEnd  # noqa: E501
from . import JAVASCRIPT_BACKEND_OUTPUT, JAVASCRIPT_BACKEND_EXPECT_FILE, create_and_compare, ROOT_DIR  # noqa: E501
import os
from subprocess import call


def test_create_python_file():
    create_and_compare(
        CreaterJavaScriptBackEnd,
        JAVASCRIPT_BACKEND_OUTPUT,
        JAVASCRIPT_BACKEND_EXPECT_FILE)

    return_code = call([
        "node",
        "--experimental-modules",
        "tests/javascript/generated_backend.test.mjs"])
    assert return_code == 0

    print('[passed] remove typescript frontend output: ',
          JAVASCRIPT_BACKEND_OUTPUT)
    os.remove(JAVASCRIPT_BACKEND_OUTPUT)

    os.chdir(ROOT_DIR)
