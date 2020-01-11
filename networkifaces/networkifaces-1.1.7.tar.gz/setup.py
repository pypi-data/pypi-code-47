from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="networkifaces",
    version="1.1.7",
    description="A Python package to get interfaces reports for any linux system.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/cpusagewin/cli-reporter",
    author="Glenn C. Wilber",
    author_email="nikhilksingh97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["networkifaces"],
    include_package_data=True,
    install_requires=["psutil","netifaces",""],
 
)