import ast


class MyNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_ClassDef(self, node: ast.ClassDef):
        for i, expr in enumerate(node.body):
            # docstring is OK
            if i == 0:
                continue

            if isinstance(expr, ast.Expr):
                value = expr.value
                if isinstance(value, ast.Str):
                    self.errors.append((expr.lineno, node.col_offset, "B000: block comment except docstring found"))

        return super().generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        for i, expr in enumerate(node.body):
            # docstring is OK
            if i == 0:
                continue

            if isinstance(expr, ast.Expr):
                value = expr.value
                if isinstance(value, ast.Str):
                    self.errors.append((expr.lineno, node.col_offset, "B000: block comment except docstring found"))

        return super().generic_visit(node)


class BlockCommentChecker(object):
    name = 'flake8-block-comment'
    version = '0.0.1'

    def __init__(self, tree: ast.Module, filename):
        self.tree = tree
        self.filename = filename

    def run(self):
        visitor = MyNodeVisitor()
        visitor.visit(self.tree)
        for error in visitor.errors:
            yield (*error, type(self))
