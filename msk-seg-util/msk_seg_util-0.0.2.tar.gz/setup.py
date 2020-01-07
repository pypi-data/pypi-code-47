import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

REQUIRED_PACKAGES = ['h5py',
                     'matplotlib',
                     'medpy',
                     'numpy',
                     'opencv-python',
                     'pandas',
                     'pyvisstats',
                     'scipy',
                     'seaborn',
                     ]

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='msk_seg_util',
      version='0.0.2',
      description='Python package for MSK segmentation utilities',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      url='https://github.com/ad12/msk_seg_util',
      author='Arjun Desai',
      author_email='arjundd@stanford.edu',
      packages=find_packages(),
      install_requires=REQUIRED_PACKAGES,
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
      ],
      license='MIT',
      python_requires='>=3.6',
)
