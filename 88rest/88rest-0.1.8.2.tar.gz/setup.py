import setuptools

setuptools.setup(
    name="88rest",
    version="0.1.8.2",
    author="Rimba Prayoga",
    author_email="rimba47prayoga@gmail.com",
    description="88 Rest Framework",
    url="http://pypi.python.org/pypi/88rest/",
    packages=["rest88"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "Django >= 2.2.8, < 3",
        "django-rest-framework",
        "requests",
        "88orm"
    ]
)
