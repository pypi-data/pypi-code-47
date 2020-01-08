import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'jokettt',
    packages = setuptools.find_packages(),
    version = '1.0.0',
    license = 'MIT',
    author = 'Francesco Piantini',
    author_email = 'francesco.piantini@gmail.com',
    description = 'A Tic Tac Toe game developed by joke',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/fpiantini/jokettt',
    download_url = 'https://github.com/fpiantini/jokettt/archive/v1.0.0.tar.gz',
    install_requires=[
          'numpy',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires='>=3.6',
)

