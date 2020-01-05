import os

ROOT_DIR = os.path.abspath(os.curdir)
CSV_FILE = os.path.join(ROOT_DIR, "data/valid_format.csv")
GO_OUTPUT = os.path.join(ROOT_DIR, "tests/go/generated.go")
GO_EXPECT_FILE = os.path.join(ROOT_DIR, "data/go/expect.go")
PYTHON_OUTPUT = os.path.join(ROOT_DIR, "tests/python/generated.py")
PYTHON_EXPECT_FILE = os.path.join(ROOT_DIR, "data/python/expect.py")
PYTHON_TYPING_OUTPUT = os.path.join(
    ROOT_DIR, "tests/python/generated_typing.py")
PYTHON_TYPING_EXPECT_FILE = os.path.join(
    ROOT_DIR, "data/python/expect_typing.py")
TYPESCRIPT_FRONTEND_OUTPUT = os.path.join(
    ROOT_DIR,
    "tests/typescript/generated_frontend.ts")
TYPESCRIPT_FRONTEND_EXPECT_FILE = os.path.join(
    ROOT_DIR,
    "data/typescript/expect_frontend.ts")
JAVASCRIPT_FRONTEND_OUTPUT = os.path.join(
    ROOT_DIR,
    "tests/javascript/generated_frontend.mjs")
JAVASCRIPT_FRONTEND_EXPECT_FILE = os.path.join(
    ROOT_DIR,
    "data/javascript/expect_frontend.js")
TYPESCRIPT_BACKEND_OUTPUT = os.path.join(
    ROOT_DIR,
    "tests/typescript/generated_backend.ts")
TYPESCRIPT_BACKEND_EXPECT_FILE = os.path.join(
    ROOT_DIR,
    "data/typescript/expect_backend.ts")
JAVASCRIPT_BACKEND_OUTPUT = os.path.join(
    ROOT_DIR,
    "tests/javascript/generated_backend.mjs")
JAVASCRIPT_BACKEND_EXPECT_FILE = os.path.join(
    ROOT_DIR,
    "data/javascript/expect_backend.js")


def compare_file(expect_file: str, result_file: str):
    expects = open(expect_file, 'r', encoding='utf8').read().split('\n')
    results = open(result_file, 'r', encoding='utf8').read().split('\n')
    err = ""
    for i, expect in enumerate(expects):
        try:
            if results[i] != expect:
                err += "[Different LINE {}] expect v.s. result:\n'{}'\n'{}'\n".format(  # noqa E501
                    i+1, expect, results[i]
                )
        except IndexError:
            err += "[Different File Lines] expect: {}, but got {}\n".format(
                len(expects), len(results)
            )
            break

    assert not err, err


def create_and_compare(creater_class, output_file, expect_file):
    creater = creater_class.from_csv_file(CSV_FILE, output_file)
    creater()
    compare_file(expect_file, output_file)
