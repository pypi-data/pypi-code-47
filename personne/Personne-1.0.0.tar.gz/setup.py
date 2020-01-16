from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(name='Personne',
      version='1.0.0',
      description="Tester les Personnes",
      long_description=readme(),
      long_description_content_type="text/markdown",
      author="Nassim",
      author_email="nacimessi10@outlook.fr",
      packages=["test"],
      license="MIT",
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
      ],
      include_package_data=True,
      # install_requires=["requests"],
      entry_points={
        "console_scripts": [
            "Python-repo=test.test_Personne:main",
        ]
    },

      
      )