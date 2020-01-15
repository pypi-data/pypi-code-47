from setuptools import setup, find_packages
setup(
    name                = 'gpugrab',
    version             = '0.1.0',
    description         = 'get idle gpu deivce.',
    author              = 'seil.na',
    author_email        = 'seil.na@vision.snu.ac.kr',
    url                 = 'https://github.com/seilna/gpugrab',
    download_url        = 'https://github.com/seilna/gpugrab/archive/master.zip',
	install_requires	= ['pynvml'],
    packages            = find_packages(exclude = []),
    keywords            = ['gpu'],
    python_requires     = '>=3',
)
