# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mtcli', 'mtcli.indicator']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'python-dotenv>=0.10.3,<0.11.0']

entry_points = \
{'console_scripts': ['atr = mtcli.cli:atr',
                     'bars = mtcli.cli:bars',
                     'ema = mtcli.cli:ema',
                     'fib = mtcli.cli:fib',
                     'mt = mtcli.cli:cli',
                     'sma = mtcli.cli:sma']}

setup_kwargs = {
    'name': 'mtcli',
    'version': '0.4.6',
    'description': 'Utilitario de linha de comando para leitura de graficos do MetaTrader 5',
    'long_description': '=========\nmtcli\n=========\n\n.. image:: https://img.shields.io/pypi/v/mtcli.svg\n        :target: https://pypi.python.org/pypi/mtcli\n\n.. image:: https://readthedocs.org/projects/mtcli/badge/?version=latest\n        :target: https://mtcli.readthedocs.io/en/latest/?badge=latest\n        :alt: Status da Documentação\n\n\nUtilitário de linha de comando para leitura de gráficos do MetaTrader 5.\n\n* Free software: MIT license\n* Documentação: https://mtcli.readthedocs.io.\n\nPré-requisitos\n---------------\n\n* `MetaTrader 5`_ - plataforma de trading.\n* `GeraCSV.ex5`_ - robô executado no MetaTrader 5.\n\n.. _MetaTrader 5: https://www.metatrader5.com/\n.. _GeraCSV.ex5: https://drive.google.com/open?id=1jSSCRJnRg8Ag_sX_ZZAT4YJ2xnncSSAe\n\nInstalação\n-----------\n\n.. code-block:: console\n\n    pip install mtcli\n\nProcedimento no MetaTrader 5\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nFaça o download do `GeraCSV.ex5`_.\n\n1. Execute o MetaTrader 5 e abra um gráfico.\n2. Execute o GeraCSV.ex5.\n3. Selecione a opção "anexar ao gráfico" no menu de contexto do GeraCSV.ex5.\n\n.. _GeraCSV.ex5: https://drive.google.com/open?id=1jSSCRJnRg8Ag_sX_ZZAT4YJ2xnncSSAe\n\n\nArquivo .env\n~~~~~~~~~~~~~\n\n\nCrie um arquivo .env na pasta raiz do Windows com o conteúdo abaixo:\n\nDIGITS="2"\n\nCSV_PATH=[caminho_dos_arquivos_do_metatrader5]\n\n\nUso\n---\n\nPara exibir as últimas 20 barras do diário do winq19:\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -c 20\n\nPara exibir o canal das últimas 20 barras do diário do winq19:\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -v ch -c 20\n\nPara exibir o preço de fechamento das últimas 20 barras do diário do winq19:\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -v c -c 20\n\nPara exibir o preço máximo das últimas 20 barras do diário do winq19:\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -v h -c 20\n\nPara exibir o preço mínimo das últimas 20 barras do diário do winq19\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -v l -c 20\n\nPara exibir o range das últimas 20 barras do diário do winq19:\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -v r -c 20\n\nPara exibir o volume das últimas 20 barras do diário do winq19:\n\n.. code-block:: console\n\n    mt bars winq19 -p daily -v vol -c 20\n\nPara exibir o ATR(14) do diário do winq19:\n\n.. code-block:: console\n\n    mt atr winq19 -p daily\n\nPara exibir o ATR(20) do diário do winq19:\n\n.. code-block:: console\n\n    mt atr winq19 -p daily -c 20\n\nPara exibir a média móvel aritmética de 20 períodos do diário do winq19:\n\n.. code-block:: console\n\n    mt sma winq19 -p daily -c 20\n\nPara exibir a média móvel exponencial de 20 períodos do diário do winq19:\n\n.. code-block:: console\n\n    mt ema winq19 -p daily -c 20\n\nPara exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de alta:\n\n.. code-block:: console\n\n    mt fib 103900 102100 h\n\nPara exibir as retrações e extensões de Fibonacci entre 103900 e 102100 na tendência de baixa:\n\n.. code-block:: console\n\n    mt fib 103900 102100 l\n',
    'author': 'Valmir Franca',
    'author_email': 'vfranca3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vfranca/mtcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
