from setuptools import setup

setup(
    name='SakuraMysql',
    version='0.1.8',
    description=(
        'mysql orm'
    ),
    long_description='mysql orm',
    author='SVz',
    author_email='903943711@qq.com',
    maintainer='SVz',
    maintainer_email='<903943711@qq.com',
    license='MIT License',
    packages=['sakura', 'tests'],
    package_dir={
        'sakura': 'sakura',
        'tests': 'tests',
    },
    install_requires=['pymysql'],
    python_requires='>=3.6',
    platforms=["all"],
    url='https://github.com/SVz777/Sakura',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
