from setuptools import setup, find_packages
import os

SRC_DIR = os.path.join(os.path.dirname(__name__), 'src')

def get_readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name="keepfresh",
    version="0.0.4",
    description="Filesystem event polling",
    author="Tomas Sheers",
    author_email="t.sheers@outlook.com",
    download_url="https://github.com/reritom/KeepFresh/archive/v0.0.4.tar.gz",
    url="https://github.com/reritom/KeepFresh",
    keywords=["FILESYSTEM", "EVENT", "POLLING"],
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    package_dir={'': SRC_DIR},
    packages=find_packages(SRC_DIR),
    entry_points={
        'console_scripts': [
            'keepfresh = keepfresh.command_line:main [keepfresh]',
        ]
    },
)
