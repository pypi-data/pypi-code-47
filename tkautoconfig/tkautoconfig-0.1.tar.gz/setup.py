from setuptools import setup

setup(
    name='tkautoconfig',
    packages=['tkautoconfig'],
    version='0.1',
    license='MIT',
    description='Create metadata file automatically for Teko',
    author='Nguyễn Ngọc Trâm',
    author_email='tram.nn@teko.vn',
    url='https://git.teko.vn/data/libs/auto-config-metadata',
    download_url = 'https://git.teko.vn/data/libs/auto-config-metadata/-/archive/v0.1/auto-config-metadata-v0.1.tar.gz',
    install_requires=[            # I get to this in a second
          'pyyaml',
          'minio',
      ],
    zip_safe=False)