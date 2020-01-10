from setuptools import setup

with open("README.md", "r") as file:
    long_desc= file.read()

setup(
    name = "slingshot-lawdocs",
    packages = ["slingshot"],
    version = "0.5",
    license = "MIT",
    description = "Slingshot is a Python library bringed on by A Mosca team for creating reproducible procedural documents for Brazilian law-suits.",
    author = "A Mosca",
    author_email = "staff.amosca@gmail.com",
    url = "https://github.com/amosca-team/slingshot/",
    long_description = long_desc,
    long_description_content_type='text/markdown',
    install_requires = ["pdfkit",
                        "pandoc",
                        "markdown"
                        ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7"
    ]
)