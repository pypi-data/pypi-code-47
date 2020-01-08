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
from typing import Optional, Tuple

from pytesting_utils import virtualenv

from testrunner.runners.abstract_runner import AbstractRunner, RunResult


class SetupPyRunner(AbstractRunner):
    """Implements a runner for setup.py"""

    def __init__(self, project_name: str, path: str, time_limit: int = 0,) -> None:
        super().__init__(project_name, path)
        self._time_limit = time_limit

    def run(self) -> Optional[Tuple[str, str]]:
        setup_py = os.path.join(self._path, "setup.py")
        if not os.path.exists(setup_py) and not os.path.isfile(setup_py):
            return None

        with virtualenv(self._project_name) as env:
            old_dir = os.getcwd()
            os.chdir(self._path)
            packages = self._extract_necessary_packages()
            env.add_packages_for_installation(packages)
            env.add_package_for_installation("benchexec")

            if self._time_limit > 0:
                command = "runexec --timelimit={}s -- ".format(self._time_limit)
            else:
                command = "runexec -- "
            command += "python setup.py test"
            out, err = env.run_commands([command])
            if os.path.exists(
                os.path.join(os.getcwd(), "output.log")
            ) and os.path.isfile(os.path.join(os.getcwd(), "output.log")):
                with open(os.path.join(os.getcwd(), "output.log")) as out_file:
                    out += "\n".join(out_file.readlines())

            os.chdir(old_dir)
            return out, err

    def get_run_result(self, log: str) -> RunResult:
        raise NotImplementedError("Implement me!")
