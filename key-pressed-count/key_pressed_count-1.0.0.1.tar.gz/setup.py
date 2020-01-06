from setuptools import setup
import os
def readme():
    with open('README.md') as f:
        README = f.read()
    return README
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="key_pressed_count",
    version="1.0.0.1",
    description="A Python package which will count your all keypressed and mouse touch",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Vijayraj72/keylogger-app",
    author="vijay saw",
    author_email="imvijayraj72@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    
    packages=['key_pressed_count'],
    include_package_data=True,
    install_requires=["Xlib","pyxhook"],
    keywords=['keypress count', 'mouse event', 'keyboard event',
              'mouse key press', 'key press', 'keyboard and mouse event'],
    entry_points={
            "console_scripts": [
                'key-pressed-count=key_pressed_count.keycount:main',
            ]
        }
)
