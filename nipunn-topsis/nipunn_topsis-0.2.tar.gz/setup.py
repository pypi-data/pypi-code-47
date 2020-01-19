from distutils.core import setup
setup(
  name = 'nipunn_topsis',         
  packages = ['nipunn_topsis'],   
  version = '0.2',      
  license='MIT',        
  description = 'Implementation of TOPSIS package of R language in python',   
  author = 'Nipunn Malhotra',                   
  author_email = 'nipunnjg@gmail.com',      
  url = 'https://github.com/nipunnmalhotra/nipunn_topsis',   
  download_url = 'https://github.com/nipunnmalhotra/nipunn_topsis/archive/v_01.tar.gz',    
  keywords = ['Perfomance Score', 'Parameter Selection'],   
  install_requires=[           
          
        'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)