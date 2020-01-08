from setuptools import setup, find_packages


# see https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use

setup(name='pycvi',
      version='0.0.13',
      description='Easily compute clustering cliterions',
      url='',
      author='Yohan Foucade',
      author_email='foucade@lipn.fr',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy', 'pandas', 'scikit-learn'])
