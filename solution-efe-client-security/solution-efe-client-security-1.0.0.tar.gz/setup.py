from setuptools import setup

setup(
    name='solution-efe-client-security',
    version='1.0.0',
    description='Paquete de preparacion',
    author='Rulman Ferro',
    author_email='rulman26@gmail.com',
    license='MIT',
    packages=['solution_efe_client_security'],
    python_requires='>=3.6',
    install_requires=['Flask','solution_efe_config']
)