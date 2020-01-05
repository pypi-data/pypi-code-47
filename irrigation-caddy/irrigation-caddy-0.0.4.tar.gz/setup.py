import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="irrigation-caddy",
    version="0.0.4",
    author="Clay Sampson",
    author_email="pdgeek@gmail.com",
    description="Irrigation Caddy Control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sampscl/irrigation_caddy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
