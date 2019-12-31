from pathlib import Path

from setuptools import setup, find_packages

readme = Path('README.md').read_text()
history = Path('HISTORY.md').read_text()

requirements = Path('requirements.txt').read_text().splitlines()
setup_requirements = ['wheel']
test_requirements = Path('requirements_dev.txt').read_text().splitlines()

setup(
    name="nidhoggr_core",
    version="0.1.0",
    license="MIT",
    description="Domain model for nidhoggr",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author="Andriy Kushnir (Orhideous)",
    author_email="me@orhideous.name",
    url="https://git.mc4ep.org/mc4ep/nidhoggr-core",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    keywords=["Minecraft", "Yggdrasil", "Authentication", ],
    setup_requires=setup_requirements,
    install_requires=requirements,
)
