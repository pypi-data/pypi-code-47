import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oucass-checklist",
    version="0.1.0",
    author="Jessica Blunt, Brian Greene",
    author_email="cass@ou.edu",
    description="Program to manage safety checks and create metadata files compatible with oucass-profiles in the field",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oucass/Checklist",
    packages=setuptools.find_packages(),
    package_data={'oucass-checklist': ['user_settings/*.pkl']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
