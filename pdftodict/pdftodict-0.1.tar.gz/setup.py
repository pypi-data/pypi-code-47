from distutils.core import setup


setup(
    name = 'pdftodict',
    packages = ['pdftodict'],
    version = '0.1',
    license='MIT',
    description = 'convert pdf to dict',
    author = 'Myroslav Zadoiian',
    author_email = 'konzamir@gmail.com',
    url = 'https://github.com/konzamir/pdf-to-dict',
    download_url = 'https://github.com/konzamir/pdf-to-dict/archive/v_01.tar.gz',
    keywords = ['pdf'],
    install_requires=[
        'pdfquery',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3', 
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
