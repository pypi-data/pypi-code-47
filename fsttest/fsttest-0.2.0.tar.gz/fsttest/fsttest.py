#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess
import sys
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path
from shutil import which
from tempfile import TemporaryDirectory, TemporaryFile
from typing import Dict, List, Generator

import toml
from blessings import Terminal  # type: ignore

from .exceptions import TestCaseDefinitionError, FSTTestError

# ############################### Constants ################################ #

# Exit codes
_EX_BASE = 0x40
EX_NO_TEST_CASES = _EX_BASE + 1
EX_HAS_FAILED_TEST_CASES = _EX_BASE + 2


# ################################ Globals ################################# #

term = Terminal()


# ################################ Classes ################################# #


class TestResults:
    """
    Keeps track of TestResults.
    """

    def __init__(self, passed: int = 0, failed: int = 0) -> None:
        self.n_passed = passed
        self.n_failed = failed

    @property
    def n_total(self) -> int:
        return self.n_passed + self.n_failed

    @property
    def has_test_failures(self) -> bool:
        """
        True if there are any test failures; false, otherwise.
        """
        return self.n_failed > 0

    def count_test_failure(self, message: str) -> None:
        """
        Call this when a test fails.
        """
        self.n_failed += 1
        print(f"{term.red}{message}{term.normal}", file=sys.stderr)

    def count_passed_test(self) -> None:
        self.n_passed += 1

    def update_in_place(self, other: "TestResults") -> "TestResults":
        """
        Updates these results with another results object.
        """

        previous_total = self.n_total

        self.n_passed += other.n_passed
        self.n_failed += other.n_failed

        assert self.n_total == previous_total + other.n_total
        return self


# ############################### Functions ################################ #


def ensure_foma_is_executable() -> None:
    """
    Raises FSTTestError if foma and flookup executables cannot be found.
    """
    if which("foma") is None:
        raise FSTTestError("Could not find foma! Is it it installed?")
    if which("flookup") is None:
        raise FSTTestError("Could not find flookup! Is foma installed?")


def determine_foma_args(raw_fst_description: dict) -> List[str]:
    """
    Given an FST description, this parses it and returns arguments to be
    passed to foma(1) in order to leave the desired tranducer on the top of
    the foma stack.
    """

    # What the TOML looks like:
    #     "fst": {"eval": "phon_rules.xfscript", "regex": "TInsertion"},

    args: List[str] = []

    # First, load whatever needs to be loaded.
    if "eval" in raw_fst_description:
        # Load an XFST script
        file_to_eval = Path(raw_fst_description["eval"])
        assert file_to_eval.exists()
        args += ["-l", str(file_to_eval)]
    elif "fomabin" in raw_fst_description:
        # Load a fomabin
        path = Path(raw_fst_description["fomabin"])
        assert path.exists()
        args += ["-e", f"load stack {path}"]
    else:
        raise FSTTestError(f"Don't know how to read FST from: {raw_fst_description}")

    # TODO: implement other forms of loading the fst

    if "regex" in raw_fst_description:
        regex = raw_fst_description["regex"]
        assert isinstance(regex, str)
        args += ["-e", f"regex {regex};"]
    elif "compose" in raw_fst_description:
        compose = raw_fst_description["compose"]
        assert isinstance(compose, list)
        # .o. is the compose regex operation
        regex = " .o. ".join(compose)
        args += ["-e", f"regex {regex};"]
    # else, it uses whatever is on the top of the stack.

    return args


@contextmanager
def load_fst(fst_desc: dict) -> Generator[Path, None, None]:
    """
    Loads an FST and yields its path. When finished using the FST, the path
    may no longer be used. Intended to be used in a with-statement:

        with load_fst({"eval": "./path/to/script.xfscript"}) as fst_path:
            ... # use fst_path
    """
    foma_args = determine_foma_args(fst_desc)

    with TemporaryDirectory() as tempdir:
        # Compile the FST first...
        base = Path(tempdir)
        fst_path = base / "tmp.fomabin"
        status = subprocess.check_call(
            ["foma", *foma_args, "-e", f"save stack {fst_path!s}", "-s"]
        )
        yield fst_path


def run_test_suite_from_filename(test_file: Path) -> TestResults:
    """
    Given a file path, parses the test suite, and runs all of the tests
    contained therein.
    """
    # Output looks like this:
    raw_test_case = toml.load(test_file)

    results = TestResults()

    fst_desc = raw_test_case["fst"]
    with load_fst(fst_desc) as fst_path:
        # Raw test cases look like this:
        # {
        #     "tests": [
        #         {"upper": "ki<ajan", "expect": "kitajan"},
        #         {"upper": "ni<ajan", "expect": "nitajan"},
        #     ],
        # }
        for test_case in raw_test_case["tests"]:
            results_from_test_case = execute_test_case(fst_path, test_case)
            results.update_in_place(results_from_test_case)

    return results


def run_tests(test_dir: Path) -> None:
    """
    Run all tests in the given test directory path.

    Files that are tested match the glob pattern:

        test_*.toml

    e.g.,

     * test_vai_inflection.toml
     * test_t_epenthesis.toml
     * test_analyze_noun.toml

    are all tests that will be matched.
    """

    ensure_foma_is_executable()

    results = TestResults()

    tests = test_dir.glob("test_*.toml")
    for test_file in tests:
        results_from_test_suite = run_test_suite_from_filename(test_file)
        results.update_in_place(results_from_test_suite)

    if results.has_test_failures:
        print(f"💥 {term.red}Failed {results.n_failed} test cases{term.normal} 😭😭😭")
        print(f"{term.bold}({results.n_passed}/{results.n_total}) passed{term.normal}")
        sys.exit(EX_HAS_FAILED_TEST_CASES)
    elif results.n_total == 0:
        print(f"{term.red}No FST test cases found.{term.normal} 🤔")
        sys.exit(EX_NO_TEST_CASES)
    else:
        print(
            f"{term.bold}{results.n_passed}/{results.n_total} tests passed!{term.normal} ✨ 🍰 ✨"
        )


def execute_test_case(fst_path: Path, test_case: dict) -> TestResults:
    """
    Execute a test case from its raw dictionary.
    """

    if "expect" not in test_case:
        raise TestCaseDefinitionError('Missing "expect" in test case')
    expected = test_case["expect"]

    if "upper" in test_case:
        inverted = True
        fst_input = test_case["upper"]
    elif "lower" in test_case:
        inverted = False
        fst_input = test_case["lower"]
    else:
        raise TestCaseDefinitionError('Missing "upper" or "lower" in test case')

    # Do the lookup
    if inverted:
        flookup_flags = ["-i"]
    else:
        flookup_flags = []

    with create_temporary_input_file(contents=fst_input) as input_file:
        output = subprocess.check_output(
            ["flookup", *flookup_flags, str(fst_path)],
            encoding="UTF-8",
            stdin=input_file,
        )

    results = TestResults()

    transductions = parse_lookup_output(output)
    assert fst_input in transductions, f"Expected to find {fst_input} in {output}"

    actual_transductions = transductions[fst_input]
    if expected in actual_transductions:
        results.count_passed_test()
    else:
        # Test case failure
        results.count_test_failure(
            f"Failure:\n"
            f"  Given: {fst_input!r}\n"
            f"  Expected: {expected!r}\n"
            f"  Instead, got: {actual_transductions!r}"
        )

    if results.n_total == 0:
        raise FSTTestError("Could not match input with output")
    else:
        return results


def parse_lookup_output(raw_output: str) -> Dict[str, List[str]]:
    """
    Output from lookup, hfst-lookup and flookup is formatted as one
    transduction per line, with tab-separated values.

    Each line is formatted like this:

        {input}␉{transduction}

    If the FST is weighted, it will look like this:

        {input}␉{transduction}␉{weight}

    e.g.,

        eats    eat+Verb+3Person+Present
        eats    eat+Noun+Mass

    e.g., with weights:

        eats    eat+Verb+3Person+Present    0.54301
        eats    eat+Noun+Mass               7.63670

    If multiple strings are given as input, a blank line will (usually)
    separate transductions.

    If a transduction fails (cannot be analyzed), the transduction will be
    `+?` and the weight (if present) will be infinity.

    e.g.,

        fhqwhgads    +?      inf

    """

    results: Dict[str, List[str]] = defaultdict(list)

    for line in raw_output.splitlines():
        if not line.strip():
            # Ignore empty lines
            continue

        input_side, output_side, *_weight = line.lstrip().split("\t")
        results[input_side].append(output_side)

    return results


@contextmanager
def create_temporary_input_file(contents: str):
    with TemporaryFile(mode="w+", encoding="UTF-8") as input_file:
        input_file.write(contents)
        input_file.write("\n")
        input_file.seek(0)
        yield input_file
