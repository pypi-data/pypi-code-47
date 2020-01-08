from setuptools import find_packages, setup

setup(
    name='canvas_api_caller',
    version='1.0.4',
    url="https://github.com/Nudge-Crew/canvas-api-caller",
    author="Noah Scharrenberg",
    author_email="nscharrenberg@hotmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT",
    install_requires=[
        'requests',
        'flask',
        'werkzeug'
    ]
)