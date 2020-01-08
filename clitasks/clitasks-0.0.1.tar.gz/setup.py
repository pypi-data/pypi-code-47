import setuptools

setuptools.setup(
    name="clitasks",
    version="0.0.1",
    author="Sarath Menon",
    author_email="sarath.menon@rub.de",
    description="Command line task manager",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    download_url="https://github.com/srmnitc/cli-tasks/archive/0.0.1.tar.gz",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['clint'],
    #scripts=['bin/pathsampling', 'bin/pathsampling_kernel'],
    entry_points={
        'console_scripts': [
            'clitasks = clitasks.bin.run:main',
        ],
    }
)
