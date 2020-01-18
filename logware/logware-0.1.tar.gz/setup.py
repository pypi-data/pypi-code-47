from setuptools import setup

setup(name='logware',
    version='0.1',
    description='Simple request logging middleware',
    url='https://github.com/GiridharSamanth/python-logware',
    author='Giridhar',
    author_email='samanth.giridhar@gmail.com',
    license='MIT',
    packages=['logware'],
    install_requires=[
      'webob'  
    ],
    zip_safe=False)
