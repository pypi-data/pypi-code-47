from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="escrotum",
    description="Minimalist screenshot capture and screen recording program inspired by scrot.",
    long_description=long_description,
    version="1.0.0",
    author='Roger Duran',
    author_email='rogerduran@gmail.com',
    url='https://github.com/Roger/escrotum',
    download_url='https://github.com/Roger/escrotum/archive/1.0.0.tar.gz',
    keywords=['screenshot', 'screen-recording', 'scrot', 'cli'],
    packages=["escrotum"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'python-gobject',
      'xcffib',
    ],
    entry_points={
        'console_scripts': [
            'escrotum = escrotum.main:run',
        ],
    }
)
