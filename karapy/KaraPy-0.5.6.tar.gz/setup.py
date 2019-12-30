import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KaraPy", # Replace with your own username
    version="0.5.6",
    author="Pixelboys_TM",
    author_email="none@n.com",
    description="A Kara runtime for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PixelboysTM/KaraPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)