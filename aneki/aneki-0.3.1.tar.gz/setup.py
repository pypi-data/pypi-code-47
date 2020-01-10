import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aneki",
    version="0.3.1",
    author="VolkovAK",
    description="Aneki = jokes delivery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VolkovAK/aneki",
    include_package_data=True,  # for adding files described in MANIFEST.in
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'aneki=aneki.main:main',
        ],
    },
)
