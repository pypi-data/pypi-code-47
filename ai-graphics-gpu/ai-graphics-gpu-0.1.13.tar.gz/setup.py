from setuptools import setup, find_packages

requirements = [
    'numpy',
    'opencv-python',
    'flask',
    'tezign',
    'mxnet-cu100',
    'insightface',
    'sklearn',
    'scenedetect',
    'moviepy',
    'Pillow',
]

__version__ = '0.1.13'

setup(
    # Metadata
    name='ai-graphics-gpu',
    version=__version__,
    author='CachCheng',
    author_email='tkggpdc2007@163.com',
    url='https://github.com/CachCheng/Python_Cookbook',
    description='AI Graphics Toolkit',
    license='Apache-2.0',
    # Package info
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
