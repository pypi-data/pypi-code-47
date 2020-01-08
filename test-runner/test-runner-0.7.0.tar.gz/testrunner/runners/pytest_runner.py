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
import re
from typing import Union, Optional, Tuple

from pytesting_utils import virtualenv
from setuptools import find_packages  # type: ignore

from testrunner.runners.abstract_runner import AbstractRunner, RunResult


class PyTestRunner(AbstractRunner):
    """A runner for pytest"""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        project_name: str,
        path: str,
        time_limit: int = 0,
        junit_xml_file: Union[str, os.PathLike] = None,
        venv_path: Union[bytes, str, os.PathLike] = None,
    ) -> None:
        super().__init__(project_name, path)
        self._time_limit = time_limit
        self._junit_xml_file = junit_xml_file
        self._venv_path = venv_path

    def run(self) -> Optional[Tuple[str, str]]:
        # TODO make sure nothing goes wrong here

        with virtualenv(self._project_name, self._venv_path) as env:
            old_dir = os.getcwd()
            os.chdir(self._path)

            if "-" in self._project_name and os.path.exists(
                os.path.join(os.getcwd(), self._project_name.replace("-", ""))
            ):
                project_name = self._project_name.replace("-", "")
            elif "_" in self._project_name and os.path.exists(
                os.path.join(os.getcwd(), self._project_name.replace("_", ""))
            ):
                project_name = self._project_name.replace("_", "")
            elif "-" in self._project_name and os.path.exists(
                os.path.join(os.getcwd(), self._project_name.replace("-", "_"))
            ):
                project_name = self._project_name.replace("-", "_")
            elif os.path.exists(os.path.join(os.getcwd(), self._project_name)):
                project_name = self._project_name
            else:
                directories = find_packages(".", exclude=["test", "tests"])
                if len(directories) == 0 and os.path.exists(
                    os.path.join(os.getcwd(), "src")
                ):
                    directories = find_packages("src", exclude=["test", "tests"])
                project_name = directories[0] if len(directories) > 1 else "."

            packages = self._extract_necessary_packages()
            env.add_packages_for_installation(packages)
            env.add_package_for_installation("pytest")
            env.add_package_for_installation("pytest-cov")
            env.add_package_for_installation("benchexec==1.22")

            if self._time_limit > 0:
                command = "runexec --no-container --timelimit={}s -- ".format(
                    self._time_limit
                )
            else:
                command = "runexec --no-container -- "
            command += "pytest --cov={} --cov-report=term-missing".format(project_name)
            if self._junit_xml_file is not None:
                command += " --junitxml={}".format(self._junit_xml_file)

            out, err = env.run_commands([command])
            if os.path.exists(
                os.path.join(os.getcwd(), "output.log")
            ) and os.path.isfile(os.path.join(os.getcwd(), "output.log")):
                with open(os.path.join(os.getcwd(), "output.log")) as out_file:
                    out += "\n".join(out_file.readlines())
            os.chdir(old_dir)
            return out, err

    def get_run_result(self, log: str) -> RunResult:
        statements = -1
        missing = -1
        coverage = -1.0
        failed = -1
        passed = -1
        skipped = -1
        warnings = -1
        error = -1
        time = -1.0

        matches = re.search(
            r"[=]+ (([0-9]+) failed, )?"
            r"([0-9]+) passed"
            r"(, ([0-9]+) skipped)?"
            r"(, ([0-9]+) warnings)?"
            r"(, ([0-9]+) error)?"
            r" in ([0-9.]+) seconds",
            log,
        )
        if matches:
            failed = int(matches.group(2)) if matches.group(2) else 0
            passed = int(matches.group(3)) if matches.group(3) else 0
            skipped = int(matches.group(5)) if matches.group(5) else 0
            warnings = int(matches.group(7)) if matches.group(7) else 0
            error = int(matches.group(9)) if matches.group(9) else 0
            time = float(matches.group(10)) if matches.group(10) else 0.0

        matches = re.search(
            r"TOTAL\s+"
            r"([0-9]+)\s+"
            r"([0-9]+)\s+"
            r"(([0-9]+)\s+([0-9]+)\s+)?"
            r"([0-9]+%)",
            log,
        )
        if matches:
            statements = int(matches.group(1)) if matches.group(1) else 0
            missing = int(matches.group(2)) if matches.group(2) else 0
            coverage = float(matches.group(6)[:-1]) if matches.group(6) else 0.0
        else:
            matches = re.search(
                r".py\s+"
                r"([0-9]+)\s+"
                r"([0-9]+)\s+"
                r"(([0-9]+)\s+([0-9]+)\s+)?"
                r"([0-9]+%)",
                log,
            )
            if matches:
                statements = int(matches.group(1)) if matches.group(1) else 0
                missing = int(matches.group(2)) if matches.group(2) else 0
                coverage = float(matches.group(6)[:-1]) if matches.group(6) else 0.0

        result = RunResult(
            statements=statements,
            missing=missing,
            coverage=coverage,
            failed=failed,
            passed=passed,
            skipped=skipped,
            warnings=warnings,
            error=error,
            time=time,
            runner="pytest",
        )
        return result
