from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name="savesyndrom",
    version="0.1.2",
    
    author="Oleg Yurchik",
    author_email="oleg.yurchik@protonmail.com",
    url="https://github.com/OlegYurchik/savesyndrom",
    
    description="",
    long_description=open(join(dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    
    packages=find_packages(),

    python_requires=">=3.6",
    install_requires=["PyQt5", "keyboard", "pywin32"],
)
