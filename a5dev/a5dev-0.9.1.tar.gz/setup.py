import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="a5dev", # Replace with your own username
    version="0.9.1",
    author="Ankit Saini",
    author_email="ankitsaini100205@gmail.com",
    description="Helper library for day to day task in a ml engineer's life.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankitsainidev/a5dev",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        'numpy',
        'opencv-python',
        'kaggle',
        'torch>=1.0.0',
        'wget',
        'requests'
    ]
)