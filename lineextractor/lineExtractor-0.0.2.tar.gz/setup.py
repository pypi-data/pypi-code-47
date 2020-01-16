import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="lineExtractor",
  version="0.0.2",
  description="A python CLI tool that allows you to extract certain lines from text files and transfer them to another file",
  long_description=README,
  long_description_content_type="text/markdown",
  author="kvanland",
  author_email="kylevanlandingham9+lineExtractor@gmail.com",
  license="MIT",
  packages=["lineExtractor"],
  zip_safe=False,
  entry_points={
      'console_scripts': [
          'lineExtractor = lineExtractor.__main__:main'
          ]
  }
)