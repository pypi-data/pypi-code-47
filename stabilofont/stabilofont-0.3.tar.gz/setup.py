from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name = "stabilofont",
    version='0.3',
    license='MIT',
    description="stabilofont is a package for change text color in terminal/cmd when you print some important text",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Rizki Maulana",
    author_email="rizkimaulana348@gmail.com",
    url="https://github.com/rizki4106/stabilo",
    download_url="https://github.com/rizki4106/stabilo/archive/master.zip",
    keywords=['colors', 'color','font','background','style'],
    packages=['stabilofont'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
)