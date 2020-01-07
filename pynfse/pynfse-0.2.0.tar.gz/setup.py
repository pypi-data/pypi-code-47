# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynfse',
 'pynfse.base',
 'pynfse.nfse',
 'pynfse.nfse.pr',
 'pynfse.nfse.pr.curitiba']

package_data = \
{'': ['*']}

install_requires = \
['PyXB==1.2.5', 'lxml==4.4.1', 'pydantic==1.0', 'signxml==2.6.0', 'zeep==3.4.0']

setup_kwargs = {
    'name': 'pynfse',
    'version': '0.2.0',
    'description': 'Lib para emissão de NFSe',
    'long_description': '# PyNFSe\n[![Code Climate](https://codeclimate.com/github/marcelobelli/PyNFSe/badges/gpa.svg)](https://codeclimate.com/github/marcelobelli/PyNFSe)\n[![Build Status](https://travis-ci.org/marcelobelli/PyNFSe.svg?branch=master)](https://travis-ci.org/marcelobelli/PyNFSe)\n[![Coverage Status](https://coveralls.io/repos/github/marcelobelli/PyNFSe/badge.svg?branch=master)](https://coveralls.io/github/marcelobelli/PyNFSe?branch=master)\n\nA biblioteca PyNFSe funciona como um facilitador para os desenvolvedores que precisam gerir a emissão de Nota Fiscal de Serviços por meio eletrônico. As funcionalidades desta biblioteca são:\n\n* Criação dos XMLs de RPS (Recibo Provisório de Serviço)\n* Criação dos XML dos Lotes RPS.\n* Envio dos lotes de RPSs, realizando a comunicação com o webservice da respectiva prefeitura\n* Consulta e Cancelamento de NFS-es emitidas\n\nAlém disso a PyNFSe possui uma CLI para operação via linha de comando.\n\n## Cidades Atendidas\n\n* Curitiba\n\n## Instalação\n\nVia PyPI\n```console\npip install PyNFSe\n```\n\nou\n```console\ngit clone https://github.com/marcelobelli/PyNFSe.git\ncd PyNFSe\npip install -r requirements.txt\n```\n\n## Problemas\n\n* Descobrir o problema de conexão quando atualiza o requests\npara versões superiores a 2.11.1 e o cryptography está instalado\n\n## Roadmap\n\n* Tornar disponível no PyPI\n* Adicionar novas cidades\n* Documentação\n',
    'author': 'Marcelo Belli',
    'author_email': 'marcelo@belli.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/marcelobelli/PyNFSe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
