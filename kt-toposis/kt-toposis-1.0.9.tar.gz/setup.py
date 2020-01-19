from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="kt-toposis",
    version="1.0.9",
    description="A Python package to get toposis rankings for any table.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kartikeytiwari37/Toposis.git",
    author="Kartikey Tiwari",
    author_email="kartikeytiwari37@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    packages=["kt_toposis"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "kt-toposis=kt_toposis.topsis:main",
        ]
    },
)