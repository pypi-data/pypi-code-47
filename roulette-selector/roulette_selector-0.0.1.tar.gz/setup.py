from setuptools import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="roulette_selector",
    version="0.0.1",
    author="Eric Musa",
    author_email="eric.musa17@gmail.com",
    description="A small roulette-style random selector of weighted options",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://bitbucket.org/Eric-Musa/roulette/",
    py_modules=['roulette_selector'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
