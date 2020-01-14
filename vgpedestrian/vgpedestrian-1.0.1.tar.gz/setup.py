from setuptools import setup, find_packages
#TODO Entrypoint stimmt noch nicht
setup(name='vgpedestrian',
      version='1.0.1',
      description='This package implements a visibility graph algorithm to calculate pedestrian ways for open spaces.',
      url='https://git.kinf.wiai.uni-bamberg.de/KinfProjektWS1920/Group4',
      author='Lennart Thamm, Maximilian Thum, Niklas Kriegel, Olha Muzhylovsk',
      author_email='Niklas-Armin.Kriegel@stud.uni-bamberg.de',
      package_dir={'':'vgpedestrian'},
      packages=find_packages("vgpedestrian",exclude=("tests")),
      install_requires=["docopt==0.6.2", "lxml==4.4.1", "Shapely==1.6.4.post2"],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'vgpedestrian = App.app:App.main'
          ]
      },
    )