
import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Peter de Boer",
    author_email="peterboer_private@hotmail.com",
    name='ponzischeme_game',
    license="MIT",
    description='ponzischeme_game is a python package for handling the game state of the game Ponzi Scheme.',
    version='v0.0.3',
    long_description=README,
    url='https://github.com/peter-de-boer/ponzischeme_game',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    #install_requires=[''],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
