#  Copyright (C) 2016-2020  Kyle.Hwang <upday7[at]163.com>
#  #
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version, with the additions
#  listed at the end of the accompanied license file.
#  #
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#  #
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#  #
#  NOTE: This program is subject to certain additional terms pursuant to
#  Section 7 of the GNU Affero General Public License.  You should have
#  received a copy of these additional terms immediately following the
#  terms and conditions of the GNU Affero General Public License which
#  accompanied this program.

from distutils.core import setup
from pathlib import Path

from setuptools import find_packages

try:
    long_description = Path("readme.md").read_text()
except FileNotFoundError:
    long_description = ""

setup(
    name="web_dict",  # How you named your package folder (MyLib)
    packages=find_packages(),  # Chose the same as "name"
    description="parser class for vaiouse online-dict, e.g. collinsdictionary/lexico/vocabulary/spanishdict etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.86",  # Start with a small number and increase it with every change you make
    license="agpl-3.0",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    author="Kyle, Hwang",  # Type in your name
    author_email="upday7@163.com",  # Type in your E-Mail
    url="https://github.com/upday7/web_dict",  # Provide either the link to your github or to your website
    keywords=[
        "dictionary",
        "spanish",
        "english",
        "chinese",
        "collins",
        "oxford",
        "lexico",
    ],
    install_requires=["bs4", "requests",],  # I get to this in a second
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Programming Language :: Python :: 3.8",
    ],
)
