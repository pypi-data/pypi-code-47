import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monitor-internet-connection", # Replace with your own username
    version="1.2.0",
    author="Martin Francis O'Connor",
    author_email="cslearncreate@gmail.com",
    description="A Python module to monitor the uptime of the Internet connection and record the time and duration of any downtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mfoc/monitor-internet-connection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)