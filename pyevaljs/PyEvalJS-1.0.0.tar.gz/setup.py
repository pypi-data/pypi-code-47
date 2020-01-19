import io
import re

from setuptools import setup
from setuptools import find_packages

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/PyEvalJS/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="PyEvalJS",
    version=version,
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="Run JavaScript Code in Python through the Microsoft Chakra engine",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Satireven",
    author_email="satireven@gmail.com",
    url="https://github.com/Satireven/PyEvalJS",
    keywords="Python JavaScript js-engine Chakra ChakraCore V8",
    license="MIT",
    python_requires=">2.6, !=3.0.*, !=3.1.*, !=3.2.*",
    include_package_data=True,
    package_data={
        "libs": [
            "src/PyEvalJS/libs/linux/libChakraCore.so",
            "src/PyEvalJS/libs/osx/libChakraCore.dylib",
            "src/PyEvalJS/libs/windows/x64/ChakraCore.dll",
            "src/PyEvalJS/libs/windows/x86/ChakraCore.dll",
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
