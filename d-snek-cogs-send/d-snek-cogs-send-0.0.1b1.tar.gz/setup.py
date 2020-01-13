import setuptools

setuptools.setup(
      name="d-snek-cogs-send",
      version="0.0.1b1",
      author="Jonathan de Jong",
      author_email="jonathan@automatia.nl",
      description="Discord SNEK Cog; Send",
      url="https://git.jboi.dev/ShadowJonathan/snek-send",
      packages=['cogs.send'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires=">=3.6",
      install_requires=["d-snek>=1.2.4", "discord.py>=1.2.5", "emoji>=0.5.4"],
      setup_requires=["wheel"],
      extras_require={
            "dev": ["ipython", "twine"],
      }
)
