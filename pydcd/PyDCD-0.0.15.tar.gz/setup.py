import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydcd", 
    version="0.0.15",
    author="Kunpeng Zhang & Shaokun Fan & Bruce Golden",
    author_email="shaokunfan@gmail.com",
    description="PyDCD: A Deep Learning-Based Community Detection Software in Python for Large-scale Networks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kpzhang/deepcommunitydetection",
    dependency_links=[
        "https://download.pytorch.org/whl/torch_stable.html"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    py_modules = ["pydcd"],
    install_requires = ['numpy>=1.18', 'networkx>=2.4', 'scikit-learn>=0.21.3', 'scipy>=1.1.0', 'torch>=1.3.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)