import setuptools
import os

if os.environ.get("CI_COMMIT_TAG"):
    version = os.environ["CI_COMMIT_TAG"]
else:
    version = os.environ["CI_JOB_ID"]

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="gym_shopping_cart",
    version=version,
    description="An OpenAI Gym for Shopping Cart Reinforcement Learning",
    author="Phil Winder",
    author_email="phil@winderresearch.com",
    license="MIT",
    packages=setuptools.find_packages(),
    url="https://gitlab.com/winderresearch/gym-shopping-cart",
    zip_safe=False,
    install_requires=["gym>=0.12.5", "pandas>=0.18.1"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
)
