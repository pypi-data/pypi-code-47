# encoding =utf-8
from os import path
import codecs
from setuptools import setup, find_packages

setup(
    name='toolkit_bert_ner',
    version='1.0.2',
    description='Use Google\'s BERT for Chinese natural language processing tasks such as named entity recognition and provide server services',
    url='https://github.com/wxl18039675170',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Allen WU',
    author_email='allen.wu18621039969@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'numpy',
        'six',
        'pyzmq>=16.0.0',
        'GPUtil>=1.3.0',
        'termcolor>=1.1',
    ],
    extras_require={
        'cpu': ['tensorflow>=1.10.0'],
        'gpu': ['tensorflow-gpu>=1.10.0'],
        'http': ['flask', 'flask-compress', 'flask-cors', 'flask-json']
    },
    classifiers=(
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ),
    entry_points={
        'console_scripts': ['toolkit_bert_ner_serving=toolkit_bert_ner.runs:start_server',
                            'toolkit_bert_ner_training=toolkit_bert_ner.runs:train_ner'],
    },
    keywords='toolkit_bert_ner nlp ner NER named entity recognition bilstm crf tensorflow machine learning sentence encoding embedding serving',
)
