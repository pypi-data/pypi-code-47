from setuptools import setup
from setuptools import find_packages

NAME = "mulan"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/mulan"
LICENSE = "MIT License"
DESCRIPTION = "木兰诗复读机"

if __name__ == "__main__":
    setup(
        name=NAME,
        version="0.0.3",
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=open("./README.md", "r").read(),
        long_description_content_type='text/markdown',
        entry_points={
            "console_scripts": [
                "mulan=mulan.shell:run"
            ]
        },
        package_data={
            "mulan": ["src/*.txt"]
        },
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6"
    )
