from flask import Flask, jsonify
from .class_injector import ClassInjector
from typing import Any
from .FunctionDefinition import make_function_definition
from .path_builder import PathBuilder

class GetSchemaFunctionInjector(ClassInjector):
    def __init__(self, app: Flask, path_builder: PathBuilder):
        self.app = app
        self.path_builder = path_builder

    def process(self, obj: Any):
        function_definition = make_function_definition(obj)

        def get_schema():
            return jsonify(
                function_definition.to_dict()
            )
        get_schema.__name__ = "%s_get_schema" % function_definition.name
        self.app.route(self.path_builder.build(function_definition.name))(get_schema)