"""
Provides Flake8 plugin to check for arguments that aren't passed by keyword.

References:
    - https://docs.python.org/3/library/ast.html
    - https://flake8.pycqa.org/en/latest/plugin-development/
    - https://github.com/asottile/flake8-2020
"""
import ast
import builtins
from typing import (
    Any,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
)

ERROR_CODE = 'KWA'
ERROR_DESCRIPTION = 'argument is not passed by keyword.'
ERROR_MESSAGE = f'{ERROR_CODE}: {ERROR_DESCRIPTION}'

ALLOWED_TO_NOT_KWARGS = set(dir(builtins) + dir(list))


class Visitor(ast.NodeVisitor):
    """
    Node visitor implementation.

    Checks call for arguments that aren't passed by keywords.
    """

    def __init__(self) -> None:
        """
        Construct the object.
        """
        self.errors: List[Tuple[int, int, str]] = []

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802
        """
        Visit a Call node.

        Arguments:
            node: the Call node.
        """
        if not self._is_allowed(call_node=node) and self._has_arguments_not_passed_by_keyword(call_node=node):
            self.errors.append(
                (node.lineno, node.col_offset, ERROR_MESSAGE),
            )

        self.generic_visit(node=node)

    def _is_allowed(self, call_node: ast.Call) -> bool:
        """
        Check if a Call node is allowed to have arguments not passed by keyword.

        Arguments:
            call_node(ast.Node): the argument to check.

        Returns:
            True if call node is allowed to have arguments not passed by keyword.
        """
        func = call_node.func

        if isinstance(func, ast.Name):
            func_name: Optional[str] = func.id

        elif isinstance(func, ast.Attribute):
            func_name = func.attr

        else:
            func_name = None

        return func_name in ALLOWED_TO_NOT_KWARGS

    def _has_arguments_not_passed_by_keyword(self, call_node: ast.Call) -> bool:
        """
        Check if a Call node has arguments not passed by keyword.

        In the AST those are represented with the symbol args.

            Call(expr func, expr* args, keyword* keywords)

        Therefore, the call has arguments not passed by keyword if the list of
        expressions in the args symbol is non empty.

        Arguments:
            call_node: the call node.

        References:
            - https://docs.python.org/3/library/ast.html#abstract-grammar

        Returns:
            True if the call has arguments not passed by keyword.
        """
        return len(call_node.args) > 0


class Plugin:
    """
    Plugin implementation.

    Checks for arguments that aren't passed by keyword.
    """

    name = 'flake8_kw_args'
    version = '0.0.1'

    def __init__(self, tree: ast.AST):
        """
        Construct the object.
        """
        self._tree = tree
        self._visitor = Visitor()

    def run(self) -> Iterable[Tuple[int, int, str, Type[Any]]]:
        """
        Run the plugin.
        """
        self._visitor.visit(node=self._tree)

        for line, col, error in self._visitor.errors:
            yield line, col, error, type(self)
