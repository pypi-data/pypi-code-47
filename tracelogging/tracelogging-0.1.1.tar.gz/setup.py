from setuptools import setup
import tracelogging


author = 'bnbdr'
setup(
    name='tracelogging',
    version='.'.join(map(str, tracelogging.version)),
    author=author,
    author_email='bad.32@outlook.com',
    url='https://github.com/{}/tracelogging'.format(author),
    description="python tracelogging for windows",
    long_description=tracelogging.__doc__,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords='windows tracelogging python etw trace',
    py_modules=['tracelogging'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
)
