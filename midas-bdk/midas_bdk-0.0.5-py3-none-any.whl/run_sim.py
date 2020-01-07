from midasbdk.simulator.sim import Simulator
from midasbdk.midas.Stock.VDaishinTrader import VDaishinTrader
from midasbdk.brains.brain import Brain

import sys, os
import inspect
import argparse

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import importlib

parser = argparse.ArgumentParser()
parser.add_argument('-a', type=str, required=True, help='algorithm name')

args = parser.parse_args()

algo_name = args.a

BRAIN_REPO = 'mybrains'

module_name = '{}.{}'.format(BRAIN_REPO, algo_name)
module = importlib.import_module(module_name)
for name, clas in inspect.getmembers(module):
    if inspect.isclass(clas):
        if issubclass(clas, Brain) and clas != Brain:  # Check if 2 classes
            break

# STOCK
trader = VDaishinTrader()
sim = Simulator()
inst = clas(trader,1)
sim.registerBrain(inst, 1.0)
sim.run()

