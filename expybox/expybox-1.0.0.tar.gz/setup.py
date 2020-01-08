from distutils.core import setup
from setuptools import find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='expybox',
    packages=find_packages(),
    version='1.0.0',
    license='MIT',
    description='Jupyter notebook toolbox for model interpretability/explainability',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Jakub Štercl',
    author_email='stercjak@fit.cvut.cz',
    url='https://github.com/Kukuksumusu/expybox',
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        'shap',
        'pdpbox',
        'lime',
        'alibi',
        'numpy',
        'pandas',
        'ipywidgets'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
