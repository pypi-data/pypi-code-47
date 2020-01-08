from setuptools import setup

setup(name='apttusvisualizations',
      version='0.11',
      description='Data visualizations for Apttus.',
      author='Caitlin Gowdy at Apttus',
      author_email='cgowdy@apttus.com',
      license='MIT',
      url = 'https://github.com/cgowdy-apttus/apttusvisualizations',
      download_url = 'https://github.com/cgowdy-apttus/apttusvisualizations/archive/v_01.tar.gz',
      packages=['apttusvisualizations'],
      install_requires=['pandas',
                        'datetime',
                        'numpy',
                        'matplotlib'],
      zip_safe=False)