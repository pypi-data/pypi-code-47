from typing import Optional,Any

class FunctionParameter:
    def __init__(self, name: str, default: Any, arg_type: type):
        self.name = name
        self.default = default
        self.arg_type = arg_type
    
    def to_dict(self):
        return {
            "name": self.name,
            "default": self.default,
            "arg_type": self.arg_type.__name__
        }
