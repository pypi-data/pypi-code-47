import setuptools

setuptools.setup(
    name='sd5gsim',
    version='0.2',
    description='SD5GSim is a 5G network simulator to simulate 5G networks performance under different circumstances using different simulation parameters.',
    url='https://github.com/sarahsaeed-tarining/sd5gsim',
    author='Sarah Saeed',
    author_email='sara.saeed.doulat@gmail.com',
    license='Duquesne',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
