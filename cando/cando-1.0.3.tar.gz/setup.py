from setuptools import setup

setup(
    name = 'cando',
    py_modules=['cando'],
    version='1.0.3',
    description='Python USB-CAN(Cando & Cando_pro) access module',
    author='Codenocold',
    author_email='codenocold@gmail.com',
    license='BSD',
    url='https://www.taobao.com',
    keywords = ['Cando', 'Cando_pro', 'USB-CAN'],
    install_requires = [
      'PyUSB==1.0.2',    # Required to access USB devices from Python through libusb
    ],
)
