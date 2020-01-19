from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='Bidirectional Hash Map',
    version='1.00',
    packages=['Bidirectional_Hash_Map'],
    url='https://github.com/DtjiAppDev/BIDIRECTIONAL_HASH_MAP',
    license='MIT',
    author='Dtji AppDev',
    author_email='dtjiappdev1999@gmail.com',
    description='This package contains implementation of a bidirectional hash map.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "Bidirectional Hash Map=Bidirectional_Hash_Map.bidirectional_hash_map:main",
        ]
    }
)
