from setuptools import setup

setup(
    name='docassemble_wrappers',
    version='0.0.4',
    packages=['docassemble_wrappers'],
    url='https://github.com/silexsistemas/docassemble-wrappers',
    license='MIT',
    author='Roberto Vasconcelos Novaes, Luiz Guilherme Paim, Iasmini Gomes',
    author_email='rnovaes@ufmg.br, luis.paimadv@gmail.com, iasmini@silexsistemas.com.br',
    description='Wrappers to external functionalities and Docassemble API',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',

        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=[
        'validator-collection-br',
    ],

    project_urls={  # Optional
                   'Documentation': 'https://github.com/rvnovaes/docassemble-wrappers',
                   'Bug Reports': 'https://github.com/rvnovaes/docassemble-wrappers/issues',
                   'Source': 'https://github.com/rvnovaes/docassemble-wrappers',
    },
)
