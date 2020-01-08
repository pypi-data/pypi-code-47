from setuptools import setup, find_packages

setup(
    name='mygrid',
    version='0.3',
    author='Lucas Melo',
    author_email='lucassmelo@dee.ufc.br',
    packages=find_packages(),
    package_data={
        'mygrid': ['data/*.json']
    },
    url='https://github.com/grei-ufc/mygrid',
    description='A package to represent a electric grid \
    topology with extensions to make power flow and short circuit \
    analysis',
    install_requires=['numpy',
                      'numba',
                      'pandas',
                      'terminaltables',
                      'graphviz'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Topic :: Scientific/Engineering',
        ],
)
