
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simimgs-csv",
    version="0.0.1",
    author="Yefei Li",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liyefei737/simimgs",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'opencv-python', 'scikit-image'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
