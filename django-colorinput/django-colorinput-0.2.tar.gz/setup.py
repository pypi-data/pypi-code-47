import setuptools

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-colorinput',
    version='0.2',
    author='Gabriel Niebler',
    author_email='gabriel.niebler@gmail.com',
    description='Color fields for Django models and forms '
                'using HTML5 native color type input elements',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/der-gabe/django-colorinput',
    packages=setuptools.find_packages(),
    package_data={
        'colorinput': ['templates/colorinput/widgets/colorinput.html'],
    },
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
