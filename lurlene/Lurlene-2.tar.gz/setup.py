import setuptools

def long_description():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
        name = 'Lurlene',
        version = '2',
        description = 'Python-based live-coding language optimised for a small number of channels',
        long_description = long_description(),
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/combatopera/Lurlene',
        author = 'Andrzej Cichocki',
        packages = setuptools.find_packages(),
        py_modules = [],
        install_requires = ['numpy', 'diapyr', 'splut', 'timelyOSC'],
        package_data = {'': ['*.pxd', '*.pyx', '*.pyxbld', '*.arid', '*.aridt']},
        scripts = [])
