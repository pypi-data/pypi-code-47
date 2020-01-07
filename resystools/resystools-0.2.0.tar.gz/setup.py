
import setuptools

setuptools.setup(
  name = 'resystools',       
  packages=setuptools.find_packages(),   
  include_package_data=True,
  version = '0.2.0',     
  license='MIT',      
  description = 'The library supports users implementing recommendation algorithms',  
  author = 'Trong Duc Le',                  
  author_email = 'trongduclebk@gmail.com',     
  url = 'https://github.com/DucLeTrong/resystools', 
  download_url = '',   
  keywords = ['RECOMMENDATION', 'RECOMMENDER'],  
  install_requires=[      
          'sklearn',
          'pandas',
          'numpy',
          'tensorboardX>=1.6'
      ],
  classifiers=[
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
# if __name__ == '__main__':
#     setup(**setup_args, install_requires=install_requires)