import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="ptoaster",
    version="1.0.0",
    author="PySimpleGUI",
    author_email="mike@PySimpleGUI.org",
    install_requires=['PySimpleGUI', ],
    description="Display a toaster-style message with an icon, title and message at any location on your screen. Option to fade in / fade out",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI PySimpleGUI tkinter toaster notification",
    url="https://github.com/PySimpleGUI/ptoaster",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ),
)