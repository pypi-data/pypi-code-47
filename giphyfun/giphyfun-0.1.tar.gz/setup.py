from setuptools import setup, find_packages

setup(
    name             = 'giphyfun',
    version          = '0.1',
    description      = 'Command line program that play random giphy.',
    # url              = '',
    # download_url     = '',
    author           = 'Goia Ciprian',
    author_email     = 'goia.ciprian14@gamil.com',
    maintainer       = 'Goia Ciprian',
    maintainer_email = 'goia.ciprian14@gmail.com',
    packages         = find_packages(),
    install_requires = ['opencv-python', 'appdirs', 'clipboard'],
    entry_points     = {
        'console_scripts': [
            'giphyfun=giphyFun.giphyFun:main',
        ],
    }
)