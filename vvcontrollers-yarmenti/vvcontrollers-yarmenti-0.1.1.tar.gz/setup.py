
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vvcontrollers-yarmenti",
    version="0.1.1",
    author="yarmenti",
    author_email="yannick.armenti@gmail.com",
    description="Helpers to use voila-vuetify template for voila-dashboards.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yarmenti/py_vvcontrollers",
    packages=setuptools.find_packages(),
    install_requires=[
        "pubsub-yarmenti>=0.2.2",
        "ipyvuetify>=1.1.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
