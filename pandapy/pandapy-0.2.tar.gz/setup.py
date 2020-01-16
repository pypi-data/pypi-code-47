from setuptools import setup, Command

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        global here

        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = glob.glob(os.path.normpath(os.path.join(here, path_spec)))
            for path in [str(p) for p in abs_paths]:
                if not path.startswith(here):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError("%s is not a path inside %s" % (path, here))
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)

setup(name='pandapy',
      version='0.2',
      description='Structured Numpy with Pandas a Click Away',
      url='https://github.com/firmai/pandapy',
      author='snowde',
      author_email='d.snow@firmai.org',
      license='MIT',
      packages=['pandapy'],
      install_requires=[
          'pandas',
          'numpy',
          'scipy',
          'operator',
          'itertools',
          'numpy-groupies'

      ],
      zip_safe=False)
