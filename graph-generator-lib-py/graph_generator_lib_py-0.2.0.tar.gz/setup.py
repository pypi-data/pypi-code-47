from setuptools import setup, find_packages

setup(
    name="graph_generator_lib_py",
    version="0.2.0",
    description="Library for generating graphs for Grapls",
    url="https://github.com/insanitybit/ggraph-generator-lib-py/",
    author="insanitybit",
    author_email="insanitybit@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
    packages=find_packages(),
    package_data={
        'graph_generator_lib_py': ["py.typed"],
    },
    include_package_data=True,
    install_requires=['protobuf'],
)
