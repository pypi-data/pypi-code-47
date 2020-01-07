import os.path as osp
from setuptools import setup, find_namespace_packages

MIN_PY_VER = '3.6'
DISTNAME = 'recOrder_base_test'
VERSION = "0.0.1"
DESCRIPTION = 'Framework to enable acquisition, analysis, visualization of computational microscopy workflows'
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    LONG_DESCRIPTION_content_type = "text/markdown"
LICENSE = 'Chan Zuckerberg Biohub Software License'
DOWNLOAD_URL = 'https://github.com/czbiohub/recOrder'

INSTALL_REQUIRES = []
REQUIRES = []

CLASSIFIERS = [
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Utilities',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]

# populate packages
PACKAGES = find_namespace_packages(include=['recOrder.*'])

# parse requirements
with open(osp.join('requirements', 'default.txt')) as f:
    requirements = [line.strip() for line in f
                    if line and not line.startswith('#')]

# populate requirements
for l in requirements:
    sep = l.split(' #')
    INSTALL_REQUIRES.append(sep[0].strip())
    if len(sep) == 2:
        REQUIRES.append(sep[1].strip())

if __name__ == '__main__':
    setup(
        name=DISTNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_content_type,
        author="Bryant Chhun",
        author_email="bchhun@gmail.com",
        license=LICENSE,
        url=DOWNLOAD_URL,
        version=VERSION,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        requires=REQUIRES,
        python_requires=f'>={MIN_PY_VER}',
        packages=PACKAGES,
        include_package_data=True
    )
