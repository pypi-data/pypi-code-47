import json
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

with open(f"{DIR_PATH}/tarot_spreads.json") as f:
    tarot_spreads = json.load(f)  # type: dict

with open(f"{DIR_PATH}/tarot_data.json") as f:
    tarot_data = json.load(f)  # type: dict

with open(f"{DIR_PATH}/tarot_skins.json") as f:
    tarot_skins = json.load(f)  # type: dict
