from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

long_desc = open('README.md', 'r').read() 


class InstallScripts(install):
  """Install script"""

  def run(self):
    subprocess.run('curl https://raw.githubusercontent.com/Riqky/Spitzer/master/setup.sh | bash', shell=True)
    install.run(self)


setup(
    cmdclass={'install': InstallScripts},
    name='SpitzerSec',
    version='0.1.7',
    description='A scanner for the first day of a pentest',
    long_description=long_desc,
    author='Rick Theeuwes',
    packages=find_packages(),
    entry_points=
    {'console_scripts': ['spitzer = Spitzer.main:main']},
    install_requires=['xmltodict==0.12.0', 'python-nmap==0.6.1', 'python-docx==0.8.10', 'beautifulsoup4==4.8.1', 'requests==2.22.0', 'tqdm==4.40.2'],
    include_package_data=True,
    package_data={'': ['*.json', 'Netwerkservices.docx', 'logo.png']},
    download_url='https://github.com/Riqky/Spitzer/archive/0.1.7.tar.gz',
    data_files=[('configs', ['Spitzer/config/config.json', 'Spitzer/config/data.json'])],
    long_description_content_type='text/markdown'
)  