from flask import Flask, render_template_string, jsonify, request
from typing import Callable,Any
from inspect import getdoc,getmembers,ismethod
from .FunctionDefinition import make_function_definition
from .FunctionEntrypoint import make_function_entrypoint
import os.path

template_dir = os.path.join(os.path.dirname(__file__),"templates")

def render_agwui_template(template_name,**context):
    filename = os.path.join(template_dir,template_name)
    return render_template_string(
        open(filename).read(),
        **context
    )

def inject_function_app(app: Flask,function: Callable[...,Any]):
    function_definition = make_function_definition(function)
    function_entrypoint = make_function_entrypoint(function_definition)

    def get():
        return render_agwui_template(
            "function.html",
            action_path=function_entrypoint.path,
            function_definition=function_definition.to_dict()
        )
    get.__name__ = "%s_get" % function_definition.name
    app.route(function_entrypoint.path, methods=["GET"])(get)

    def post():
        values = [
            (parameter.arg_type)(request.form[parameter.name])
            for parameter
            in function_definition.parameters
        ]
        return str(function(*values))
    post.__name__ = "%s_post" % function_definition.name
    app.route(function_entrypoint.path,methods=["POST"])(post)
    
    def get_schema():
        return jsonify(
            function_definition.to_dict()
        )
    get_schema.__name__ = "%s_get_schema" % function_definition.name
    app.route(function_entrypoint.schema_path)(get_schema)


def inject_class_app(app: Flask,obj: Any):
    name = obj.__class__.__name__
    description = getdoc(obj)

    functions = [function for (name,function) in getmembers(obj,predicate=ismethod) if not name.startswith("__")]
    function_entrypoints = [
        make_function_entrypoint(make_function_definition(function))
        for function
        in functions
    ]

    @app.route("/")
    def index():
        return render_agwui_template(
            "class.html",
            name=name,
            description=description,
            function_entrypoints = function_entrypoints
        )

    for function in functions:
        inject_function_app(app,function)