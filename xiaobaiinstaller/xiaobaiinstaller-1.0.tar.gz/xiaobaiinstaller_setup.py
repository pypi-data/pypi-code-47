import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaobaiinstaller", # Replace with your own username
    version="1.0",
    author="Tser",
    author_email="807447312@qq.com",
    description="Xiaobai Test Install Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/big_touch/",
    packages=setuptools.find_packages(),
    keywords="xiaobai tool test install",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    py_modules = ['xiaobaiinstaller'],
    install_requires=[
    	"requests_html"
    ],
    package_data = {
        'xiaobaiinstaller': ['xiaobaiinstaller.cp37-win_amd64.pyd', 'logo.ico'],
    },
    entry_points={'console_scripts': [
        'xiaobaiinstaller = xiaobaiinstaller.xiaobaiinstaller:main',
    ]},
)
