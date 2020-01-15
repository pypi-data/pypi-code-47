import os
from setuptools import setup


version = '0.0.1'

readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_file, 'r') as f:
    long_description = f.read()

setup(
    name='utils-django',
    version=version,
    python_requires='>=3.5',
    url='https://gitlab.com/semus/integracao_externa/utils_django',
    author='Paulo Roberto Cruz',
    author_email='paulo.cruz9@gmail.com',
    download_url='https://gitlab.com/semus/integracao_externa/utils_django',
    description="Gerenciador de importação.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    packages=[
        'utils', 'utils.migrations',
    ],
    include_package_data=True,
    license='BSD',
    install_requires=["Django>=3.0", ],
    tests_require=['mock', 'django-environ', 'pytest', 'pytest-django'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Framework :: Django :: 2.1',
                 'Framework :: Django :: 2.2',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Security',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3 :: Only',
                 ],
    test_suite='tests.main',
)