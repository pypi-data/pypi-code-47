import typing
from typing import Optional, Callable, Iterable, Iterator, Dict, Union
import dataclasses
import argparse
from functools import partial
import yaml
import os


__all__ = [
    'confclass',
    'confparam'
]


# A sentinel object to detect if a parameter is supplied or not.
# Use an empty class to give it a unique representation.
class _UNSET_TYPE:
    pass
_UNSET = _UNSET_TYPE()


class _CONFCLASS_MARK_TYPE:
    pass
_CONFCLASS_MARK = _CONFCLASS_MARK_TYPE()


class DefaultBoolean:
    """
    Used to distinguish between an explicitly set boolean value and an unset default fallback boolean value.
    """
    def __init__(self, val: bool = False):
        self.val = val

    def __bool__(self):
        return self.val

    @classmethod
    def is_default(cls, val):
        return isinstance(val, DefaultBoolean)


def _add_arg_prefix_to_arg_name(arg_name: str, arg_prefix: Optional[str] = None):
    if arg_prefix is None or len(arg_prefix) < 1:
        return arg_name
    arg_name_wo_preceding_dashes = arg_name.lstrip('-')
    nr_preceding_dashes = len(arg_name) - len(arg_name_wo_preceding_dashes)
    preceding_dashes = "-" * nr_preceding_dashes
    return f'{preceding_dashes}{arg_prefix}--{arg_name_wo_preceding_dashes}'


def _is_confclass(cls_or_instance):
    return hasattr(cls_or_instance, '__is_confclass') and \
           getattr(cls_or_instance, '__is_confclass') is _CONFCLASS_MARK


def _union_type_check(possible_types: Iterable[type], value: object) -> object:
    for _type_candidate in possible_types:
        try:
            casted = _type_candidate(value)
            return casted
        except Exception as e:
            raise argparse.ArgumentTypeError(e)


_collection_types = {list, tuple, set, frozenset}  # dict, OrderedDict


def _collection_type_check(_collection_type: type, _items_types, value: object) -> object:
    # TODO: fully implement and check this function.
    assert _collection_type in _collection_types
    return _collection_type(value)


def _typing_type_to_argparse_add_argument_kwargs(_type: type) -> Dict:
    # TODO: fully implement and check this function.
    kwargs = {}
    if isinstance(_type, typing._GenericAlias):
        if _type.__origin__ is typing.Union:
            if type(None) in _type.__args__:
                kwargs['required'] = False
                kwargs['default'] = None
            possible_types = [tp for tp in _type.__args__ if tp is not type(None)]
            assert len(possible_types) > 0
            if len(possible_types) == 1:
                kwargs.update(_typing_type_to_argparse_add_argument_kwargs(possible_types[0]))
                return kwargs
            kwargs['type'] = partial(_union_type_check, possible_types)
            return kwargs
        if _type.__origin__ in _collection_types:
            # FIXME: how does `argparse` expect to get list?
            #  maybe we just should set `type` to be the item type and set `nargs` to "?" or "+"?
            return {'type': partial(_collection_type_check, _type.__origin__, _type.__args__)}
        raise ValueError(f'Type `{_type}` is not supported by `confclass`.')
    elif _type is bool:
        return {'action': 'store_true'}
    else:
        return {'type': _type}


class ConfParam(dataclasses.Field):
    description: Optional[str] = None
    default_as_other_field: Optional[str] = None
    default_factory_with_self_access: Optional[Callable] = None
    choices: Optional[Iterable] = None

    def __init__(self,
                 default=dataclasses.MISSING,
                 default_factory=dataclasses.MISSING,
                 init=True,
                 repr=True,
                 hash=None,
                 compare=True,
                 metadata=None,
                 description: Optional[str] = None,
                 default_as_other_field: Optional[str] = None,
                 default_factory_with_self_access: Optional[Callable] = None,
                 default_description: Optional[str] = None,
                 init_from_arg: Union[DefaultBoolean, bool] = DefaultBoolean(False),
                 arg_names: Optional[Iterable[str]] = None,
                 arg_prefix: Optional[str] = None,
                 choices: Optional[Iterable] = None):

        self.description = description
        self.default_as_other_field = default_as_other_field
        self.default_factory_with_self_access = default_factory_with_self_access
        self.default_description = default_description
        self._arg_names = tuple(arg_names) if arg_names is not None else None
        self.arg_prefix = arg_prefix
        # Notice: In the line below it is important that `init_from_arg` is the last, so it would stay DefaultBoolean
        #         when everything else is False.
        self.init_from_arg = bool(self._arg_names) or bool(self.arg_prefix) or init_from_arg
        self.choices = list(choices) if choices is not None else None

        if default_as_other_field is not None and default_factory_with_self_access is not None:
            raise ValueError('Cannot set both `default_as_other_field` and `default_factory_with_self_access`.')

        if default_as_other_field is not None or default_factory_with_self_access is not None:
            if default is not dataclasses.MISSING or default_factory is not dataclasses.MISSING:
                raise ValueError(
                    'Cannot set both `default` nor `default_factory` together with `default_as_other_field`'
                    'or with `default_factory_with_self_access`.')
            # We initially set the `field.default` to an unique `_UNSET` value, which we later detect
            # as the field value and re-assign a new value to this field.
            default = _UNSET

        super(ConfParam, self).__init__(
            default=default, default_factory=default_factory, init=init,
            repr=repr, hash=hash, compare=compare, metadata=metadata)

    def get_arg_names(self, argname_prefix: Optional[str] = None):
        arg_names = self._arg_names
        if not arg_names:
            arg_names = (f"--{self.name.replace('_', '-')}",)
        if argname_prefix is None or len(argname_prefix) == 0:
            return arg_names
        return tuple(_add_arg_prefix_to_arg_name(arg_name, argname_prefix) for arg_name in arg_names)

    def add_to_argparser(self, argparser: argparse.ArgumentParser, argname_prefix: Optional[str] = None):
        if _is_confclass(self.type):
            confclass = self.type
            total_argname_prefix = None
            if argname_prefix and self.arg_prefix:
                total_argname_prefix = argname_prefix + '-' + self.arg_prefix
            elif argname_prefix and not self.arg_prefix:
                total_argname_prefix = argname_prefix
            elif not argname_prefix and self.arg_prefix:
                total_argname_prefix = self.arg_prefix
            confclass.add_args_to_argparser(argparser, total_argname_prefix)
        else:
            arg_kwargs = {}
            arg_names = self.get_arg_names(argname_prefix)
            if self.is_arg_positional:
                arg_kwargs['dest'] = self.get_arg_dest(argname_prefix)
                arg_kwargs['required'] = self.is_required_as_arg
            if self.description:
                arg_kwargs['help'] = self.description
                if self.default_description:
                    arg_kwargs['help'] += f' (default: {self.default_description})'
                elif self.default_as_other_field is not None:
                    arg_kwargs['help'] += f' (default: value of `{self.default_as_other_field}`)'
                elif self.default is not dataclasses.MISSING and self.default is not _UNSET:
                    arg_kwargs['help'] += f' (default: {self.default})'
                elif self.default_factory is not dataclasses.MISSING:
                    arg_kwargs['help'] += f' (default: {self.default_factory()})'
            if self.choices is not None:
                arg_kwargs['choices'] = self.choices
            # TODO: complete the rest of the possible parameters that we should pass here to `add_argument()`
            # TODO: for a boolean parameter add `store_true` and `store_false` arguments.
            arg_kwargs.update(_typing_type_to_argparse_add_argument_kwargs(self.type))
            argparser.add_argument(
                *arg_names,
                **arg_kwargs)

    def load_from_args(self, args: argparse.Namespace, argname_prefix: Optional[str] = None) -> object:
        if _is_confclass(self.type):
            confclass = self.type
            total_argname_prefix = None
            if argname_prefix and self.arg_prefix:
                total_argname_prefix = argname_prefix + '-' + self.arg_prefix
            elif argname_prefix and not self.arg_prefix:
                total_argname_prefix = argname_prefix
            elif not argname_prefix and self.arg_prefix:
                total_argname_prefix = self.arg_prefix
            return confclass.load_from_args(args, total_argname_prefix)
        else:
            arg_dest = self.get_arg_dest(argname_prefix)
            if arg_dest in args:
                return args.__getattribute__(arg_dest)
            return None

    def get_arg_dest(self, argname_prefix: Optional[str] = None) -> str:
        return self.get_arg_names(argname_prefix)[0].strip('-').replace('-', '_')

    @property
    def has_default(self):
        return self.default is not dataclasses.MISSING or \
               self.default_factory is not dataclasses.MISSING or \
               self.default_factory_with_self_access is not None or \
               self.default_as_other_field is not None

    @property
    def is_arg_positional(self):
        return all(arg_name[0] == '-' for arg_name in self.get_arg_names())

    @property
    def is_required_as_arg(self):
        return self.init_from_arg and not self.has_default


confparam = ConfParam


def confclass(_cls,
              frozen: bool = True,
              init_all_from_arg_by_default: bool = True,
              load_from_yaml_via_arg: bool = True):

    # cls_annotations = _cls.__dict__.get('__annotations__', {})
    # cls_fields = [dataclasses._get_field(_cls, name, type)
    #               for name, type in cls_annotations.items()]

    # print('_cls annotations:', _cls.__dict__.get('__annotations__', {}))
    # class _inh:
    #     __dict__ = _cls.__dict__
    #     # __class__ = _cls.__class__
    #     __annotations__ = _cls.__annotations__
    #     # a: int
    #     pass
    # print('_cls annotations:', _cls.__dict__.get('__annotations__', {}))
    # print('_inh annotations:', _inh.__dict__.get('__annotations__', {}))
    # print('_cls __dict__:', _cls.__dict__)
    # print('_inh __dict__:', _inh.__dict__)
    # _cls = _inh

    # print('_inh(_cls) annotations:', _inh.__dict__.get('__annotations__', {}))
    # del _inh.__dict__['__annotations__']['a']
    # _inh.__dict__['__annotations__'].update(_cls.__dict__.get('__annotations__', {}))
    # object.__setattr__(_inh, '__annotations__', _cls.__dict__.get('__annotations__', {}))
    # print('_inh(_cls) [after coping annotations from _cls] annotations:', _inh.__dict__.get('__annotations__', {}))
    # _cls = _inh

    def __set_unset_fields(_self):
        for fld in dataclasses.fields(_self):
            if not isinstance(fld, ConfParam):
                continue

            if getattr(_self, fld.name) is not _UNSET:
                continue

            if fld.default_factory_with_self_access is not None:
                new_value = fld.default_factory_with_self_access(_self)
                object.__setattr__(_self, fld.name, new_value)
            elif fld.default_as_other_field is not None:
                assert hasattr(_self, fld.default_as_other_field)
                value = getattr(_self, fld.default_as_other_field)
                assert value is not _UNSET
                object.__setattr__(_self, fld.name, value)

    def __verify_fields_values(_self):
        pass  # TODO: implement!

    orig_post_init = getattr(_cls, '__post_init__', None)
    def __post_init__(self):
        __set_unset_fields(self)
        if orig_post_init is not None:
            orig_post_init(self)
        __verify_fields_values(self)
    setattr(_cls, '__post_init__', __post_init__)

    # Create a `dataclass()` out of the _cls
    # Make sure that auto created fields are from type `ConfParam` rather than `dataclasses.Field`
    orig_dataclasses_field_fn = dataclasses.field
    dataclasses.field = confparam
    _cls = dataclasses.dataclass(_cls, frozen=frozen)
    dataclasses.field = orig_dataclasses_field_fn

    if init_all_from_arg_by_default:
        for fld in dataclasses.fields(_cls):
            if not isinstance(fld, ConfParam):
                continue
            if DefaultBoolean.is_default(fld.init_from_arg):
                fld.init_from_arg = True

    def _iter_fields_with_args(cls) -> Iterator[ConfParam]:
        for fld in dataclasses.fields(cls):
            if not isinstance(fld, ConfParam):
                continue
            if not fld.init_from_arg:
                continue
            yield fld
    setattr(_cls, '_iter_fields_with_args', classmethod(_iter_fields_with_args))

    def add_args_to_argparser(cls,
                               argparser: argparse.ArgumentParser,
                               argname_prefix: Optional[str] = None):
        for fld in _iter_fields_with_args(cls):
            fld.add_to_argparser(argparser, argname_prefix)
    setattr(_cls, 'add_args_to_argparser', classmethod(add_args_to_argparser))

    def _load_from_args(cls,
                        args: Optional[argparse.Namespace] = None,
                        argname_prefix: Optional[str] = None) -> dict:
        if args is None:
            argparser = argparse.ArgumentParser()
            cls.add_args_to_argparser(argparser)
            args = argparser.parse_args()

        kwargs_to_ctor = {}
        for fld in _iter_fields_with_args(cls):
            value = fld.load_from_args(args, argname_prefix)
            if value is not None:
                kwargs_to_ctor[fld.name] = value
        return kwargs_to_ctor

    def load_from_args(cls,
                       args: Optional[argparse.Namespace] = None,
                       argname_prefix: Optional[str] = None):
        kwargs_to_ctor = _load_from_args(cls, args, argname_prefix)
        return cls(**kwargs_to_ctor)
    setattr(_cls, 'load_from_args', classmethod(load_from_args))

    default_hierarchy_fallback_order = frozenset({'args', 'kwargs', 'yaml'})
    def factory(cls,
                load_from_args: Union[argparse.Namespace, bool] = False,
                load_from_yaml: Union[str, bool] = False,
                argname_prefix: Optional[str] = None,
                verify_confclass: bool = True,
                hierarchy_fallback_order=default_hierarchy_fallback_order,
                **explicit_params_to_set):
        """
        Default params setting hierarchy fallback:
        1. From argument
        2. Explicit given as kwargs
        3. From yaml
        4. Default value
        """

        assert set(hierarchy_fallback_order).issubset(default_hierarchy_fallback_order)

        # TODO: handle differently confparams which are inner confclasses!
        #  they should be created iff they (or one of its inner confclasses)
        #  got a non-default value (from arg, explicit or yaml) for one of its params.

        # TODO: allow getting dict as explicit value for an inner confclass.
        #  because you want to set some of its params and maybe load the rest
        #  from arg or from the yaml.

        kwargs_to_ctor = {}

        for origin in hierarchy_fallback_order:
            if origin == 'yaml' and load_from_yaml:
                if load_from_yaml is True:
                    load_from_yaml = f'{cls.__name__}.yaml'
                if os.path.isfile(load_from_yaml):
                    with open(load_from_yaml, 'r') as yaml_file:
                        # TODO: handle inner confclasses
                        loaded_params_dict = yaml.safe_load(yaml_file)
                        kwargs_to_ctor.update(loaded_params_dict)
            if origin == 'kwargs':
                kwargs_to_ctor.update(explicit_params_to_set)
            if origin == 'args' and load_from_args:
                args = load_from_args if isinstance(load_from_args, argparse.Namespace) else None
                kwargs_to_ctor.update(_load_from_args(cls, args, argname_prefix))

        obj = cls(**kwargs_to_ctor)
        if verify_confclass and hasattr(obj, '__verify_conf__'):
            obj.__verify_conf__()
        return obj
    setattr(_cls, 'factory', classmethod(factory))

    def save_to_yaml(_self,
                     dest_yaml_path: Optional[str] = None,
                     export_only_explicitly_set_params: bool = False) -> typing.NoReturn:
        dict_to_export = dataclasses.asdict(_self)
        if export_only_explicitly_set_params:
            # TODO: fix for sub confclasses (which are dicts here and they also
            #  may recursively include inner confclasses)
            dict_to_export = {key: val
                              for key, val in dict_to_export.items()
                              if key in _self.__explicitly_set_params__}
        if dest_yaml_path is None:
            dest_yaml_path = f'{_self.__class__.__name__}.yaml'
        with open(dest_yaml_path, 'w') as yaml_file:
            yaml.dump(dict_to_export, yaml_file, default_flow_style=False)
    setattr(_cls, 'save_to_yaml', save_to_yaml)

    def pprint(_self, print_fn: Callable[[str], typing.NoReturn] = print, min_param_name_col_len: int = 0):
        def _longest_param_name_len(_self) -> int:
            return max(max((len(param_name),
                            (4 + _longest_param_name_len(_self.__getattribute__(param_name)))
                            if _is_confclass(_self.__getattribute__(param_name)) else 0)
                           )
                       for param_name, _ in dataclasses.asdict(_self).items())

        for param_name, param_val in dataclasses.asdict(_self).items():
            if _is_confclass(_self.__getattribute__(param_name)):
                param_val = ''
            param_name_col_len = max(_longest_param_name_len(_self) + 2, min_param_name_col_len)
            print_fn(f'{param_name: <{param_name_col_len}}{param_val}')
            if _is_confclass(_self.__getattribute__(param_name)):
                _self.__getattribute__(param_name).pprint(
                    print_fn=lambda x: print_fn(f'    {x}'), min_param_name_col_len=param_name_col_len-4)
    setattr(_cls, 'pprint', pprint)

    orig_ctor = getattr(_cls, '__init__')
    def __init__(_self, **kwargs):
        orig_ctor(_self, **kwargs)
        explicitly_set_params: typing.Set[str] = set(getattr(_self, '__explicitly_set_params__', set()))
        explicitly_set_params.update((param_name for param_name in kwargs))
        object.__setattr__(_self, '__explicitly_set_params__', frozenset(explicitly_set_params))
    setattr(_cls, '__init__', __init__)

    setattr(_cls, '__is_confclass', _CONFCLASS_MARK)

    return _cls
