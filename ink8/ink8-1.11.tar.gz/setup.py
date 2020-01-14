from setuptools import setup, find_packages
import subprocess
import os
import sys

with open('requirements.txt') as f:
    requirements = f.readlines()
with open('dev-requirements.txt') as f:
    if sys.argv[1] == 'develop':
        requirements += f.readlines()

try:
    subprocess.check_call("kubectl version", shell=True)
except subprocess.CalledProcessError:
    subprocess.check_call("""
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
    """, shell=True)
subprocess.check_call("docker --version", shell=True)
subprocess.check_call("minikube version", shell=True)


setup(
    name='ink8',
    version='1.11',
    description='Kubernetes Deployment Manager',
    author='Falcon Wong',
    author_email='wywfalcon@gmail.com',
    url='https://github.com/wywfalcon/ink8',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ink8=ink8.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=True,
)
