from setuptools import find_packages, setup

install_requires=[
    'torch',
    'opencv-python>=3.4.3.18',
    'numpy',
    'pillow'
    ]

setup(
    name='cvt',
    version='0.0.5',
    packages=find_packages(exclude=('test',)),
    author='jie.wang',
    author_email='jie.wang@ruc.edu.cn',
    description='Image Transformation Package',
    url='https://github.com/wangjie-ruc/cvt',
    license='BSD',
    install_requires=install_requires
)
