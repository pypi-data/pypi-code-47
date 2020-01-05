import ast
from ast import Attribute
import astunparse
import inspect

from flake8_boto3 import __version__

BOTO3_NAME = "boto3"
CLIENT_DEPRECATED_METHOD_NAMES = ["list_objects", "put_bucket_lifecycle"]


class CheckDeprecatedAPI(object):
    name = "r2c-boto3-dont-use-deprecated-api"
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        visitor = CodeVisitor()
        visitor.visit(self.tree)

        if visitor.using_boto3:
            warnings = visitor.warnings
        else:
            warnings = (
                []
            )  # must be a false positive because not importing boto3 (better than a dumb grep)

        for warning in warnings:
            yield (
                warning.lineno,
                warning.col_offset,
                self._message_for(warning),
                "CheckDeprecatedAPI",
            )

    def _message_for(self, warning):
        return (
            f"{self.name} Use of Deprecated API Detected: {astunparse.unparse(warning)}"
        )


class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.warnings = []
        self.using_boto3 = False

    def visit_Call(self, call):
        if type(call.func) == Attribute:
            if call.func.attr in CLIENT_DEPRECATED_METHOD_NAMES:
                self.warnings.append(call)

    def visit_Import(self, s):
        names = s.names
        for fqn in names:
            if fqn.name == BOTO3_NAME:
                self.using_boto3 = True

    def visit_ImportFrom(self, import_from: ast.ImportFrom):
        if import_from.module == BOTO3_NAME:
            self.using_boto3 = True
