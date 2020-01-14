from lazy_rpc import remote
from lazy_rpc.utils import filtered_lazy_rpc_keyword, build_uniq_name

FUNCTIONS = {}

def lazy(fn):
  def proxy(*args, **kwargs):
    is_server = kwargs.get('l__sender', None) is None

    if is_server:
      kwargs = filtered_lazy_rpc_keyword(kwargs)
      fn(*args, **kwargs)
    else:
      remote.call(fn, *args, **kwargs)

  FUNCTIONS[build_uniq_name(fn)] = proxy

  return proxy

