from setuptools import setup

setup(
    name='docassemble_wrappers',
    version='0.0.3',
    packages=['docassemble_wrappers'],
    url='https://github.com/silexsistemas/docassemble-wrappers',
    license='MIT',
    author='Roberto Vasconcelos Novaes, Luiz Guilherme Paim, Iasmini Gomes',
    author_email='rnovaes@ufmg.br, luis.paimadv@gmail.com, iasmini@silexsistemas.com.br',
    description='Wrappers to external functionalities and Docassemble API',
    install_requires=[
        'validator-collection-br',
    ],
)
