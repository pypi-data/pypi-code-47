import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonVuetifyMarkdown",
    version="0.1.2",
    description="Adds Vuetify typography classes to various tags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Robert Jauss",
    author_email="robertjauss@gmail.com",
    url="https://gitlab.com/robertjauss/python-vuetify-markdown",
    packages=setuptools.find_packages(),
    py_modules=["PythonVuetifyMarkdown"],
    install_requires=["markdown>=2.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
