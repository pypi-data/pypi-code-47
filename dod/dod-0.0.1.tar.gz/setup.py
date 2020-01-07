from setuptools import setup, find_packages


# see https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use

setup(name='dod',
      version='0.0.1',
      description='Simple package to manage datasets.',
      url='',
      author='Yohan Foucade',
      author_email='foucade@lipn.fr',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy', 'pandas', 'scikit-learn', 'wget'])
