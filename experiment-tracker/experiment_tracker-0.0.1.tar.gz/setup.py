import setuptools

setuptools.setup(
  name = 'experiment_tracker',
  version = '0.0.1',
  author = 'Markus Zopf',
  description = 'Simple tool to track experiments by writing parameters and corresponding results into an SQL database.',
  url = 'https://github.com/MarkusZopf/Experiment-Tracker',
  packages = ['experiment_tracker'],
  install_requires=[
          'pymysql',
      ],
  classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
  ],
   python_requires='>=3.7.3',
)