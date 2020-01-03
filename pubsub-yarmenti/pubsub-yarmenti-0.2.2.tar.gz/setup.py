
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pubsub-yarmenti",
    version="0.2.2",
    author="yarmenti",
    author_email="yannick.armenti@gmail.com",
    description="A simple pub/sub implementation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yarmenti/py_pubsub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)