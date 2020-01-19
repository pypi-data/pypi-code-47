# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi_rest',
 'bareasgi_rest.protocol',
 'bareasgi_rest.protocol.iso_8601',
 'bareasgi_rest.protocol.json',
 'bareasgi_rest.swagger']

package_data = \
{'': ['*'], 'bareasgi_rest': ['templates/*']}

install_requires = \
['bareasgi-jinja2>=3.1,<4.0',
 'bareasgi>=3.5,<4.0',
 'docstring-parser>=0.5,<0.6',
 'inflection>=0.3.1,<0.4.0',
 'typing-extensions>=3.7,<4.0']

setup_kwargs = {
    'name': 'bareasgi-rest',
    'version': '3.0.0rc6',
    'description': 'REST support for bareASGI',
    'long_description': '# bareASGI-rest\n\n\nThis package provides enhanced support for writing REST\nAPIs with [bareASGI](https://bareasgi.com).\n\nIt includes:\n\n* A router to simplify the creation of REST APIs,\n* A swagger API endpoint\n\nThis is a Python 3.7+ package, and is currently pre-release.\n\n## Installation\n\nThe package can be install from pypi.\n\nIt is currently pre-release so you will need the --pre flag.\n\n```bash\n$ pip install --pre bareASGI-rest\n```\n\nAn ASGI server will be required to run the code. The examples below use\n[uvicorn](https://www.uvicorn.org/).\n\n```bash\n$ pip install uvicorn\n```\n\n## Usage\n\nThe router provided by this package maps the arguments and\ntypes of request handlers.\n\nWe will create a mock book repository.\n\n### Creating typed dictionaries\n\nHere is the type of a book. We use `TypedDict` to allow automatic type discovery\n\n```python\nfrom datetime import datetime\ntry:\n    # Available in 3.8\n    from typing import TypedDict  # type:ignore\nexcept:\n    # Available in 3.7\n    from typing_extensions import TypedDict\n\nclass Book(TypedDict):\n    """A Book\n\n    Args:\n        book_id (int): The book id\n        title (str): The title\n        author (str): The author\n        published (datetime): The publication date\n    """\n    book_id: int\n    title: str\n    author: str\n    published: datetime\n```\n\nNote: the docstring will be used to provide documentation for swagger.\n\n### Creating the API\n\nNow we can build the API.\n\n```python\nfrom typing import Dict, List\nfrom urllib.error import HTTPError\n\n\nBOOKS: Dict[int, Book] = {}\nNEXT_ID: int = 0\n\nasync def get_books() -> List[Book]:\n    """Get all the books.\n\n    This method gets all the books in the shop.\n\n    Returns:\n        List[Book]: All the books\n    """\n    return list(BOOKS.values())\n\n\nasync def get_book(book_id: int) -> Book:\n    """Get a book for a given id\n\n    Args:\n        book_id (int): The id of the book\n\n    Raises:\n        HTTPError: 404, when a book is not found\n\n    Returns:\n        Book: The book\n    """\n\n    if book_id not in BOOKS:\n        raise HTTPError(None, 404, None, None, None)\n\n    return BOOKS[book_id]\n\n\nasync def create_book(\n        author: str,\n        title: str,\n        published: datetime\n) -> int:\n    """Add a book\n\n    Args:\n        author (str): The author\n        title (str): The title\n        published (datetime): The publication date\n\n    Returns:\n        int: The id of the new book\n    """\n    NEXT_ID += 1\n    BOOKS[NEXT_ID] = Book(\n        book_id=NEXT_ID,\n        title=title,\n        author=author,\n        published=published\n    )\n    return NEXT_ID\n\n\nasync def update_book(\n        book_id: int,\n        author: str,\n        title: str,\n        published: datetime\n) -> None:\n    """Update a book\n\n    Args:\n        book_id (int): The id of the book to update\n        author (str): The new author\n        title (str): The title\n        published (datetime): The publication date\n\n    Raises:\n        HTTPError: 404, when a book is not found\n    """\n    if book_id not in BOOKS:\n        raise HTTPError(None, 404, None, None, None)\n    BOOKS[book_id][\'title\'] = title\n    BOOKS[book_id][\'author\'] = author\n    BOOKS[book_id][\'published\'] = published\n```\n\nWe can see that errors are handler by raising HTTPError\nfrom the `urllib.errors` standard library package. A convention has been applied such that the status code MUST\nappear before the message, separated by a comma.\n\n### Adding support for the REST router\n\nNow we must create our application and add support for the router.\n\n```python\nfrom bareasgi import Application\nfrom bareasgi_rest import RestHttpRouter, add_swagger_ui\n\n\nrouter = RestHttpRouter(\n    None,\n    title="Books",\n    version="1",\n    description="A book api",\n    base_path=\'/api/1\',\n    tags=[\n        {\n            \'name\': \'Books\',\n            \'description\': \'The book store API\'\n        }\n    ]\n)\napp = Application(http_router=router)\nadd_swagger_ui(app)\n```\n\nNote the `base_path` argument can be used to prefix all\npaths.\n\nThe `RestHttpRouter` is a subclass of the basic router, so\nall those methods are also available.\n\n### Creating the routes\n\nNow we can create the routes:\n\n```python\ntags = [\'Books\']\nrouter.add_rest({\'GET\'}, \'/books\', get_books,tags=tags)\nrouter.add_rest({\'GET\'}, \'/books/{bookId:int}\', get_book, tags=tags)\nrouter.add_rest({\'POST\'}, \'/books\', create_book, tags=tags, status_code=201)\nrouter.add_rest({\'PUT\'}, \'/books/{bookId:int}\', update_book, tags=tags, status_code=204)\n```\n\nFirst we should note that the paths will be prefixed with the\n`base_path` provided to the router.\n\nReferring back to the implementation of `get_book` we can\nsee  that the camel-case path variable `bookId` has been\nmapped to the snake-case `book_id` parameter. The JSON object provided in the body of the `create_book` will\nsimilarly map camel-cased properties to the snake-cased\nfunction parameters.\n\nWe can also see how the status codes have been overridden\nfor the `POST` and `PUT` endpoints, and all the routes\nhave the "Books" tag for grouping in the UI.\n\n### Serving the API\n\nFinally we can serve the API:\n\n```python\nimport uvicorn\n\nuvicorn.run(app, port=9009)\n```\n\nBrowsing to http://localhost/api/1/swagger we should see:\n\n![Top Level](screenshot1.png)\n\nWhen we expand `GET /books/{bookId}` we can see all the\ninformation provided in the docstring and typing has been\npassed through to the swagger UI.\n\n![GET /books/{bookId}](screenshot2.png)\n\n## Thanks\n\nThanks to [rr-](https://github.com/rr-) and contributors\nfor the excellent\n[docstring-parser](https://github.com/rr-/docstring_parser)\npackage.\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareASGI-rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
