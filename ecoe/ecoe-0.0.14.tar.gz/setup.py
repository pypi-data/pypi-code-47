import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

VERSION = "0.0.14"
print( "ecoe version", VERSION)


setuptools.setup(
    name="ecoe", # Replace with your own username
    version=VERSION,
    author="John Bolte",
    author_email="john.bolte@oregonstate.edu",
    description="Package for Ecological Engineering Applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OSU-BEE/ecoe",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",

        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],

    keywords='ecological engineering python',  # Optional
    
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    #package_dir={'': 'eco_eng'},  # Optional
    #packages=setuptools.find_packages(where='eco_eng'),
    #        package_dir = {
    #        'mySubPackage1': 'mySubPackage1',
    #        'mySubPackage2': 'mySubPackage2'},
    #    packages=['mySubPackage1', 'mySubPackage2'],
    packages=['ecoe', 'ecoe.econ','ecoe.geo','ecoe.hydro', 'ecoe.modeling'],
    python_requires='>=3.5',
    install_requires=['numpy', 'pandas', 'matplotlib'],  # Optional
)

###     # List additional URLs that are relevant to your project as a dict.
###     #
###     # This field corresponds to the "Project-URL" metadata fields:
###     # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
###     #
###     # Examples listed include a pattern for specifying where the package tracks
###     # issues, where the source is hosted, where to say thanks to the package
###     # maintainers, and where to support the project financially. The key is
###     # what's used to render the link text on PyPI.
###     project_urls={  # Optional
###         'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
###         'Funding': 'https://donate.pypi.org',
###         'Say Thanks!': 'http://saythanks.io/to/example',
###         'Source': 'https://github.com/pypa/sampleproject/',
###     },
### )