import setuptools

setuptools.setup(
      name="d-snek-cogs-find",
      version="0.0.1",
      author="Jonathan de Jong",
      author_email="jonathan@automatia.nl",
      description="Discord SNEK Cog; Find",
      url="https://git.jboi.dev/ShadowJonathan/snek-find",
      packages=['cogs.find'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires=">=3.6",
      install_requires=["d-snek>=1.2.4", "discord.py>=1.2.5", "ruamel-yaml>=0.16.5"],
      setup_requires=["wheel"],
      extras_require={
            "dev": ["ipython", "twine"],
      }
)
