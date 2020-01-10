#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages

black_widow_src = "src/black_widow"

with open(black_widow_src + "/README.md", "r") as fh:
    long_description = fh.read()

with open(black_widow_src + "/requirements.txt", "r") as fh:
    install_requires = fh.readlines()

setup(
    name="black-widow",
    version='1.6.6',
    author="Fabrizio Fubelli",
    author_email="offensive-hub@protonmail.com",
    description="Offensive penetration testing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/offensive-hub/black-widow",
    packages=find_namespace_packages('src'),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    exclude_package_data={
        'black_widow': ['docs', 'docker', 'resources']
    },
    package_data={
        '': [
            '*.html',
            '*.css',
            '*.js',
            '*.eot', '*.svg', '*.ttf', '*.woff', '*.woff2',
            '*.png', '*.jpg', '*.ico',
            # 'web.wsgi',
            'LICENSE.txt',
            'resources/black-widow-ascii.txt'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Natural Language :: English",
        "Topic :: Education :: Testing",
        'Topic :: Software Development :: Build Tools',
        "Topic :: System :: Clustering",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Hardware :: Symmetric Multi-processing",
        "Topic :: Utilities"
    ],
    entry_points={
        'console_scripts': [
            'black-widow = black_widow:main',
        ]
    },
    python_requires='>=3.6',
    keywords='black-widow penetration testing offensive cyber security pentest sniffing',
    project_urls={
        'Documentation': 'https://docs.black-widow.io',
        'Source': 'https://github.com/offensive-hub/black-widow',
        'Tracker': 'https://github.com/offensive-hub/black-widow/issues',
    },
    install_requires=install_requires
)
