import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alert", # Replace with your own username
    version="0.0.2",
    author="Rehan Guha",
    py_modules=["alert"],
    license='gpl-3.0',
    author_email="rehanguha29@gmail.com",
    description="A quick package to raise alerts for long running programs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rehanguha/alert",
    package_dir={'': 'alert'},
    packages=setuptools.find_packages(),
    keywords = ['alert', 'log', 'mail', 'email', 'smtplib'],
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Topic :: Scientific/Engineering",
        'Intended Audience :: Developers',
    ],
    python_requires='>=2.7',
    install_requires=[],
)
