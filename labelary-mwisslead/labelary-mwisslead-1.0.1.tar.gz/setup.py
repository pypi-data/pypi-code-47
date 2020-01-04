from setuptools import setup

def main():
    VERSION='1.0.1'
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setup(
        name='labelary-mwisslead',
        version=VERSION,
        description="Module for interacting with api.labelary.com",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/mwisslead/pylabelary",

        author="Michael Wisslead",
        author_email="michael.wisslead@gmail.com",
        maintainer="Michael Wisslead",
        maintainer_email="michael.wisslead@gmail.com",

        classifiers=[
            "Programming Language :: Python",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        license="(specified using classifiers)",
        platforms=["(specified using classifiers)"],

        packages=['labelary'],
        package_data={
        },
        install_requires=['requests'],
        test_suite='nose.collector',
        tests_require=['nose'],
    )

if __name__ == '__main__':
    main()
