import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="pyctoolbox",
    version='0.1.1',
    author="PyCoders",
    author_email="admin@pycoders.vn",
    description="A strong Toolbox for Python Coders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pycodersvn/pycoders-toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pyctoolbox=cli:main
    ''',
)