from distutils.core import setup

setup(
    name='kevin_siry_lib_session',
    packages=['kevin_siry_lib_session'],
    version='0.0.2',
    license='MIT',
    description='Manage the creation and the deletion of kevin_siry_lib_session',
    author='ALTEN',
    author_email='kevin.siry@alten.com',
    url='http://gitlab-alten.francecentral.cloudapp.azure.com/mane/lib-session',
    download_url='http://gitlab-alten.francecentral.cloudapp.azure.com/mane/lib-session/mane/lib-session/repository/develop/archive.tar.gz',
    keywords=['SESSION'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
