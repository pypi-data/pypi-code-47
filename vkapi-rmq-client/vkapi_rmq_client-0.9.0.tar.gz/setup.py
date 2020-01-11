import setuptools
import vkapi


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="vkapi_rmq_client",
    version=vkapi.__version__,
    author="Mikhail Migushov",
    author_email="me@chuvash.pw",
    description="A library to work with vkAPIService",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyber-chuvash/vkAPIClient",
    packages=['vkapi'],
    install_requires=['pika'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
