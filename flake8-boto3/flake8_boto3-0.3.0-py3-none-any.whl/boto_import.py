import ast
from ast import Attribute
import astunparse
import inspect

from flake8_boto3 import __version__

INVALID_IMPORT_NAME = "boto"


class CheckInvalidBotoImport(object):
    name = "r2c-use-boto3-over-boto"
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        visitor = CodeVisitor()
        visitor.visit(self.tree)

        for warning in visitor.warnings:
            yield (
                warning.lineno,
                warning.col_offset,
                self._message_for(warning),
                "CheckInvalidBotoImport",
            )

    def _message_for(self, warning):
        return f"{self.name} Detected an import of boto instead of boto3: {astunparse.unparse(warning)}"


class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.warnings = []

    def visit_Import(self, s):
        names = s.names
        for fqn in names:
            if fqn.name == INVALID_IMPORT_NAME:
                self.warnings.append(s)

    def visit_ImportFrom(self, import_from: ast.ImportFrom):
        if import_from.module == INVALID_IMPORT_NAME:
            self.warnings.append(import_from)
