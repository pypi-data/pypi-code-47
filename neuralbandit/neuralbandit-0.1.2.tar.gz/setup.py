# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neuralbandit']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.1,<2.0.0', 'pandas>=0.25.3,<0.26.0', 'torch>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'neuralbandit',
    'version': '0.1.2',
    'description': 'Reproducing the experiments of the NeuralBandit and BanditForest papers. ',
    'long_description': '# NeuralBandit\n\nThis WIP repository reproduces the experiments of the [NeuralBandit](https://hal.archives-ouvertes.fr/hal-01117311/document) and [BanditForest](http://proceedings.mlr.press/v51/feraud16.html) papers. The code of BanditForest is available [here](https://www.researchgate.net/publication/308305599_Test_code_for_Bandit_Forest_algorithm).\n\n### Table of contents\n- [Steps to reproduce](#steps-to-reproduce)\n- [Citations](#citations)\n    + [NeuralBandit](#neuralbandit-1)\n    + [BanditForest](#banditforest)\n\n### TODO List\n* Doing the requirements.txt\n* Automating the run of experiments\n* NeuralBandit Paper\n    * Implementation of NeuralBandit.A and .B\n    * Adding concept drift to the Game\n\n* BanditForest Paper\n    * Adding Census et Adult dataset\n    * Adding Noise to the reward\n\n### Steps to reproduce\n```python\n\nfrom neuralbandit import get_cov_dataset, ContextualBanditGame, NeuralBandit\nfrom neuralbandit.sota import RandomBandit, BanditTron, LinUCB\n\ndataset = get_cov_dataset()\n\ncumulative_reward = 0\nT = int(2.5E6)\n\ngame = ContextualBanditGame(dataset, T)\n#player = RandomBandit(dataset.K)\n#player = LinUCB(dataset.K, dataset.D)\nplayer = NeuralBandit(dataset.K, dataset.D, layer_count = 1, layer_size = 64, gamma = 0.05)\n\nfor t in tqdm(range(T)):\n        context = game.get_context()\n        action = player.select(context)\n        reward = game.play(action)\n        \n        cumulative_reward += reward\n        \n        player.observe(action, context, reward)\n\ncumulative_regret = (T*game.optimal_accuracy - cumulative_reward)\nprint(cumulative_regret)\n```\n\n### Citations\n#### NeuralBandit\n```\n@InProceedings{10.1007/978-3-319-12637-1_47,\nauthor="Allesiardo, Robin\nand F{\\\'e}raud, Rapha{\\"e}l\nand Bouneffouf, Djallel",\neditor="Loo, Chu Kiong\nand Yap, Keem Siah\nand Wong, Kok Wai\nand Teoh, Andrew\nand Huang, Kaizhu",\ntitle="A Neural Networks Committee for the Contextual Bandit Problem",\nbooktitle="Neural Information Processing",\nyear="2014",\npublisher="Springer International Publishing",\naddress="Cham",\npages="374--381",\nabstract="This paper presents a new contextual bandit algorithm, NeuralBandit, which does not need hypothesis on stationarity of contexts and rewards. Several neural networks are trained to modelize the value of rewards knowing the context. Two variants, based on multi-experts approach, are proposed to choose online the parameters of multi-layer perceptrons. The proposed algorithms are successfully tested on a large dataset with and without stationarity of rewards.",\nisbn="978-3-319-12637-1"\n}\n```\n#### BanditForest\n```\n@InProceedings{pmlr-v51-feraud16,\n  title = \t {Random Forest for the Contextual Bandit Problem},\n  author = \t {Raphaël Féraud and Robin Allesiardo and Tanguy Urvoy and Fabrice Clérot},\n  booktitle = \t {Proceedings of the 19th International Conference on Artificial Intelligence and Statistics},\n  pages = \t {93--101},\n  year = \t {2016},\n  editor = \t {Arthur Gretton and Christian C. Robert},\n  volume = \t {51},\n  series = \t {Proceedings of Machine Learning Research},\n  address = \t {Cadiz, Spain},\n  month = \t {09--11 May},\n  publisher = \t {PMLR},\n  pdf = \t {http://proceedings.mlr.press/v51/feraud16.pdf},\n  url = \t {http://proceedings.mlr.press/v51/feraud16.html},\n  abstract = \t {To address the contextual bandit problem, we propose an online random forest algorithm. The analysis of the proposed algorithm is based on the sample complexity needed to find the optimal decision stump. Then, the decision stumps are recursively stacked in a random collection of decision trees, BANDIT FOREST. We show that the proposed algorithm is optimal up to logarithmic factors. The dependence of the sample complexity upon the number of contextual variables is logarithmic. The computational cost of the proposed algorithm with respect to the time horizon is linear. These analytical results allow the proposed algorithm to be efficient in real applications , where the number of events to process is huge, and where we expect that some contextual variables, chosen from a large set, have potentially non-linear dependencies with the rewards. In the experiments done to illustrate the theoretical analysis, BANDIT FOREST obtain promising results in comparison with state-of-the-art algorithms.}\n}\n\n```\n',
    'author': 'rallesiardo',
    'author_email': 'robin.allesiardo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rallesiardo/NeuralBandit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
