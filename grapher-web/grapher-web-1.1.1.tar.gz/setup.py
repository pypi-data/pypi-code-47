from setuptools import setup


setup(
    name='grapher-web',
    version='1.1.1',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['data', 'visualization', 'monitoring', 'graphs'],
    python_requires='~=3.7',
    description='Grapher Web UI',
    author='Volodymyr Paslavskyy',
    author_email='qfoxic@gmail.com',
    packages=['grapher.web'],
    package_dir={'grapher.web': 'src/web'},
    package_data={'grapher.web': [
        'ui/*.txt',
        'ui/*.ico',
        'ui/*.html',
        'ui/*.js',
        'ui/*.css'
    ]},
    url='https://gitlab.com/grapher/grapher-web/',
    download_url='https://gitlab.com/grapher/grapher-web/-/archive/1.1.1/grapher-web-1.1.1.tar.gz'
)
