from setuptools import setup

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(name="pbu-log-inspector",
      version="0.0.2",
      description="Flask endpoint delivering filtered log messages via REST",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/ilfrich/pbu-log-inspector",
      author="Peter Ilfrich",
      author_email='peter.ilfrich@au1.ibm.com',
      license="Apache-2.0",
      packages=[
          "loginspect"
      ],
      install_requires=[
          "flask",
      ],
      tests_require=[
          "pytest",
      ],
      zip_safe=False)
