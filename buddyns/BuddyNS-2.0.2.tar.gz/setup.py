import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BuddyNS", # Replace with your own username
    version="2.0.2",
    author="BuddyNS.com",
    author_email="support@buddyns.com",
    description="A python client library to easily consume BuddyNS.com's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.buddyns.com/support/api/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Security",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires='>=2.7',
)
