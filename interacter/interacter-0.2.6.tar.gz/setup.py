from distutils.core import setup

setup(
    name='interacter',
    packages=['interacter'],
    version='0.2.6',
    license='MIT',
    description='gRPC server to remote control robots',
    author='Edwinn Gamborino',
    author_email='r04921098@ntu.edu.tw',
    url='https://github.com/ntu-airobo/interacter',
    download_url='https://github.com/ntu-airobo/interacter/archive/v_0.2.6.tar.gz',
    keywords=['robot', 'grpc', 'server'],
    install_requires=[
        'grpcio',
        'hanziconv',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
