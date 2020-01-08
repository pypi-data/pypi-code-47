import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
    "django_middleware_global_request",
]

setup(
    name="django-admin-item-owner",
    version="0.2.0",
    description="Model item always has an owner, and login user can only see owned items.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["django-admin-item-owner"],
    packages=find_packages(".", exclude=("item_owner_example", "item_owner_example.migrations", "item_owner_demo")),
    py_modules=["item_owner"],
    requires=requires,
    install_requires=requires,
    zip_safe=False,
)
