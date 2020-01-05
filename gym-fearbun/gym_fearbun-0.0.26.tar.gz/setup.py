from setuptools import setup
import setuptools

setup(name='gym_fearbun',
      version='0.0.26',
      install_requires=['gym', 'six'],
      url='https://github.com/rolypolyvg295/gym_fearbun/tree/master/gym_fearbun',
      include_package_data=True,
      packages=setuptools.find_packages(),
      package_data={'gym_fearbun/maps': ['*.txt']},
      license='MIT'
)
