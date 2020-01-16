import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="journ",
    version="0.1.7",
    author="Ron Becker",
    author_email="ronbecker@outlook.com",
    description="A really simple command line journal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ronbecker/journ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	"Development Status :: 5 - Production/Stable"
    ],
    entry_points={
            'console_scripts': [
                 'journ=journ:main',
            ]
    },
    python_requires='>=3.6',
)
