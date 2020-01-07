from flask import Flask
from typing import Any
import os.path

template_dir = os.path.join(os.path.dirname(__file__),"templates")

def get_default_template(template_name: str) -> str:
    filename = os.path.join(template_dir,template_name)
    with open(filename) as f:
        return f.read()


from .index_class_handler import IndexClassHandler
from .class_injector import ClassInjector
from .function_injector import FunctionInjector
from .get_function_injector import GetFunctionInjector
from .post_function_injector import PostFunctionInjector
from .get_schema_function_injector import GetSchemaFunctionInjector
from .path_builder import PathBuilder
from .function_extractor import FunctionExtractor

def inject_class_app(app: Flask,obj: Any):
    function_extractor  = FunctionExtractor()

    get_path_builder    = PathBuilder("/{name}")
    post_path_builder   = PathBuilder("/{name}")
    schema_path_builder = PathBuilder("/{name}/schema")

    get_template_str = get_default_template("function.html")
    preview_image_template_str = get_default_template("preview_image.html")

    index_class_handler = IndexClassHandler(app, function_extractor, get_path_builder, "/", get_default_template("class.html"))
    handlers = [
        GetFunctionInjector(app, get_path_builder, post_path_builder, get_template_str),
        PostFunctionInjector(app, post_path_builder, preview_image_template_str),
        GetSchemaFunctionInjector(app, schema_path_builder)
    ]
    function_injector = FunctionInjector(function_extractor, handlers)

    class_injector = ClassInjector([
        index_class_handler,
        function_injector
    ])

    class_injector.process(obj)
