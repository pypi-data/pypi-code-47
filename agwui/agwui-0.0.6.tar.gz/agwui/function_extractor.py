from typing import Any
from inspect import getmembers,ismethod

class FunctionExtractor:
    def extract(self, obj: Any):
        return  [function for (name,function) in getmembers(obj,predicate=ismethod) if not name.startswith("__")]
