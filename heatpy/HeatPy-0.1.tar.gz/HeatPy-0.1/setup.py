import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HeatPy", # Replace with your own username
    version="0.1",
    author="Marianna Nezhurina",
    author_email="mariana13019940@gmail.com",
    description="A python package for heat simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marianna13/heatsim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
