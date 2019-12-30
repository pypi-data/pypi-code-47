import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cognitivegeo',
    version='1.1',
    packages=setuptools.find_packages(),
    description='A python tool for geoscience data analysis',
    author='GeoPy Team',
    author_email='geopy.info@gmail.com',
    url='https://geopyteam.wixsite.com/cognitivegeo',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['Geoscience', 'Seismic'],
    install_requires=[
        'PyQt5<5.10',
        'matplotlib',
        'vispy',
        'numpy',
        'scipy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)