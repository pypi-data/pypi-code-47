from distutils.core import setup
from setuptools import find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='expybox',  # How you named your package folder (MyLib)
    packages=find_packages(),
    version='0.0.3-alpha',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Jupyter notebook toolbox for model interpretability/explainability',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Jakub Štercl',  # Type in your name
    author_email='stercjak@fit.cvut.cz',  # Type in your E-Mail
    url='https://github.com/Kukuksumusu/expybox',  # Provide either the link to your github or to your website
    # download_url='https://github.com/Kukuksumusu/expybox/archive/0.0.2-alpha.tar.gz',
    # keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],  # Keywords that define your package best
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[  # I get to this in a second
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
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.7',
    ],
)
