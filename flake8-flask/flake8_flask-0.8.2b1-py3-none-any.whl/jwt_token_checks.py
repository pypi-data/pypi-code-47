import ast
import logging
import sys

from flake8_flask.flask_base_visitor import FlaskBaseVisitor

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stderr)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(handler)


class JWTTokenChecksVisitor(FlaskBaseVisitor):
    name = "r2c-flask-missing-jwt-token"

    jwt_token_message = f"{name} This file has `flask_jwt` imported, but no route is protected with a `@jwt_required` or `@jwt_optional`. Authenticating your API routes using JWT tokens significantly improves security of the data you pass through the APIs."

    reported = False

    def __init__(self):
        super(JWTTokenChecksVisitor, self).__init__()

    def _is_jwt_decorator_present(self, node: ast.FunctionDef) -> bool:
        for decorator in node.decorator_list:
            name = (
                decorator.func.attr
                if isinstance(decorator.func, ast.Attribute)
                else decorator.func.id
            )
            if name == "jwt_required" or name == "jwt_optional":
                return True
        return False

    def _is_route(self, node: ast.FunctionDef) -> bool:
        for decorator in node.decorator_list:
            name = (
                decorator.func.attr
                if isinstance(decorator.func, ast.Attribute)
                else decorator.func.id
            )
            if name == "route":
                return True
        return False

    def _remove_message(self) -> None:
        for node in self.report_nodes:
            if node['message'] == self.jwt_token_message:
                self.report_nodes.remove(node)
                return
    
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        if not self.is_imported("flask_jwt") or not self._is_route(node): return

        if not self.reported:
            self.report_nodes.append(
                {
                    "node": node,
                    "message": self.jwt_token_message,
                }
            )
            self.reported = True
        
        if self._is_jwt_decorator_present(node):
            self._remove_message()
            return
