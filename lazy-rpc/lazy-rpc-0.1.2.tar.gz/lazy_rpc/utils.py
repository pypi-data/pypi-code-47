import pickle

def filtered_lazy_rpc_keyword(kwargs):
  return {k:v for k,v in kwargs.items() if is_not_lazy_rpc_keyword(k)}

def is_not_lazy_rpc_keyword(kw :str) -> bool:
  return kw is None or not kw.startswith('l__')

def build_uniq_name(fn):
  uniq_name = '{}--{}'.format(fn.__module__,
                              fn.__qualname__)
  return uniq_name

def pack(fn, *args, **kwargs) -> bytes:
    value = {
      'args': args,
      'kwargs': kwargs,
    }
    return pickle.dumps(value)

def unpack(value):
  return pickle.loads(value)
