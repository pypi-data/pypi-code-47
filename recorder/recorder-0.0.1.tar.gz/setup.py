from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="recorder",
    version="0.0.1",
    keywords=("pip", "recorder"),
    description="a simple audio recorder",
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    license="MIT Licence",

    url="https://github.com/lixk/recorder",
    author="Xiangkui Li",
    author_email="1749498702@qq.com",
    py_modules=['recorder'],
    # packages=find_packages(),
    # include_package_data=True,
    platforms="any",
    install_requires=["pyaudio", "numpy"]
)
