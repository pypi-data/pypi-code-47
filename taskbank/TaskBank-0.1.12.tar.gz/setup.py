import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = ["TaskBank"]

setuptools.setup(
    name="TaskBank",
    version="0.1.12",
    author="Alexandre Kempf",
    author_email="alexanre.kempf@cri-paris.org",
    description="A library of machine learning tasks for HackDuck",
    long_description=long_description,
    package_dir={"": "src"},
    packages=["TaskBank"],
    long_description_content_type="text/markdown",
    url="https://github.com/AlexandreKempf/TaskBank",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
