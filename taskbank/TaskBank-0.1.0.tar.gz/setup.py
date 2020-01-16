import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='TaskBank',
     version='0.1.0',
     author="Alexandre Kempf",
     author_email="alexanre.kempf@cri-paris.org",
     description="A library of machine learning tasks for HackDuck",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/AlexandreKempf/TaskBank",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],)
