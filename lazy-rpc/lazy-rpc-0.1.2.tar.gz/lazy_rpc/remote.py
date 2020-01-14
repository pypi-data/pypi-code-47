from lazy_rpc.utils import is_not_lazy_rpc_keyword

def call(fn, *args, **kwargs):
  code = fn.__code__
  len_kwargs = len(list(filter(is_not_lazy_rpc_keyword, kwargs.keys())))
  
  if code.co_argcount != len(args) or code.co_kwonlyargcount != len_kwargs:
    raise TypeError('type error')

  sender = kwargs['l__sender']
  del kwargs['l__sender']
  sender.send(fn, *args, **kwargs)

