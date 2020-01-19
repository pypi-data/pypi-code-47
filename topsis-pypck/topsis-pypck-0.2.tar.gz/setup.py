import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-pypck", # Replace with your own username
    version="0.2",
    author="Nishchay Mahajan",
    author_email="nmahajan_be17@thapar.edu",
    description="Topsis implementation package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nishchaym/topsis_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
