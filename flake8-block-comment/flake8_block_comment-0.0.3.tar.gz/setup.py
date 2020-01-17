import setuptools


def get_long_description():
    description = []
    with open('README.md') as f:
        description.append(f.read())
    return '\n\n'.join(description)


setuptools.setup(
    name="flake8_block_comment",
    license="MIT",
    version="0.0.3",
    description="Block comment checker",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Hideki Ikemoto",
    author_email="ikemo333@gmail.com",
    url="https://github.com/ikemo3/flake8-block-comment",
    py_modules=['flake8_block_comment'],
    install_requires=[
        'pycodestyle >= 2.0.0, < 3.0.0',
    ],
    entry_points={
        'flake8.extension': [
            'B000 = flake8_block_comment:BlockCommentChecker',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
