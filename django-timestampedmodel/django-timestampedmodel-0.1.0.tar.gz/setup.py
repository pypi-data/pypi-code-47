from setuptools import setup

# The text of the README file
with open("README.md", "r") as fh:
    README = fh.read()

# This call to setup() does all the work
setup(
    name="django-timestampedmodel",
    version="0.1.0",
    description="Django model with created_at and updated_at fields added by default",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MattShirley/django-timestampedmodel",
    author="Matt Shirley",
    author_email="mattutshirley@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["timestampedmodel"],
    include_package_data=True,
    install_requires=["django"],
)