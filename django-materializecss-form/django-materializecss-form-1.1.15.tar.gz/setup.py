import codecs
import os
import re

from setuptools import setup, find_packages

# import materializecssform




###################################################################

NAME = "django-materializecss-form"
PACKAGES = find_packages(where="materializecssform")
META_PATH = os.path.join("materializecssform", "meta.py")
KEYWORDS = ["materialize", "django", "css", "materializecss", "django forms"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = []

###################################################################


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("uri"),
        version=find_meta("version"),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        package_dir={"": "materializecssform"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        options={"bdist_wheel": {"universal": "1"}},
    )


# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

# setup(

#     name='django-materializecss-form',

#     version=materializecssform.__version__,

#     packages=find_packages(),

#     author="Kal Walkden",

#     author_email="kal@walkden.us",

#     description="A simple Django form template tag to work with Materializecss",
#     long_description=long_description,
#     long_description_content_type="text/markdown",

#     include_package_data=True,

#     url='https://github.com/kalwalkden/django-materializecss-form',
#     classifiers=[
#         "Programming Language :: Python",
#         "Development Status :: 4 - Beta",
#         "Framework :: Django",
#         "Intended Audience :: Developers",
#         "License :: OSI Approved :: MIT License",
#         "Natural Language :: English",
#         "Operating System :: OS Independent",
#         "Programming Language :: Python :: 3.6",
#     ],

#     license="MIT",

#     zip_safe=False
# )
