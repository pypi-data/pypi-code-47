import setuptools

setuptools.setup(
      name="d-snek-cogs-tarot",
      version="0.1.0",
      author="Jonathan de Jong",
      author_email="jonathan@automatia.nl",
      description="Discord SNEK Cog; Tarot",
      url="https://git.jboi.dev/ShadowJonathan/snek-tarot",
      packages=['cogs.tarot', 'cogs.tarot.t_data'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires=">=3.6",
      install_requires=["snek>=1.2.3", "discord.py>=1.2.5"],
      setup_requires=["wheel"],
      extras_require={
            "dev": ["ipython", "twine"],
      },
      include_package_data=True
)
