from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="api-base",
    version="1.0.1",
    description="A Python package to connect database",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Tung Nguyen",
    author_email="tung.nguyen@quant-edge.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["api_base"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "api-base=api_base.redis.utils.redis_connect:main",
        ]
    },
)