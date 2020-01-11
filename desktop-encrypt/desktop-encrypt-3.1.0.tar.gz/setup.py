from setuptools import setup

setup(name='desktop-encrypt',
      version='3.1.0',
      description='keep desktop folders encrypted',
      url='http://github.com/geavioleta/desktop-encrypt',
      author='geavioleta',
      author_email='geavioleta@protonmail.com',
      license='MIT',
      packages=['desktopencrypt'],
      entry_points = {
          'console_scripts': ['desktop-lock=desktopencrypt.lock:lock', 'desktop-unlock=desktopencrypt.unlock:unlock', 'desktop-keygen=desktopencrypt.keygen:keygen'],
      },
      install_requires=['eciespy', 'ecdsa'],
      python_requires='>=3.5',
      zip_safe=False)