from setuptools import setup

setup(name='py-dataflow',
      version='0.0.3',
      description='PySpark application',
      url='http://github.com/junqueira/py-dataflow',
      author='junqueira',
      author_email='lcjneto@gmail.com',
      packages=['cloud', 'file', 'integration', 'pypack', 'securit', 'storage', 'transform', 'utils'],
      zip_safe=False)
