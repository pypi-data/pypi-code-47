from setuptools import setup, find_packages

setup(name='disagree',
      version='0.2.6',
      author='Oliver Price',
      author_email='op.oliverprice@gmail.com',
      download_url='https://github.com/o-P-o/disagree/',
      packages=['disagree', 'disagree.test'],
      include_package_data=True,
      license='LICENSE',
      description='Visual and statistical assessment of annotator agreements',
      #long_description=open('README.md').read(),
      install_requires=[
        'scipy >= 1.1.0',
        'tqdm >= 4.26.0',
        'pandas >= 0.23.0']
     )
