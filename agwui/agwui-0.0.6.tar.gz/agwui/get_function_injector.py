from flask import Flask, render_template_string
from .class_injector import ClassInjector
from typing import Any
from .FunctionDefinition import make_function_definition
from .path_builder import PathBuilder

class GetFunctionInjector(ClassInjector):
    def __init__(self, app: Flask, get_path_builder: PathBuilder, post_path_builder: PathBuilder, get_template_str: str):
        self.app = app
        self.get_template_str = get_template_str
        self.get_path_builder = get_path_builder
        self.post_path_builder = post_path_builder

    def process(self, obj: Any):
        function_definition = make_function_definition(obj)
   
        def get():
            return render_template_string(
                self.get_template_str,
                action_path=self.post_path_builder.build(function_definition.name),
                function_definition=function_definition.to_dict()
            )
        get.__name__ = "%s_get" % function_definition.name
        self.app.route(self.get_path_builder.build(function_definition.name), methods=["GET"])(get)
