from setuptools import setup, find_packages

setup(
      name="SquidUtils",
      version="0.1.1",
      description="Central server and controller for GiantSquid",
      url="http://gitlab.com/GiantSquid/GiantSquid",
      author="GiantSquid",
      author_email="u@r0t.me",
      license="MIT",
      packages=find_packages(include=['SquidUtils', 'SquidUtils.*']),
      install_requires=[],
      zip_safe=False
)
