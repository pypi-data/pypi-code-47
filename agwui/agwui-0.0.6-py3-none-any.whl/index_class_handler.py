from .class_handler import ClassHandler
from flask import Flask, render_template_string
from .FunctionDefinition import make_function_definition
from .path_builder import PathBuilder
from .function_extractor import FunctionExtractor
from typing import Any
from inspect import getdoc

class IndexClassHandler(ClassHandler):
    def __init__(self, app:Flask, function_extractor: FunctionExtractor, get_path_builder: PathBuilder, path: str, template: str):
        self.app = app
        self.path = path
        self.template = template
        self.get_path_builder = get_path_builder
        self.function_extractor = function_extractor

    def process(self, obj: Any):
        name = obj.__class__.__name__
        description = getdoc(obj)

        functions = self.function_extractor.extract(obj)
        function_entrypoints = [
            {
                "path": self.get_path_builder.build(definition.name),
                "definition": definition
            }
            for definition
            in map(
                make_function_definition,
                functions
            )
        ]

        @self.app.route(self.path)
        def index():
            return render_template_string(
                self.template,
                name=name,
                description=description,
                function_entrypoints = function_entrypoints
            )
