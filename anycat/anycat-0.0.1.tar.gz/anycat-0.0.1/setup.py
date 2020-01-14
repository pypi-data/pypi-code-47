import setuptools

with open('README.md') as fin:
    long_description = fin.read()

with open('anycat') as fin:
    version_line = [l for l in fin if l.startswith('VERSION =')][0]
    version = version_line.strip().split(' ', 2)[2].strip("'")

setuptools.setup(
    name="anycat",
    version=version,
    author="Michael Penkov",
    author_email="m@penkov.dev",
    description="UNIX cat with read support for S3, SSH, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpenkov/anycat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['smart_open'],
    scripts=['anycat'],
)
