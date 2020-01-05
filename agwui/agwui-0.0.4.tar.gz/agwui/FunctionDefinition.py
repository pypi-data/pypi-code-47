from typing import List,Optional,Callable,Any
from .FunctionParameter import FunctionParameter
from inspect import signature,getdoc,Parameter

class FunctionDefinition:
    def __init__(self, name: str, description: Optional[str], return_type: type, parameters: List[FunctionParameter]):
        self.name = name
        self.description = description
        self.return_type = return_type
        self.parameters = parameters

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "return_type": self.return_type.__name__,
            "parameters": list(map(lambda x:x.to_dict(),self.parameters))
        }

def make_function_definition(function: Callable[...,Any]) -> FunctionDefinition:
    name = function.__name__
    description = getdoc(function)
    function_signature = signature(function)
    return_type = function_signature.return_annotation

    return FunctionDefinition(
        name,
        description,
        return_type,
        [
            FunctionParameter(name, parameter.default if parameter.default != Parameter.empty else None, parameter.annotation)
            for (name,parameter)
            in function_signature.parameters.items()   
        ]
    )