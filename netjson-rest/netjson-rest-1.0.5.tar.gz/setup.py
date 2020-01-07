from setuptools import setup

# reading long description from file
# with open('DESCRIPTION.txt') as file:
long_description = '''netjson-rest
======

A simple flask rest API's to convert from json config to openwrt and vice versa

The code is Python 2, but Python 3 compatible.


![diagram](Diagram.JPG)

------------
Installation
------------
```
pip install netjson-rest
```
For a manual installation
------------
```

   mkdir netjson-rest
   wget git@github.com:umeshahp/netjson-rest.git
   cd netjson-rest
   python setup.py install
   cd netjsonFlaskRest
   python flaskRestAPI.py

```



##Usage:

Invoke this API to convert from json  to openwrt by  http://IP:6000/api/v1/netjson-config/jsontoopenwrt/

```
data = {
    "hostname" :  "spanidea",
    "timezone" :  "IST",
    "radios" : [{
    "name" : "Spanidea",
    "protocol" : "802.11ac" ,
    "channel" : 36,
    "channel_width" : 20,
    "tx_power " : 10,
    "country" : "IN"

        }
]
,
"wireless": [
        {
            "name": "lo",
            "type": "wireless",
            "addresses": [
                {
                    "address": "127.0.0.1",
                    "mask": 8,
                    "proto": "static",
                    "family": "ipv4"
                }
            ]
        }
    ]
}
```
## request above endpoint from python
```
x = request.post(data =data, url = 'http://<IP>:6000/api/v1/netjson-config/jsontoopenwrt/')

```

##Call this to convert from  openwrt to json : http://<IP>:6000/api/v1/netjson-config/openwrttojson/
## Example to request from  python
```
multipart_form_data = {
    'file2': ('custom_file_name.zip', open('myfile.zip', 'rb')),
    'action': (None, 'store'),
    'path': (None, '/path1')
}

x = request.post(data = multipart_form_data , url = 'http://<IP>:6000/api/v1/netjson-config/openwrttojson/', files=multipart_form_data )
```'''

# specify requirements of your package here
REQUIREMENTS = ['requests','netjsonconfig', 'flask']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    #'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

# calling the setup function
setup(name='netjson-rest',
      version='1.0.5',
      description='Rest API to convert openwrt config to json and vice versa using flask',
      #long_description=long_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
      url='https://github.com/umeshahp/netjson-rest',
      author='Umesha HP',
      author_email='hpu89@yahoo.com',
      license='GPLV3',
      packages=['netjsonFlaskRest'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='Rest API for netjson config'
      )
