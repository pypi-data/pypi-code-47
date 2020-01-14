from os.path import abspath, dirname

from setuptools import setup
from setuptools.command.install import install


LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("mypy_boto3: Running post-install script for mypy-boto3-budgets")
        try:
            from mypy_boto3.main import add_package_to_index

            add_package_to_index("budgets")
            print("mypy_boto3: Service budgets added to index")
        except Exception as e:
            print("mypy_boto3: Package index update failed for mypy-boto3-budgets:", e)


setup(
    name="mypy-boto3-budgets",
    version="1.11.2.0",
    packages=["mypy_boto3_budgets"],
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Type annotations for boto3.Budgets 1.11.2 service.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    keywords="boto3 budgets type-annotations boto3-stubs mypy mypy-stubs typeshed autocomplete auto-generated",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3_budgets": ["py.typed"]},
    python_requires=">=3.7",
    project_urls={
        "Documentation": "https://mypy-boto3.readthedocs.io/en/latest/",
        "Source": "https://github.com/vemel/mypy_boto3",
        "Tracker": "https://github.com/vemel/mypy_boto3/issues",
    },
    install_requires=["typing_extensions; python_version < '3.8'",],
    zip_safe=False,
    cmdclass={"install": PostInstallCommand},
)
