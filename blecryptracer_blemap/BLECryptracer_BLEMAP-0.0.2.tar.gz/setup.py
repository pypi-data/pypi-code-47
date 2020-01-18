import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BLECryptracer_BLEMAP", # Replace with your own username
    version="0.0.2",
    author="guizos",
    author_email="guizos@mail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guizos/BLECryptracer_BLEMAP",
    packages=['BLECryptracer_BLEMAP'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
