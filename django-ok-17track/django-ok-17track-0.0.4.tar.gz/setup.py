from setuptools import setup, find_packages

pkj_name = 'track17'

setup(
    name='django-ok-17track',
    version='0.0.4',
    long_description_content_type='text/x-rst',
    packages=[pkj_name] + [pkj_name + '.' + x for x in find_packages(pkj_name)],
    include_package_data=True,
)
