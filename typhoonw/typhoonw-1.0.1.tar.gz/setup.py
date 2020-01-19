from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='typhoonw',
    version='1.0.1',
    author='dakele',
    author_email='wmxy123@yeah.net',
    description='typhoon analysing website for yyp',
    long_description = long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==1.1.1',
        'Flask-SQLAlchemy==2.4.1',
        'pytest==4.6.8',
        'coverage==5.0.1',
        'pymysql==0.9.3',
        'cryptography==2.8',
        'Flask-Excel==0.0.7',
        'pyexcel-xlsx==0.5.7',
        'pyexcel-xls==0.5.8',
        'pyexcel-handsontable==0.0.2',
        'flask-bootstrap==3.3.7.1',
        'gunicorn==19.10.0',
        'gevent==1.4.0',
        'pip==19.3.1',
    ],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage==5.0.1'],
    },
    python_requires='>=2.7',
)