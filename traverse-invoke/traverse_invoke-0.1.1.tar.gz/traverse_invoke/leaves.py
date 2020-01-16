import inspect

def kwarg(func, config):
    if hasattr(func, '__call__'):
        func(**config)
    else:
        raise Exception(f'trying to call {func}')


from .core import entry_traverse

# ## ## ## ## ## This is demonstrative stuff ######
funcs = {}

def wrap(retkey):
    def wrap1(f):
        return f
        # Uncomment above to use normal adapt (adapt2)
        def wrapped(**config):
            ret = f(**config['this'])
            config['this'][retkey] = ret
        wrapped.__name__ = f.__name__
        return wrapped
    return wrap1

def fadd(f):
    funcs[f.__name__] = f
    return f

@fadd
@wrap('params')
def _get_args(func, **kw):
    params = [ name for
        name, param in inspect.signature(func).parameters.items()
              if param.kind not in [param.VAR_POSITIONAL, param.VAR_KEYWORD]
    ]
    return params

@fadd
@wrap('config')
def _filter_dict(config, params, **kw):
    return {
        key : config.get(key) for
        key in params if config.get(key) is not None
    }

@fadd
@wrap(None)
def _wrap(func, config, **kw):
    print('$$\n$$\n this:', func, config)
    kwarg(func, config)


def adapt(func, config):
    entry_traverse(
        {'this':{'func':func, 'config':config}},

        '_get_args._filter_dict._wrap'.split('.'),

        funcs
        ,leaf=kwarg
    )
# ## ## ## ## ## Stuff above euqivalent to below ######

def adapt2(func, config):
    config = _filter_dict(config, _get_args(func))
    return kwarg(func, config)

