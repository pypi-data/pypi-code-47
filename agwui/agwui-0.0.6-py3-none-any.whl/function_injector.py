from .class_injector import ClassInjector
from .class_handler import ClassHandler
from typing import Any,List
from inspect import getdoc,getmembers,ismethod
from .function_extractor import FunctionExtractor

class FunctionInjector(ClassInjector):
    def __init__(self, function_extractor: FunctionExtractor, handlers: List[ClassHandler]):
        self.function_extractor = function_extractor
        self.handlers = handlers

    def process(self, obj: Any):
        functions = self.function_extractor.extract(obj)
        for function in functions:
            for handler in self.handlers:
                handler.process(function)
