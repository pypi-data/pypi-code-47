#!/usr/bin/env python3

from setuptools import setup


setup(name='qt5_t5darkstyle',
      version='1.1',
#      install_requires=["PyQT5"],
      python_requires='>=3',
      license="bsd-3-clause",
      description="Dark Stylesheet for QT5",
      long_description_content_type='text/markdown',
      long_description="""# Dark Stylesheet for QT5

the css and icons were inspired by https://github.com/ColinDuquesnoy/QDarkStyleSheet which are Copyright (c) 2013-2018 Colin Duquesnoy

## Usage:

    from qt5_t5darkstyle import darkstyle_css
    widget.setStylesheet(darkstyle_css())

or set your own colors with:

    widget.setStylesheet(darkstyle_css(MY_COLORS_DICT))

""",
      author='Jürgen Herrmann',
      author_email='t-5@t-5.eu',
      url='https://gitlab.com/t-5/qt5_t5darkstyle',
      packages=['qt5_t5darkstyle'],
      package_dir={'qt5_t5darkstyle': 'src'},
      package_data={'': ['src/*.css']},
      include_package_data=True,
     )
