from setuptools import setup

setup(
    name='solution-efe-setup',
    version='1.0.0',
    description='Paquete de preparacion',
    author='Rulman Ferro',
    author_email='rulman26@gmail.com',
    license='MIT',
    packages=['solution_efe_setup'],
    python_requires='>=3.6',
    install_requires=['Flask','flask-swagger-ui','solution_efe_config']
)