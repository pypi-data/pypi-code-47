from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
    name='topsis-101703177',
    version='0.0.1',
    description='A topsis Package Project of UCS633',
    author='Divya Arora',
    author_email='divyaarora2k@gmail.com',
    long_description="This package has been created based on Project 1 of course UCS633."
    "Divya Arora COE 8 101703177",
    license='MIT',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Python Software Foundation License",
    ],
    packages=["topsis-101703177"],
    include_package_data=True,
    )