from distutils.core import setup

setup(
    name='armapy',
    version='0.8.5',
    packages=['armapy', 'armapy.plot'],
    url='',
    license='GPL',
    author='Patrick Rauer',
    author_email='j.p.rauer@sron.nl',
    description='Package to calculate magnitudes from a spectra',
    install_requires=['astropy', 'numpy', 'scipy'],
    package_data={
          '': ['./alpha_lyr_stis_006.fits',
               './local/shortcuts.ini']
      },
)
