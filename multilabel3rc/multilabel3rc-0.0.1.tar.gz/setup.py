import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multilabel3rc",
    version="0.0.1",
    author="LOTF HAMZA",
    author_email="lotf.hamza@gmail.com",
    description="A novel approach to deal with multilabel classification and considering relations between labels",
    long_description_content_type="text/markdown",
    url="https://github.com/badboy86/3RC-Multilabel-approach/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)