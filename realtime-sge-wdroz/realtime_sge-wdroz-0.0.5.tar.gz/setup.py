import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line != ""]
    install_reqs = [line for line in lines if not line.startswith("#")]

setuptools.setup(
    name="realtime_sge-wdroz",
    version="0.0.5",
    author="William Droz",
    author_email="william.droz@idiap.ch",
    description="Internal tools to use the SGE grid in realtime at Idiap Research Institute",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.idiap.ch/william.droz/realtime_sge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=install_reqs,
    python_requires=">=3.5",
)
