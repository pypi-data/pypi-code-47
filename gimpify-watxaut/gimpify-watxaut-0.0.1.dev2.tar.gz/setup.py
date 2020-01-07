import setuptools

from gimpify.__init__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gimpify-watxaut",
    version=__version__,
    author="watxaut",
    author_email="watxaut@gmail.com",
    description="Just a package to create automatic face image montages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/watxaut/gimpify",
    packages=setuptools.find_packages(where="."),
    keywords="face recognition montage",
    # py_modules=['gimpify', 'gimpify.montages'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    project_urls={
        'Source': 'https://github.com/watxaut/gimpify',
        'Tracker': 'https://github.com/watxaut/gimpify/issues',
    },
    install_requires=[
        "face-recognition>=1.2.3",
        "Pillow>=7.0.0"
    ],
)
