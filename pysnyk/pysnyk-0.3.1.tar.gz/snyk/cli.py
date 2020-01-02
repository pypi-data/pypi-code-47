import json
import shutil
from dataclasses import dataclass
from typing import Optional

import attr

import delegator  # type: ignore

from .errors import SnykNotFoundError, SnykRunError


def _check_for_snyk(func):
    def check(*args, **kwargs):
        if not shutil.which("snyk") is not None:
            raise SnykNotFoundError
        return func(*args, **kwargs)

    return check


@attr.s(auto_attribs=True)
class SnykCLI(object):
    directory: str

    def run(self, args):
        command = delegator.run(f"conftest {args}")
        try:
            results = ConftestResult.schema().loads(command.out, many=True)
        except json.decoder.JSONDecodeError as e:
            error_message = command.err.split("msg=")[-1].strip('"')
            raise ConftestRunError(error_message) from e
        return ConftestRun(code=command.return_code, results=results)

    @_check_for_snyk
    def test(self, args: List[str] = []):
        args_str = " ".join(args)
        return self.run(f"test --json {args_str}")
