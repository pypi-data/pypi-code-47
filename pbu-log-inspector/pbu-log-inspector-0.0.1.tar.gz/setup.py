from setuptools import setup

setup(name="pbu-log-inspector",
      version="0.0.1",
      description="Flask endpoint delivering filtered log messages via REST",
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
