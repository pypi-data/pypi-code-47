from setuptools import setup, find_packages

setup(
	name = 'web-parser',
	version = '0.1.0',
	description = 'This is a parser tool which made all the stuff for you',
	author = 'Ivan Vinogradov',
	py_modules = ["web-parser", "requests", "bs4"],
	package_dir = {'': 'src'},
	python_requires='>=3.6',
	author_email="author@example.com",
    long_description= "With this little tool you can parse from websites text, image files, video files and also some high rescued data. An explanaton will come after my website is ready.",
    long_description_content_type="text/markdown",
    url="https://www.bit.ly/bestf2l",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)