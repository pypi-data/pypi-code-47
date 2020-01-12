import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ProjectScope",
    version="0.0.10",
    license='MIT',
    author="Corey Bird",
    author_email="birdcorey@gmail.com",
    description="A small project management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/CoreyBird/projectscope/src/master/",
    download_url="https://bitbucket.org/CoreyBird/projectscope/src/master/dist/ProjectScope-0.0.10.tar.gz",
    packages=setuptools.find_packages(),
    install_requires=[
        'wxPython',
        'Panda3D',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
    package_data={'': ['version_info.txt']},
)
