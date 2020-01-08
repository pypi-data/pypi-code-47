import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='goodwan_client',
    packages=['goodwan_client'],
    include_package_data=True,
    description='GoodWan IoT client module',
    long_description_content_type="text/markdown",
    long_description=README,
    version='0.3.1',
    url='https://github.com/kanavis/goodwan_client',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["requests", "pytz"],
    author='Kanavis',
    author_email='dkanavis@gmail.com',
    keywords=['goodwan', 'iot']
)
