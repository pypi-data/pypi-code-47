from setuptools import setup, find_packages

setup(
    name = "kakao-i-python",
    version = "0.1",
    description = "python module to use kakao i skill",
    author = "Jeongin Lee",
    author_email = "jil8885@hanyang.ac.kr",
    url = "https://github.com/jil8885/kakao-i-python",
    # download_url = "",
    install_requires = [],
    packages = find_packages(exclude=[]),
    keywords = ["kakao-i"],
    python_requires = ">=3",
    pacakge_data = {},
    zip_safe = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],    
)