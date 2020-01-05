from setuptools import setup

setup(
    name="flake8-profiles",
    license="MIT",
    version="0.1.0",
    description="profiles for flake8",
    author="Leif Walsh",
    author_email="leif@twosigma.com",
    url="https://github.com/twosigma/flake8-profiles",
    py_modules=["flake8_profiles"],
    install_requires=[
        "flake8 >= 3",
        "six",
    ],
    entry_points={
        "flake8.report": [
            "CNF101 = flake8_profiles:ProfilePlugin",
        ],
    },
)
