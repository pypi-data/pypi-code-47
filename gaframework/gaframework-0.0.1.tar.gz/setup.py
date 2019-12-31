import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaframework", # Replace with your own username
    version="0.0.1",
    author="John Newcombe",
    author_email="jnewcombeuk@gmail.com",
    description="Simple to use genetic algorithm library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/johnnewcombe/gapy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3.6',
)

# After Twine is installed, we can open the Terminal (Alt+F12) and run twine register dist/pad-on-left-1.0.0.tar.gz -r testpypi and then twine upload dist/* -r testpypi. If these commands executed correctly, you should be able to find your package on testpypi.
#
# If everything looks good on testpypi, you can run the same commands without -r testpypi:
#
# twine register dist/pad-on-left-1.0.0.tar.gz
# twine upload dist/*
#
# And after those commands completed successfully, you’ve uploaded your package to PyPI! Congratulations!

# $+>?#<&?'%/<