import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oucass-checklist",
    version="0.2.0",
    author="Jessica Blunt, Brian Greene",
    author_email="cass@ou.edu",
    description="Program to manage safety checks and create metadata files compatible with oucass-profiles in the field",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oucass/Checklist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        checklist=checklist.checklist:cli
    ''',
    python_requires='>=3.7',
    package_data={"checklist":["user_settings/*.pkl"]},
    include_package_data=True,
)
