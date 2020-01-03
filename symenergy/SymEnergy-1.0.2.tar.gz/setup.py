import fnmatch
from setuptools import find_packages, setup
from setuptools.command.build_py import build_py as build_py_orig

with open("README_pypi.md", "r") as fh:
    long_description = fh.read()

exclude = ['_eval_temp']


class build_py(build_py_orig):

    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        modules = [(pkg, mod, file, ) for (pkg, mod, file, ) in modules
                   if not any(pattern in mod for pattern in exclude)]
        print('*'*30)
        print(modules)
        print('*'*30)
        return modules

setup(
    name="SymEnergy",
    version="1.0.2",
    author="SymEnergy contributors listed in AUTHORS",
    author_email="m.c.soini@posteo.de",
    description=("Lagrange multiplier based energy market toy "
                 "modeling framework"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcsoini/symenergy",
  #  packages=['symenergy'],#['symenergy.assets', "symenergy.core"], 
    packages=['symenergy.assets', 'symenergy.evaluator', 'symenergy.core'],#find_packages(),
    cmdclass={'build_py': build_py},
    install_requires=['pandas']
 #   classifiers=[
 #       "Programming Language :: Python :: 3",
 #       "License :: OSI Approved :: BSD 2-Clause License",
 #       "Operating System :: OS Independent",
 #   ],
)
