from setuptools import setup

setup(
    name='mc_PIH',
    version='0.0.1',
    author='Hugn_王海涛',
    author_email='wang1183478375@outlook.com',
    install_requires=['opencv-python>=4.1.2.30'
                      ],
    data_files=[('',['mc_PIH.py']),
                ('',['PIH.py'])
                ],
    include_package_data = True, 
    zip_safe=False,
    )