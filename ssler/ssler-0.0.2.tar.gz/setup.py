import setuptools

with open("README.md", "r") as fh:  # description to be used in pypi project page
    long_description = fh.read()

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

install_requires = ['flask', 'requests']  # any requirements your package has

setuptools.setup(
    name="ssler",
    version="0.0.2",
    author="Abin Simon",
    author_email="abinsimon10@gmail.com",
    description="Easy SSL for your localhost server",
    url="https://github.com/meain/ssler",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=["ssler"],
    install_requires=install_requires,
    keywords=["ssl", "python", "localhost"],
    classifiers=classifiers,
    entry_points={"console_scripts": ["ssler = ssler.ssler:main"]},
)
