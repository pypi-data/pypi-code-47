from typing import List, Any
from .FunctionDefinition import FunctionDefinition
from .class_handler import ClassHandler

class ClassInjector:
    def __init__(self,handlers: List[ClassHandler]):
        self.handlers = handlers

    def process(self, obj: Any):
        for handler in self.handlers:
            handler.process(obj)
