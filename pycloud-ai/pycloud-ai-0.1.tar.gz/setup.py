import os
from setuptools import setup

install_requires = []
with open("requirements.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            install_requires.append(line)

setup(
    name="pycloud-ai",
    version="0.1",
    description="Pycloud engine",
    author="Krzysztof Balka",
    author_email="krzysztof.balka@gmail.com",
    url="http://pycloud.ai",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    install_requires=["setuptools", "docopt"] + install_requires,
    packages=["pycloud"],
    include_package_data=True,
    python_requres='3.6',
)
