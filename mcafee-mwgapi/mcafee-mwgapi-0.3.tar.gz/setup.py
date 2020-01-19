import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="mcafee-mwgapi", # Replace with your own username
    version="0.3",
    author="Ipv6Python",
    author_email="ramipv6@gmail.com",
    description="Mcafee Web Gateway API functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ipv6Python/mcafee-mwgapi",
    packages=setuptools.find_packages(),
    license='MIT',
    keywords='mcafee webgateway api development',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
