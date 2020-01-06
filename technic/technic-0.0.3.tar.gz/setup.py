import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="technic",  # Replace with your own username
    version="0.0.3",
    author="Divyaansh Dandona",
    author_email="divy96@gmail.com",
    description="A python library for Technical Trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dvd9604/technic.git",
    keywords=["trading", "technical", "analysis"],
    install_requires=["numpy", "pandas"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
