import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ambiance_client", # Replace with your own username
    version="0.0.3",
    author="Ben Klang",
    author_email="bklang@wirehack.net",
    description="A Python client for the Elixir Ambiance home automation API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/bklang/ambiance_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
    ],
)
