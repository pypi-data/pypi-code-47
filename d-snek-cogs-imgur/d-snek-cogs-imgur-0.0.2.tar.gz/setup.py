import setuptools

setuptools.setup(
      name="d-snek-cogs-imgur",
      version="0.0.2",
      author="Jonathan de Jong",
      author_email="jonathan@automatia.nl",
      description="Discord SNEK Cog; Imgur",
      url="https://git.jboi.dev/ShadowJonathan/snek-imgur",
      packages=['cogs.imgur'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires=">=3.6",
      install_requires=["d-snek>=1.2.4", "discord.py>=1.2.5", "imgurpython>=1.1.7"],
      setup_requires=["wheel"],
      extras_require={
            "dev": ["ipython", "twine"],
      }
)
