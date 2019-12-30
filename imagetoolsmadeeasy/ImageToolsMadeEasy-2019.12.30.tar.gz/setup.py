import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ImageToolsMadeEasy",
    version="2019.12.30",
    author="Paul Baumgarten",
    author_email="pbaumgarten@gmail.com",
    description="Tools to simplify using face detection and ArUco recognition with PIL image objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulbaumgarten/ImageToolsMadyEasy",
    packages=setuptools.find_packages(),
    keywords='PIL pillow opencv aruco haarcascades',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy','opencv-contrib-python', 'pillow'],
    python_requires='>=3'
)