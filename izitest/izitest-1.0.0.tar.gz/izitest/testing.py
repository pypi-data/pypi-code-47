# -*- coding: utf-8 -*-

from typing import List, TextIO

from dataclasses import (dataclass, field)

from sys import stdout, stderr
from sys import exit

from pathlib import Path

import subprocess as sp

import yaml  # pylint: disable=import-error

import izitest.tests
from izitest.prettyprint import (prettyprint, Color)
from izitest.parser import parse_args


__all__ = [
    "discover_testsuite",
    "run_test",
    "run_testcase",
    "run_testsuite"
]


def __run_exec(path: str, args: List[str], stdin: str, timeout: int = 1) -> sp.CompletedProcess:
    """Run an executable.

    Args:
        path (str): path to the executable (can be relative to PATH env)
        args (List[str]): list of arguments (can be empty)
        stdin (str): input of the program
        timeout (int, optional): timeout (in sec). Defaults to 1

    Returns:
        sp.CompletedProcess: the completed process.

    Raises:
        sp.TimeoutExpired: if the timeout expired.
    """
    try:
        return sp.run([path] + args, input=stdin,
                      capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        return sp.run([Path(path).absolute()] + args, input=stdin,
                      capture_output=True, text=True, timeout=timeout)


def __fake_run_exec(expect: dict) -> sp.CompletedProcess:
    """Fake the run of an executable.

    Args:
        expect (dict): a dictionnary containing the expected outputs (stdout, stderr, retcode)

    Returns:
        sp.CompletedProcess: a completed process, as if it was run by sp.run()
    """
    fake_stdout = expect.get("stdout", '')
    fake_stderr = expect.get("stderr", '')
    fake_retcode = expect.get("retcode", 0)

    return sp.CompletedProcess('', fake_retcode, fake_stdout, fake_stderr)


def discover_testsuite(path: Path, categories: List[str] = None) -> List[Path]:
    """Returns a list of discovered tests files that match given categories/filters (if any)

    Args:
        path (Path): path of the test suite directory
        categories (List[str], optional): categories/filters - only the files that match (at least)
        one of them will be explored

    Returns:
        List[Path]: list of discovered tests files
    """

    prettyprint("Discovering test suite...", Color.GREEN, end="\n\n")

    # Must be sorted using str (string representation) to have a 'tree-like' order
    yamlfiles: List[Path] = sorted(path.rglob("*.yaml"), key=str)

    testsfiles: List[Path] = []

    if categories is None:
        testsfiles = yamlfiles
    else:
        for f in yamlfiles:
            if any(c in str(f) for c in categories):
                testsfiles.append(f)

    return testsfiles


def run_test(fn_name: str, ref: sp.CompletedProcess, test: sp.CompletedProcess) -> (bool, str):
    """Run the test named `fn_name` (located in izitest.tests).

    Args:
        fn_name (str): name of the test function
        ref (sp.CompletedProcess): reference executable
        test (sp.CompletedProcess): tested executable

    Returns:
        bool: True if the test succeed, False otherwise
        str: diff between two outputs
    """

    fn_test = getattr(izitest.tests, fn_name)
    return fn_test(ref, test)


def run_testcase(testcase: dict, exec: Path, args: List[str], ref: Path = None, refargs: List[str] = None):
    tests: List[str] = testcase.get("tests", None)
    if tests is None:
        prettyprint("No test to run...", Color.CYAN, bold=False, indent=3, end=' ')
        prettyprint("Skipped", Color.YELLOW)
        return

    add_args: str = testcase.get("args", None)
    args += add_args

    if refargs is not None:
        refargs += add_args

    stdin: str = testcase.get("stdin", '')

    expect: dict = testcase.get("expect", None)

    try:
        if expect is None:
            if ref is None:
                prettyprint("No ref executable provided...", Color.MAGENTA, bold=False, indent=3, end=' ')
                prettyprint("Skipped", Color.RED)
                return

            ref_proc = __run_exec(ref, refargs, stdin)
        else:
            ref_proc = __fake_run_exec(expect)

        test_proc: sp.CompletedProcess = __run_exec(exec, args, stdin)
    except sp.TimeoutExpired:
        prettyprint("Timeout expired!", Color.MAGENTA, bold=False, indent=2, end=' ')
        prettyprint("Skipped", Color.YELLOW)
        return

    for test in tests:
        prettyprint(test, Color.CYAN, bold=False, indent=3, end=' ')

        passed: bool
        diff: str
        passed, diff = run_test(test, ref_proc, test_proc)
        if passed:
            prettyprint("Passed", Color.GREEN)
        else:
            prettyprint("Failed", Color.RED)
            if diff != '':
                print(diff)


def run_testsuite(args):
    testfiles: List[Path] = discover_testsuite(args.testdir, args.cat)

    prettyprint("Running test suite:")
    for path in testfiles:
        testdir: str = path.parts[0]
        prettyprint(f"Running tests in {path.relative_to(testdir)}:", Color.BLUE, indent=1)
        try:
            with open(path, 'r') as f:
                tests: dict = yaml.safe_load(f.read())
        except Exception:
            prettyprint(f"Failed to load test file {path}!", Color.RED, stderr, indent=2)

        if tests is None:
            prettyprint("Empty file...", Color.CYAN, bold=False, indent=2, end=' ')
            prettyprint("Skipped", Color.YELLOW)
            continue

        for testcase in tests:
            if testcase.get("name", None) is None:
                continue

            prettyprint(f"{testcase['name']}", Color.CYAN, indent=2)

            if not testcase.get("skip", False):
                run_testcase(testcase, args.exec[0], args.exec[1:], args.ref[0], args.ref[1:])
            else:
                prettyprint("Test is disabled...", Color.CYAN, bold=False, indent=3, end=' ')
                prettyprint("Skipped", Color.YELLOW)
