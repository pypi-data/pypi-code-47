import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()


# get version, the cool way
f_version = open(Path("gimpify/__init__.py"))
for line in f_version.readlines():
    if "__version__" in line:
        version = line.strip().replace(" ", "").replace("__version__=", "").replace('"', "")
        print(version)
        break
else:
    raise Exception("__version__ not found!")
f_version.close()

setuptools.setup(
    name="gimpify-watxaut",
    version=version,
    author="watxaut",
    author_email="watxaut@gmail.com",
    description="Just a package to create automatic face image montages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/watxaut/gimpify",
    # package_dir={'': 'gimpify'},
    packages=setuptools.find_packages(where=".", include=['gimpify', 'gimpify.*'],
                                      exclude=["*.tests", "*.tests.*", "tests.*", "tests/"]),
    keywords="face recognition montage",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    project_urls={
        "Source": "https://github.com/watxaut/gimpify",
        "Tracker": "https://github.com/watxaut/gimpify/issues",
    },
    install_requires=["face-recognition>=1.2.3", "Pillow>=7.0.0"],
)
