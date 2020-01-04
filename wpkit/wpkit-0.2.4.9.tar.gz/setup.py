import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wpkit", # Replace with your own username
    version="0.2.4.9",
    author="WangPei",
    author_email="1535376447@qq.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Peiiii/wpkit",
    packages=setuptools.find_packages(),
    package_dir={'wpkit':'wpkit'},
    package_data={'wpkit':[
        'data/*',
        'data/templates/*','data/demos/*','data/static/*','data/static/js/*','data/static/css/*',
        'data/static/html/*','data/*/*','data/*/*/*','data/*/*/*/*','data/*/*/*/*/*','data/*/*/*/*/*'
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)