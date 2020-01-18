"""SQLAlchemy-Function

This module defines the following bases:

1. `FunctionMixin`: for creating Function models.
2. `FunctionRelator`: a base for models which relate to Function models.
"""

from sqlalchemy import Column, Integer, PickleType
from sqlalchemy.inspection import inspect
from sqlalchemy_mutable import MutableListType, MutableDictType


class FunctionMixin():
    """Mixin for Function models

    A Function model has a parent, a function, args, and kwargs. When called,
    the Function model executes its function, passing in its parent (if 
    applicable) and its args and kwargs.

    Function models also have an index for convenient use with ordering_list.
    """
    index = Column(Integer)
    _func = Column(PickleType)
    args = Column(MutableListType)
    kwargs = Column(MutableDictType)

    @classmethod
    def register(cls, func):
        """Register a function

        This method simplifies the syntax for creating Function models and 
        associating them with their parents.
        """
        def add_function(parent, *args, **kwargs):
            cls(parent, func, list(args), kwargs)
        setattr(cls, func.__name__, add_function)
        return func

    @property
    def func(self):
        return self._func

    @func.setter
    def func(self, value):
        assert value is None or callable(value), (
            'Attempted to set function attribute to non-function value'
            )
        self._func = value

    def __init__(self, parent=None, func=None, args=[], kwargs={}):
        if parent is not None:
            self.parent = parent
        self.func = func
        self.args, self.kwargs = args, kwargs
        super().__init__()
    
    def __call__(self):
        if self.func is None:
            return
        if hasattr(self, 'parent'):
            return self.func(self.parent, *self.args, **self.kwargs.unshell())
        return self.func(*self.args, **self.kwargs)

        
class FunctionRelator():
    """FunctionRelator base

    The FunctionRelator can be subclassed for models which have 
    relationships to Function models. It provides automatic conversion of 
    functions to Function models when setting attributes.
    """
    _exempt_attrs_fr = ['_func_rel_indicator', '_func_rel_attrs']

    def __new__(cls, *args, **kwargs):
        """
        Set class function relationship indicators and attributes.

        func_rel_indicator maps attribute names to indicators that the 
        attribute is a relationship to Function models.

        func_rel_attrs maps a function relationship name to a 
        (model_class, uselist) tuple.
        """
        if not hasattr(cls, '_func_rel_indicator'):
            cls._func_rel_indicator = {}
            cls._func_rel_attrs = {}
        try:
            return super().__new__(cls, *args, **kwargs)
        except:
            return super().__new__(cls)

    def __setattr__(self, name, value):
        """Set attribute

        Before setting an attribute, determine if it the attribute is a relationship to a Function model. If so, convert the value from a function(s) to a Function model(s).
        """
        if name in self._exempt_attrs_fr:
            return super().__setattr__(name, value)
        is_func_rel = self._func_rel_indicator.get(name)
        if is_func_rel is None:
            is_func_rel = self._set_func_rel(name)
        if is_func_rel:
            model_class, use_list = self._func_rel_attrs[name]
            if use_list:
                value = self._to_function_models(value, model_class)
            else:
                value = self._to_function_model(value, model_class)
        super().__setattr__(name, value)

    @classmethod
    def _set_func_rel(cls, name):
        """
        Set the function relationship status for a previously unseen 
        attribute.
        """
        mapper = inspect(cls).mapper
        rel = [r for r in mapper.relationships if r.key == name]
        if not (rel and FunctionMixin in rel[0].mapper.class_.__mro__):
            is_func_rel = False
        else:
            rel = rel[0]
            cls._func_rel_attrs[name] = (rel.mapper.class_, rel.uselist)
            is_func_rel = True
        cls._func_rel_indicator[name] = is_func_rel
        return is_func_rel
    
    def _to_function_models(self, funcs, model_class):
        """Convert a list of functions to Function models"""
        if not isinstance(funcs, list):
            funcs = [funcs]
        models = [self._to_function_model(f, model_class) for f in funcs]
        return [m for m in models if m is not None]
    
    def _to_function_model(self, func, model_class):
        """Convert a single function to a Function model"""
        if isinstance(func, model_class):
            return func
        if callable(func):
            return model_class(self, func)
        if func is None:
            return None
        raise ValueError(
            'Function relationships requre Function models or callables'
        )