#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Define the FST class.
"""

import shutil
import subprocess
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory, TemporaryFile
from typing import IO, Any, Dict, Generator, List

from .exceptions import FSTTestError


class FST:
    def __init__(self, foma_args: List[str] = None, existing_path: Path = None):
        self._directory = tempdir = TemporaryDirectory()
        base = Path(tempdir.name)
        self._path = fst_path = base / "tmp.fomabin"

        if foma_args:
            subprocess.check_call(
                ["foma", *foma_args, "-e", f"save stack {fst_path!s}", "-s"]
            )
        elif existing_path:
            shutil.copyfile(existing_path, fst_path)
        else:
            raise ValueError("Must provide some existing FST...")

    def __enter__(self) -> "FST":
        # Note: Intiailization already done in __init__
        return self

    def __exit__(self, _exec_type, _exec, _stack):
        self._directory.cleanup()

    @property
    def path(self) -> Path:
        return self._path

    def apply(self, inputs: List[str], direction: str = "up") -> Dict[str, List[str]]:
        if direction == "down":
            flookup_flags = []
        elif direction == "up":
            flookup_flags = ["-i"]
        else:
            raise ValueError(
                f'direction must be "up" or "down"; got {direction!r} instead'
            )

        assert all("\n" not in inp for inp in inputs)
        fst_input = "\n".join(inputs)
        with create_temporary_input_file(contents=fst_input) as input_file:
            output = subprocess.check_output(
                ["flookup", *flookup_flags, str(self.path)],
                encoding="UTF-8",
                stdin=input_file,
            )

        return parse_lookup_output(output)

    @staticmethod
    def load_from_description(fst_desc: Dict[str, Any]) -> "FST":
        if "fomabin" in fst_desc:
            # Avoid compiling with Foma.
            return FST.load_from_path(fst_desc["fomabin"])

        return FST(foma_args=determine_foma_args(fst_desc))

    @staticmethod
    def _load_fst(fst_desc: Dict[str, Any]) -> Generator[Path, None, None]:
        """
        Loads an FST and yields its path. When finished using the FST, the path
        may no longer be used. Intended to be used in a with-statement:

            with load_fst({"eval": "./path/to/script.xfscript"}) as fst_path:
                ... # use fst_path
        """
        with FST.load_from_description(fst_desc) as fst:
            yield fst.path

    @staticmethod
    def load_from_path(fst_path: Path) -> "FST":
        assert fst_path.exists()
        return FST(existing_path=fst_path)


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
    else:
        raise FSTTestError(f"Don't know how to read FST from: {raw_fst_description}")

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
def create_temporary_input_file(contents: str) -> Generator[IO[str], None, None]:
    """
    Write text to a file, and use it from the beginning.
    """
    with TemporaryFile(mode="w+", encoding="UTF-8") as input_file:
        input_file.write(contents)
        input_file.write("\n")
        input_file.seek(0)
        yield input_file


def ensure_foma_is_executable() -> None:
    """
    Raises FSTTestError if foma and flookup executables cannot be found.
    """
    if shutil.which("foma") is None:
        raise FSTTestError("Could not find foma! Is it it installed?")
    if shutil.which("flookup") is None:
        raise FSTTestError("Could not find flookup! Is foma installed?")
