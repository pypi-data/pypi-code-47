from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="ocrzzz",
    version="1.0.0",
    description="A Python package to get ocr.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/utkarsh-pro/ocr",
    author="Test",
    author_email="test@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ocr"],
    include_package_data=True,
    install_requires=["opencv-python", "numpy"],
    entry_points={
        "console_scripts": [
            "ocr=ocr.Main:main",
        ]
    },
)