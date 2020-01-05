from __future__ import absolute_import
from create_multi_langs.creater.go import CreaterGo
from . import GO_OUTPUT, GO_EXPECT_FILE, ROOT_DIR, create_and_compare
import os
from subprocess import call


def test_create_go_file():
    create_and_compare(CreaterGo, GO_OUTPUT, GO_EXPECT_FILE)

    print("go test ...")
    os.chdir("tests/go")
    return_code = call(["go", "test"])
    assert return_code == 0

    print('[passed] remove go output: ', GO_OUTPUT)
    os.remove(GO_OUTPUT)

    os.chdir(ROOT_DIR)
