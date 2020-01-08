
import json
from pathlib import Path
from collections import abc, defaultdict
from functools import partial


class ConfigError(Exception):
    pass


class ConfigService:
    """
    >>> config_svc = ConfigService()
    >>> config_svc.put('answer', 42)
    >>> config_svc.get('answer')
    42
    >>> config_svc.put('user.name', 'x')
    >>> config_svc.put('user.email', 'x@example.com')
    >>> config_svc.get('user')
    {"user.name": "x", "user.email": "x@example.com"}
    """

    def __init__(self):
        cfg = Path('~/.leezy').expanduser()

        def recursive_dd():
            return defaultdict(recursive_dd)

        hook = partial(defaultdict, recursive_dd)
        try:
            self.data = json.loads(cfg.read_text(encoding='utf8'), object_hook=hook)
        except FileNotFoundError:
            self.data = recursive_dd()


    def __getattr_expr(self, dot_key):
        # 'user.name' => ['user']['name']
        return ''.join([f"[{x!r}]" for x in dot_key.split('.')])

    @staticmethod
    def unset(kvs, key):
        expr = f"del kvs{CFG.getattr_expr(key)}"
        try:
            exec(expr)
        except (KeyError, TypeError):
            print(f"config: {key!r} is not found")
            sys.exit(1)

    @staticmethod
    def store(kvs, key, val):
        expr = f"kvs{CFG.getattr_expr(key)} = val"
        try:
            exec(expr)
        except (KeyError, TypeError):
            print(f"config: {key!r} is not valid")
            sys.exit(1)

    @staticmethod
    def fetch_all(kvs, prefix):
        for key, value in kvs.items():
            next_prefix = prefix+'.'+key if prefix else key
            if isinstance(value, abc.Mapping):
                yield from CFG.fetch_all(value, next_prefix)
            else:
                yield next_prefix, value
