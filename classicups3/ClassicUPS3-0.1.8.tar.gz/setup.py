from distutils.core import setup

setup(
    name='ClassicUPS3',
    version='0.1.8',
    author='Jason Duncan',
    author_email='jason.matthew.duncan@gmail.com',
    url='https://github.com/jduncan8142/ClassicUPS3',
    packages=['ClassicUPS3'],
    description='Usable UPS Integration in Python 3',
    long_description=open('README.rst').read(),
    keywords=['UPS'],
    requires=['dict2xml', 'xmltodict'],
    classifiers=["Programming Language :: Python :: 3.7",
                 "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                 "Operating System :: OS Independent"
                 ]
)

# To update pypi: `python setup.py register sdist bdist_wininst upload`
