from setuptools import setup

setup(
    name='solution-efe-database',
    version='1.0.0',
    description='Paquete de base de datos',
    author='Rulman Ferro',
    author_email='rulman26@gmail.com',
    license='MIT',
    packages=['solution_efe_database'],
    python_requires='>=3.6',
    install_requires=['PyMySQL','solution_efe_config']
)