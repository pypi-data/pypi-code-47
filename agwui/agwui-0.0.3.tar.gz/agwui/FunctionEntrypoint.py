from .FunctionDefinition import FunctionDefinition

class FucntionEntrypoint:
    def __init__(self, path: str, schema_path: str, function_definition: FunctionDefinition):
        self.path = path
        self.schema_path = schema_path
        self.function_definition = function_definition

def make_function_entrypoint(function_definition: FunctionDefinition) -> FucntionEntrypoint:
    path = "/" + function_definition.name
    schema_path = path + "/schema"
    return FucntionEntrypoint(
        path,
        schema_path,
        function_definition
    )