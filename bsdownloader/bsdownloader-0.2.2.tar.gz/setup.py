import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fp:
    install_requires = fp.read()

setuptools.setup(
    name="bsdownloader",
    version="0.2.2",
    author="Aleksey Pestov",
    author_email="aleksey191295@gmail.com",
    description="Song downloader for Beat Saber",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Norne9/beatsaber-downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["bs-downloader = bsdownloader.__main__:main", "bsdownloader = bsdownloader.__main__:main"]
    },
)
