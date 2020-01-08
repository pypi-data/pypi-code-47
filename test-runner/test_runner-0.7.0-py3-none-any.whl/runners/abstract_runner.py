"""
Test runner is a library for running unit tests on Python code.

It offers the opinion to automatically detect the correct run settings for
the tests and gives information about the test results and coverage information.

Test-Runner is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test-Runner is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Test-Runner.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
from abc import ABCMeta, abstractmethod
from typing import List, Optional, Tuple

import attr
import pipfile  # type: ignore
from pytesting_utils import Preconditions


# pylint: disable=too-many-instance-attributes,too-few-public-methods
@attr.s
class RunResult:
    """A data class to store run results"""

    statements: int = attr.ib(default=-1)
    missing: int = attr.ib(default=-1)
    coverage: float = attr.ib(default=-1.0)
    failed: int = attr.ib(default=-1)
    passed: int = attr.ib(default=-1)
    skipped: int = attr.ib(default=-1)
    warnings: int = attr.ib(default=-1)
    error: int = attr.ib(default=-1)
    time: float = attr.ib(default=-1.0)
    runner: str = attr.ib(default="")


class AbstractRunner(metaclass=ABCMeta):
    """An abstract base class for test runners."""

    def __init__(self, project_name: str, path: str) -> None:
        Preconditions.check_argument(
            len(project_name) > 0, "Project name must not be empty!"
        )
        Preconditions.check_argument(len(path) > 0, "Path must not be empty!")
        self._project_name = project_name
        self._path = path

    @abstractmethod
    def run(self) -> Optional[Tuple[str, str]]:
        """Runs the tests using the test runners.

        The result is a tuple of normal output and error output, if created
        """

    @abstractmethod
    def get_run_result(self, log: str) -> RunResult:
        """Generates a run result for a log string"""

    def _extract_necessary_packages(self) -> List[str]:
        packages: List[str] = []
        file_names = [
            "requirements.txt",
            "dev-requirements.txt",
            "dev_requirements.txt",
            "test-requirements.txt",
            "test_requirements.txt",
            "requirements-dev.txt",
            "requirements_dev.txt",
            "requirements-test.txt",
            "requirements_test.txt",
        ]
        for file_name in file_names:
            packages.extend(self._extract_packages(os.path.join(self._path, file_name)))
        if os.path.exists(os.path.join(self._path, "Pipfile")) and os.path.isfile(
            os.path.join(self._path, "Pipfile")
        ):
            packages.extend(self._extract_packages_from_pipfile())
        return packages

    @staticmethod
    def _extract_packages(requirements_file):
        packages = []
        if os.path.exists(requirements_file) and os.path.isfile(requirements_file):
            with open(requirements_file) as req_file:
                for line in req_file.readlines():
                    if "requirements" in line:
                        continue
                    packages.append(line.strip())
        return packages

    def _extract_packages_from_pipfile(self) -> List[str]:
        packages = []
        pip_file = pipfile.load(os.path.join(self._path, "Pipfile"))
        data = pip_file.data
        if len(data["default"]) > 0:
            for key, _ in data["default"].items():
                packages.append(key)
        if len(data["develop"]) > 0:
            for key, _ in data["develop"].items():
                packages.append(key)
        return packages

    def __str__(self) -> str:
        return "Runner for project {} in path {} (type {})".format(
            self._project_name, self._path, type(self).__name__
        )

    def __repr__(self) -> str:
        return self.__str__()
