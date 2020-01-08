import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RpiSerial", # Replace with your own username
    version="0.0.2",
    author="Ashish Sharma",
    author_email="ashishbhardwaj023@gmail.com",
    description="All Serial Device Interface with Raspberry Pi, Jetson nano, etc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ashish1743/Serial_Device",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
