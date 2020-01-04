from setuptools import setup, find_packages

with open('README.rst') as f:
    README = f.read()

setup(
    name = "django-personal-finances",
    version = "0.04",
    description = "A Django app to track personal finances",
    long_description = README,
    author = "Wade Roberts",
    author_email = "waderoberts123@gmail.com",
    license = "MIT",
    classifiers = [
        "Environment :: Web Environment",
        "Framework :: Django :: 3.0",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
)
