from setuptools import setup

with open('DESCRIPTION.txt') as file:
    long_description = file.read()

REQUIREMENTS = [
'asn1crypto==1.2.0',
'certifi==2019.11.28',
'cffi==1.13.2',
'chardet==3.0.4',
'Click==7.0',
'cryptography==2.8',
'Flask==1.1.1',
'Flask-SQLAlchemy==2.4.0',
'idna==2.8',
'itsdangerous==1.1.0',
'Jinja2==2.10.3',
'keyboard==0.13.4',
'MarkupSafe==1.1.1',
'nltk==3.4.5',
'numpy==1.17.4',
'pandas==0.25.3',
'PyAudio==0.2.11',
'pycparser==2.19',
'pyodbc==4.0.27',
'pyOpenSSL==19.1.0',
'PySocks==1.7.1',
'python-dateutil==2.8.1',
'pytz==2019.3',
'QDarkStyle==2.7',
'requests==2.22.0',
'six==1.13.0',
'SpeechRecognition==3.6.3',
'SQLAlchemy==1.3.12',
'urllib3==1.25.7',
'Werkzeug==0.16.0',
'win-inet-pton==1.1.0',
'wincertstore==0.2'
]

CLASSIFIERS = [
    "Programming Language :: Python 3.7 ",
]

setup(name='AI_waiter', 
      version='1.0.1', 
      description='Code to read record an order and write to a database', 
      long_description=long_description, 
      url='https://github.com/AltiusBI/wAIter', 
      author='Josie Park and ', 
      author_email='josie.park@altiusdata.com', 
      license='MIT', 
      packages=['src'], 
      install_requires=REQUIREMENTS,
      python_requires = '<3.8' ,
      ) 