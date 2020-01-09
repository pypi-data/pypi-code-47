import setuptools 
from os import path

p = path.abspath(path.dirname(__file__))

with open(path.join(p, 'README.md')) as f:
    README = f.read()



setuptools.setup(
        name="pyQpController", # Replace with your own username
        version="0.0.1",
        author="Yuquan Wang",
        author_email="wyqsnddd@gmail.com",
        description="Python implementation of a multi-objective controller using quadratic programming.",
        # long_description=README,
        # long_description_content_type="text/markdown",
        
        install_requires=[
            "pydart2",
            ],

        url="https://github.com/wyqsnddd/pyQpController",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Operating System :: OS Independent",
            ],
        python_requires='>=3.6',
        )

