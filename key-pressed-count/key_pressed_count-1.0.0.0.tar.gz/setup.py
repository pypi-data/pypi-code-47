from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="key_pressed_count",
    version="1.0.0.0",
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
    entry_points={
            "console_scripts": [
                'key-pressed-count=key_pressed_count.keycount:main',
            ]
        }
)
