# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poche']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poche',
    'version': '0.3.0',
    'description': 'Simple and fast Python in-memory caching library',
    'long_description': '# poche\n\n[![Build Status](https://travis-ci.org/etienne-napoleone/poche.svg?branch=develop)](https://travis-ci.org/etienne-napoleone/poche)\n[![Codecov](https://codecov.io/gh/etienne-napoleone/poche/branch/develop/graph/badge.svg)](https://codecov.io/gh/etienne-napoleone/poche)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nSimple and fast Python in-memory caching.\n\nMeant to speed up using dictionaries as cache backend for simple usecases.\n\nNo external dependencies, 100% code coverage and static type checked.\n\n## Installation\n\nRequires Python 3.6+.\n\n```bash\npip install poche\n```\n\n## Roadmap\n\nv1:\n\n- [x] K/V cache system\n- [x] Basic TTL\n- [x] TTL methods (get, bump, remove, etc)\n- [ ] Memoizing decorator\n- [ ] (Lower required Python version)\n\nv2:\n\n- [ ] Optional per cache stats\n\n## Usage\n\nInstantiate a Poche cache object:\n\n```python\n>>> import poche\n>>> c = poche.Cache()\n# or you can set a default TTL\n>>> c = poche.Cache(default_ttl=5)\n```\n\n**Warning:** When using TTLs, The only call removing a value with expired TTL is `get()`!\n\n### Basic operations\n\nSet a value in cache:\n\n```python\ndef set(key: Hashable, value: Any, Optional: Optional[Union[int, datetime]] = None) -> None\n```\n\nGet a value in cache:\n\n```python\ndef get(key: Hashable) -> Any\n```\n\nGet or set a value in cache if not present:\n\n```python\ndef gos(key: Hashable, value: Any, ttl: Optional[int] = None) -> Any\n```\n\nDelete a value in cache:\n\n```python\ndef delete(key: Hashable) -> None\n```\n\nFlush all cache content:\n\n```python\ndef flush() -> None\n```\n\nExamples:\n\n```python\n>>> c.set("un", 1)\n>>> c.get("un")\n1\n>>> c.delete("un")\n\n>>> c.get("deux")\nKeyError\n>>> c.gos("deux", 2) \n2\n>>> c.gos("deux", 3)\n2\n>>> c.get("deux")\n2\n>>> c.flush()\n```\n\n### TTLs\n\nSet the TTL of a cache item:\n\n```python\ndef set_ttl(key: Hashable, ttl: Optional[Union[int, datetime]],) -> None\n```\n\nGet the TTL of a cache item:\n\n```python\ndef get_ttl(key: Hashable) -> Optional[datetime]\n```\n\nAdd seconds to the current TTL:\n\n```python\ndef bump(key: str, ttl: int) -> None:\n```\nExamples:\n\n```python\n>>> c.set("un", 1, ttl=2)\n>>> c.get("un")\n1\n>>> time.sleep(3)\n>>> c.get("un")\nKeyError\n\n>>> c.set("deux", 2, ttl=datetime(2025, 20, 1)) \n>>> c.get_ttl("deux")\ndatetime(2025, 20, 1)\n>>> c.set_ttl("deux", 2)\n>>> time.sleep(3)\n>>> c.get("deux")\nKeyError\n\n>>> c.set("trois", 3, ttl=2)\n>>> c.set_ttl(None)\n>>> time.sleep(3)\n>>> c.get("trois")\n3\n\n# The only call removing a value with expired TTL is `get()`!\n>>> c.set("quatre", 4, ttl=2)\n>>> time.sleep(3)\n>>> "quatre" in c.keys()\nTrue\n>>> c.get("quatre")\nKeyError\n>>> "quatre" in c.keys()\nFalse\n```\n\n### Dictionary like methods\n\nGet the cache keys:\n\n```python\ndef keys() -> KeysView[Hashable]\n```\n\nGet de cache values:\n\n```python\ndef values() -> ValuesView[Any]\n```\n\nGet the cache values:\n\n```python\ndef items() -> ItemsView[Hashable, Cacheitem]\n```\nExamples:\n\n```python\n>>> c.set("un", 1)\n>>> c.set("deux", 2)\n>>> c.keys()\n["un", "deux"]\n>>> c.values()\n[1, 2]\n>>> for item in c.items():\n...     print(f"{item[0]} -> {item[1].value}")\n"1 -> un"\n"2 -> deux"\n```\n\n### Access raw objects\n\nExamples:\n\n```Python\n>>> c.set("un", 1)\n>>> c["un"]\nCacheitem(expiration=None, value=1)\n>>> c["un"] == 1\nTrue\n>>> 1 in c\nTrue\n>>> c["un"] < 2\nTrue\n>>> c["deux"] = 2\nTypeError\n>>> c["deux"] = Cacheitem(expiration=None, value=2)\n>>> len(c)\n2\n>>> c["un"] < c["deux"]\nTrue\n>>> del c["deux"]\n```\n',
    'author': 'etienne-napoleone',
    'author_email': 'etienne.napoleone@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etienne-napoleone/poche',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
