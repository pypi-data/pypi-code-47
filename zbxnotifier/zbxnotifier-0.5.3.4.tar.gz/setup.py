from distutils.core import setup


setup(
  name = 'zbxnotifier',
  packages = ['zbxnotifier', 'zbxnotifier/modules', 'zbxnotifier/modules/windowelements', 'zbxnotifier/modules/zabbix'],
  version = '0.5.3.4',
  license='gpl-3.0',
  description = 'Simple Zabbix Notifier Desktop Application',
  author = 'Daniel Kovacs',
  author_email = 'kovacsdanielhun@gmail.com',
  url = 'https://github.com/inframates/zbxnotifier',
  download_url = 'https://github.com/inframates/zbxnotifier/archive/0.5.3.4.tar.gz',
  keywords = ['Zabbix', 'desktop', 'monitoring'],
  install_requires=[
        'PyQt5',
        'py-zabbix',
        'keyring<=18',
        'appdirs',
        'configparser',
        'win10toast'
      ],
  scripts = ['scripts/ZBXNotifier.pyw'],
  classifiers =[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: System :: Monitoring',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3',
  ],
)