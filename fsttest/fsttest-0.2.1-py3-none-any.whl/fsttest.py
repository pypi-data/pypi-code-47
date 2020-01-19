#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Generator

import toml
from blessings import Terminal  # type: ignore

from ._fst import FST
from .exceptions import FSTTestError, TestCaseDefinitionError

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


@contextmanager
def load_fst(fst_desc: Dict[str, Any]) -> Generator[Path, None, None]:
    return FST._load_fst(fst_desc)


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
        direction = "up"
        fst_input = test_case["upper"]
    elif "lower" in test_case:
        direction = "down"
        fst_input = test_case["lower"]
    else:
        raise TestCaseDefinitionError('Missing "upper" or "lower" in test case')

    # Do the lookup
    with FST.load_from_path(fst_path) as fst:
        transductions = fst.apply([fst_input], direction)

    results = TestResults()
    assert (
        fst_input in transductions
    ), f"Expected to find {fst_input} in {transductions}"

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
