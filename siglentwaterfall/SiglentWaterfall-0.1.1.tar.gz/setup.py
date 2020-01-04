from setuptools import setup, find_packages

setup(
    name='SiglentWaterfall',
    version='0.1.1',
    license='MIT',
    packages=['siglent'],
    description='Waterfall Siglent scope traces',
    author="Eric Waller",
    url="https://github.com/ewwaller/siglentwaterfall",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Click', 'pyqtgraph', 'PyQt5', 'PyOpenGL', 'scipy', 'pyvisa',
    ],
    entry_points={
        'console_scripts': ['siglent=siglent.__main__:main', ], },
    python_requires='>=3.6')


