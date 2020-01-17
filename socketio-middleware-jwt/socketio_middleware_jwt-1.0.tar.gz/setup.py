from setuptools import setup

setup(
    name='socketio_middleware_jwt',
    version='1.0',
    author='Daniel Pereira Zitei, Carla de Almeida Madureira',
    author_email='daniel.zitei@gmail.com, carla.almadureira@gmail.com',
    packages=['socketio_middleware_jwt'],
    description="This is a middleware for jwt",
    url='https://github.com/keyloguer/socketio_middleware_jwt',
    install_requires=['pyjwt', 'requests', 'flask','flask_middleware_jwt'],
    license="Apache License, Version 2.0"
)