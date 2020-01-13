from setuptools import setup, find_packages

setup(
    name = "midi-webmixer",
    version = "0.0.1",
    author = "Adam Cathersides",
    author_email = "adamcathersides@gmail.com",
    description = ("A web based GUI to control a audio mixer via midi messages"),
    packages = ['mixer'],
    include_package_data = True,
    install_requires = [
        'flask',
        'flask-restful',
        'python-rtmidi',
        'netifaces',
        'click',
        'redis'
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points={
          'console_scripts': [
              'webmixer = mixer.cli:start'
          ]
      }
)
