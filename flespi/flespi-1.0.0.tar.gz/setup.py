"""Setup file"""
import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="flespi",
  version="1.0.0",
  author="Golden M",
  author_email="support@goldenmcorp.com",
  description="Flespi REST API for Python",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/goldenm-software/flespi-python",
  packages=setuptools.find_packages(),
  python_requires='>=3.6',
)
