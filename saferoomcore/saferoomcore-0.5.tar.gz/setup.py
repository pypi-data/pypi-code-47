# Import section
import setuptools

# Setup section
setuptools.setup(name='saferoomcore',
      version='0.5',
      description='List of packages used in Saferoom Enterprise',
      long_description='Coming soon',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
      ],
      keywords='saferoom encryption decryption cms evernote onenote',
      url='https://github.com/saferoombiz/saferoomcore',
      author='Alexey Zelenkin',
      author_email='alexey.zelenkin@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(exclude=["tests.py"]),
      include_package_data=True,
      install_requires=[
          'requests',
      ],
      zip_safe=False)
