from setuptools import setup


version = "1.0.2"
url = "https://github.com/dopstar/smoking-gun"

if "a" in version:
    dev_status = "3 - Alpha"
elif "b" in version:
    dev_status = "4 - Beta"
else:
    dev_status = "5 - Production/Stable"


with open("README.md") as fd:
    long_description = fd.read()


requirements = None
testing_requirements = [
    "flask",
    "pytest",
    "pytest-cov",
    "wheel",
    "codecov",
    "coverage",
    "mock",
]

linting_requirements = [
    "flake8",
    "bandit",
    "flake8-isort",
    "flake8-quotes",
]


setup(
    name="smoking_gun",
    version=version,
    packages=["smoking_gun"],
    install_requires=requirements,
    tests_require=testing_requirements,
    extras_require={"testing": testing_requirements, "linting": linting_requirements},
    author="Mkhanyisi Madlavana",
    author_email="mmadlavana@gmail.com",
    url=url,
    download_url="{url}/archive/{version}.tar.gz".format(url=url, version=version),
    description="The log capturing library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    keywords=["Smoking", "Gun", "profiling", "tracing", "logging"],
    classifiers=[
        "Development Status :: {0}".format(dev_status),
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Version Control :: Git",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
