from flask import Flask, render_template_string, request, make_response
from .class_injector import ClassInjector
from typing import Any
from .FunctionParameter import FunctionParameter
from .FunctionDefinition import make_function_definition
from .ExtraType import FileType,ImageType
from .path_builder import PathBuilder

def extract_obj(flaskRequest, parameter: FunctionParameter) -> Any:
    if parameter.arg_type == FileType:
        return FileType(flaskRequest.files[parameter.name])
    elif parameter.arg_type == ImageType:
        return ImageType(flaskRequest.files[parameter.name])
    else:
        return (parameter.arg_type)(flaskRequest.form[parameter.name])

class PostFunctionInjector(ClassInjector):
    def __init__(self, app: Flask, path_builder: PathBuilder, preview_image_template_str: str):
        self.app = app
        self.preview_image_template_str = preview_image_template_str
        self.path_builder = path_builder

    def process(self, obj: Any):
        function_definition = make_function_definition(obj)
   
        def post():
            values = [
                extract_obj(request, parameter)
                for parameter
                in function_definition.parameters
            ]

            result = obj(*values)

            if function_definition.return_type == FileType:
                response = make_response()
                response.data = result.file_obj.read()
                response.mimetype = "application/octet-stream"
                return response
            elif function_definition.return_type == ImageType:
                from base64 import b64encode
                b64data = b64encode(result.file_obj.read()).decode()
                ext = result.file_obj.filename.split(".")[-1]
                return render_template_string(
                    self.preview_image_template_str,
                    b64data=b64data,
                    ext=ext
                )
            else:
                return str(result)

        post.__name__ = "%s_post" % function_definition.name
        self.app.route(self.path_builder.build(function_definition.name),methods=["POST"])(post)

