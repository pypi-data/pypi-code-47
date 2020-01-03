# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['storybro',
 'storybro.cli',
 'storybro.cli.commands.models',
 'storybro.cli.commands.stories',
 'storybro.data',
 'storybro.data.grammars',
 'storybro.generation',
 'storybro.generation.gpt2',
 'storybro.models',
 'storybro.play',
 'storybro.stories',
 'storybro.story']

package_data = \
{'': ['*'], 'storybro.cli': ['commands/*']}

install_requires = \
['appdirs==1.4.3',
 'click-config-file==0.5.0',
 'click==7.0',
 'cmd2==0.9.22',
 'cryptography>=2.8,<2.9',
 'func_timeout==4.3.5',
 'google-cloud-storage==1.23.0',
 'gsutil==4.46',
 'importlib_resources>=1.0.2,<1.1.0',
 'numpy==1.18.0',
 'playsound==1.2.2',
 'profanityfilter==2.0.6',
 'prompt_toolkit==3.0.2',
 'pyyaml==5.2',
 'regex==2019.12.20',
 'tensorflow==1.15',
 'tracery==0.1.1']

entry_points = \
{'console_scripts': ['storybro = storybro:main']}

setup_kwargs = {
    'name': 'storybro',
    'version': '0.1.0',
    'description': 'A GPT-2 based AI assisted storytelling tool',
    'long_description': "# Storybro\n\nStorybro is a community maintained fork of [AI Dungeon 2](https://github.com/AIDungeon/AIDungeon). AI Dungeon was originally created by [Nick Walton](https://github.com/nickwalton).\n\nVisit our Wiki here: [Storybro wiki](https://github.com/storybro/storybro/wiki)\n\nRead more about AI Dungeon 2 and how it was built [here](https://pcc.cs.byu.edu/2019/11/21/ai-dungeon-2-creating-infinitely-generated-text-adventures-with-deep-learning-language-models/).\n\nThis fork aims to provide:\n- Improvements the original codebase\n- A command-line tool `storybro` for managing models, stories, etc\n- An improved interactive play mode\n- A model registry where models can be downloaded\n- An http web-service exposing most features\n- A Pip installable Python package\n\n### Note\n\nStorybro's AI can use your GPU or CPU. *A GPU will produce AI responses much faster than a CPU.* An nVidia GPU with 12 GB or more of memory, and CUDA installed, **is required** for GPU play. If you do not have such a GPU, you can play on your CPU. However, *each turn can take a couple of minutes or more* for the game to compose its response.\n\n# Playing\n\nThis README only covers installation. To learn how to play visit our [Wiki](http://github.com/storybro/storybro/wiki).\n\n# Installation\n\nInstalling Storybro requires the following software:\n\n- Python 3.4 - 3.7\n\nGrab the source code with Git and clone it to your machine:\n\n    git clone https://github.com/storybro/storybro/\n\n## Windows Installation\n\nStorybro comes with a few Windows Batch scripts to facilitate installation. If you'd like to install manually, see [Manual Installation](#manual-installation).\n\nStorybro uses [Chocolatey](http://chocolatey.org), a package manager, to install dependencies:\n\n1: Using an **ADMINISTRATOR** terminal from the root of this repo:\n\n\n    ./bin/windows/install/install-choco.bat\n\n2: Close your terminal and re-open it.\n    \n3: Now that Chocolatey is installed, install our dependencies and Storybro:\n\n\n    ./bin/windows/install/install-storybro.bat\n\n4: Once installation is done you should be in a shell. You can now use the `storybro` command:\n\n## Linux Installation\n\nStorybro comes with a few shell scripts to faciliate installation. If you'd like to install manually, see [Manual Installation](#manual-installation). \n\nTo install Storybro simply run the install script:\n\n    ./bin/linux/install/install\n    \nYou can now use [Poetry](https://python-poetry.org/) to enter a shell where you can use the `storybro` command:\n\n    poetry shell\n\n## Manual Installation\n\nStorybro is a Python application and uses [Poetry](https://python-poetry.org/) for its environment.\n\nInstall Poetry with Pip:\n\n    $ pip install poetry\n    \nUse Poetry to install Storybro:\n\n    $ poetry install\n    \nUse Poetry to run Storybro:\n\n    $ poetry run storybro\n    \nStorybro uses [Aria2](https://aria2.github.io/) to download models. Make sure that it is installed and on your `$PATH` if you intend to use Storybro to download models.\n\n\nCommunity\n------------------------\n\nStorybro is an open source project. Questions, discussion, and contributions are welcome. Contributions can be anything from new packages to bugfixes, documentation, or even new core features.\n\nResources:\n\n* **Reddit**: [r/AIDungeon](https://www.reddit.com/r/AIDungeon/)\n* **Discord**: [aidungeon discord](https://discord.gg/Dg8Vcz6)\n\n\nContributing\n------------------------\nContributing to Storybro is easy! Just send us a [pull request](https://help.github.com/articles/using-pull-requests/) from your fork. Make sure ``develop`` is the destination branch. \n\nStorybro uses a rough approximation of the [Git Flow](http://nvie.com/posts/a-successful-git-branching-model/) branching model.  The ``develop`` branch contains the latest contributions, and ``master`` is always tagged and points to the latest stable release.\n\nIf you're a contributor, make sure you're testing and playing on `develop`. That's where all the magic is happening (and where we hope bugs stop).\n",
    'author': 'Nick Walton',
    'author_email': 'unknown@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/storybro/storybro',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.8,<3.7.0',
}


setup(**setup_kwargs)
