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
from typing import Optional, Tuple

from testrunner.runners.abstract_runner import AbstractRunner, RunResult


class ToxRunner(AbstractRunner):
    """Provides a runner for the tox tool"""

    def run(self) -> Optional[Tuple[str, str]]:
        pass  # pragma: no cover

    def get_run_result(self, log: str) -> RunResult:
        pass  # pragma: no cover
