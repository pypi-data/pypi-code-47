from setuptools import setup

setup(name='contendo_finance_insights',
    version='0.1.26',
    description='contendo.ai finance insights package',
    url='https://github.com/Yahalis/contendo_finance/tree/master/finance_insights',
    author='Yahali Sherman, contendo.ai',
    author_email='yahali@contendo.ai',
    license='APACHE2',
    packages=['contendo_finance_insights'],
    install_requires=[
        'ta',
        'statsmodels==0.10.1',
        'newspaper3k',
        'nltk',
        'google-cloud-bigquery',
        'google-cloud-storage',
        'python-dotenv',
        'pytrends',
        # 'fastai',
        'contendo_utils',
    ],
      include_package_data=True,
      zip_safe=False)
