import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loki-pkg",
    version="0.0.1.dev1",
    author="Luis Soto",
    author_email="luis-vicente.soto-salinas@dxc.com",
    description="REST API operations for tibco bpm amx 4.3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["requests==2.22.0", "urllib3==1.25.7"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
    python_requires='==2.7',
)
