from setuptools import find_packages, setup

EXTRAS_REQUIRE: dict = {
    "tests": [
        "pytest==5.3.2",
        "pytest-cov==2.8.1",
        "pytest-asyncio==0.10.0",
        "asynctest==0.13.0",
    ],
    "lint": ["mypy==0.761", "flake8==3.7.9", "isort==4.3.21", "black==19.10b0"],
    "docs": ["mkdocs==1.0.4", "mkdocs-material==4.6.0", "mkautodoc==0.3.0"],
}

EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["bump2version", "twine"]
)


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="aioboot",
    version="0.3.0",
    description="Python asynchronous application framework.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Anton Ruhlov",
    author_email="antonruhlov@gmail.com",
    url="https://github.com/antonrh/aioboot",
    packages=find_packages("src", exclude=("test*",)),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["starlette==0.13.0", "click==7.0", "injector==0.18.2"],
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    zip_safe=False,
    keywords=["starlette", "asgi", "click", "web", "api", "async"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    project_urls={},
)
