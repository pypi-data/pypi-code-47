# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s3os']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.10.50,<2.0.0', 'ruamel.yaml>=0.16.5,<0.17.0', 'toml>=0.9,<0.10']

setup_kwargs = {
    'name': 's3os',
    'version': '1.0.0',
    'description': 'S3 Object Store. Store and retrieve python objects in s3 simply..',
    'long_description': 'S3 Object Store\n-------\n\n![badge](https://github.com/MartinHowarth/s3os/workflows/Test/badge.svg)\n\nSimple pythonic wrapper to use s3 as a python object store.\n\nProvides simple object storage methods; and a Dict-like interface for more complicated uses.\n\nExamples\n--------\nBasic usage:\n\n    from s3os import store_simple, retrieve_simple, delete_simple\n    \n    my_object = [1, 2, 3]\n    \n    store_simple("my_key", my_object)\n    \n    assert retrieve_simple("my_key") == my_object\n    \n    delete_simple("my_key")\n\nThe above example uses a global namespace in the bucket "s3os" - i.e. all the default settings of this package.\n\nYou can specify your own namespaces (i.e. buckets) as follows:\n\n    from s3os import store, retrieve, delete, ObjectLocation, Bucket\n    \n    my_bucket = Bucket("my_bucket")\n    my_object_location = ObjectLocation("my_key", bucket=my_bucket)\n    my_object = [1, 2, 3]\n    \n    store(my_object_location, my_object)\n    \n    assert retrieve(my_object_location) == my_object\n    \n    delete(my_object_location)\n\n\nOr simply use s3 like a normal python dictionary:\n\n    from s3os import S3Dict, S3DictConfig, Bucket\n    \n    my_bucket = Bucket("my_bucket")\n    s3dict = S3Dict(_config=S3DictConfig(id="my_dict_id", bucket=my_bucket))\n    \n    # Store information in s3\n    s3dict["apples"] = 5\n    s3dict["bananas"] = 2\n    \n    ...\n    \n    # Later, or in a different python executable, access the same dictionary again:\n    my_bucket = Bucket("my_bucket")\n    s3dict = S3Dict(_config=S3DictConfig(id="my_dict_id", bucket=my_bucket))\n    \n    print(s3dict["apples])  # 5\n    print(s3dict.get_all_from_s3())  # {"apples": 5, "bananas": 2}\n    \n\n\nBy default, `S3Dict` uses an internal cache to speed up item retrieval. \nSet and Delete operations are always performed synchronously.\n\n\nInstallation\n------------\nInstall the package:\n\n    pip install s3os\n\nSetup your AWS credentials. For example set these environment variables:\n\n    AWS_ACCESS_KEY_ID=...\n    AWS_SECRET_ACCESS_KEY=...\n    \nAlso see https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html for more authentication options.\n\n> Note: `boto.client()` and `Session` authentication methods are not currently supported - raise an issue or submit a PR if you want them!\n\n\nDevelopment installation\n------------------------\nInstall poetry - see https://pypi.org/project/poetry/\n\nThe following command should be used to install the dependencies:\n\n    poetry install\n\n\nTesting\n-------\nThe following command should be used to run the tests:\n\n    poetry run pytest tests\n\nValid AWS authentication credentials are required to run some of the tests.\nSee setup instructions.\n\nThe tests make a very small number of calls to S3, so the cost of running the tests is negligible.\n',
    'author': 'Martin Howarth',
    'author_email': 'howarth.martin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MartinHowarth/s3os',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
