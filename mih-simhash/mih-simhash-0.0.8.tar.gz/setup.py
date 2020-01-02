#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'mih-simhash',
        version = '0.0.8',
        description = '',
        long_description = '',
        author = 'MIH',
        author_email = '',
        license = '',
        url = '',
        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = [
            '__init__',
            'simhash',
            'redis'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'aioredis==1.3.1',
            'hiredis==1.0.1'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
