import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "pineapple", "VERSION"), encoding="utf-8") as f:
    version = f.read()

setuptools.setup(
    name="sg_pineapple",
    version=version,
    description="Pineapple software, visual scripting for automating API testing",
    url="https://github.com/societe-generale/Pineapple",
    author="SG",
    author_email="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Interpreters",
        "Topic :: System :: Benchmark",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="visual scripting node orchestration scenario api",
    package_dir={"": "pineapple"},
    packages=[
        "pineapple_core.core",
        "pineapple_core.utils",
        "pineapple_core.static_analysis",
        "pineapple_core",
        "pineapple_nodes.nodes",
        "pineapple_nodes.utils",
        "pineapple_nodes",
        "pineapple_server",
        "pineapple_server.server",
    ],
    install_requires=["klotan==1.7.0", "nq==4.0.1"],
    extras_require={"tests": ["pytest", "flake8", "pytest-cov"]},
    entry_points={
        "console_scripts": ["pineapple_server=pineapple_server.server.webserver:run"]
    },
    project_urls={
        "Bug Reports": "https://sgithub.fr.world.socgen/ktollec111518/Pineapple/issues",
        "Source": "https://sgithub.fr.world.socgen/ktollec111518/Pineapple",
    },
)
