from setuptools import setup

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='pyoptionic',
    version='0.0.1',
    description='',
    author='Seow Jia Jun',
    author_email = 'seowjiajun@gmail.com',
    py_modules=["pyoptionic"],
    package_dir={'': 'pyoptionic'},
)
