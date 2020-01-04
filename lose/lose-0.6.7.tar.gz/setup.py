import setuptools

with open('readmePypi.md', 'r') as f:
	ld = f.read()

setuptools.setup(
	name="lose",
	version="0.6.7",
	description="A helper package for handling data in hdf5 format",
	long_description=ld,
	long_description_content_type="text/markdown",
	author="okawo",
	author_email="okawo.198@gmail.com",
	url="https://github.com/okawo80085/lose",
	packages=setuptools.find_packages(),
	install_requires=['tables', 'numpy'],
	license='MIT',
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Operating System :: OS Independent",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Intended Audience :: Science/Research",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Scientific/Engineering :: Artificial Intelligence",
	],
	python_requires='>=3.5',
)
