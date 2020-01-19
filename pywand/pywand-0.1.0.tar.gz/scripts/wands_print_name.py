#! /usr/bin/env python3

from pywand.wandreader import WandInputReader
from pywand.wandid import WandId

if __name__ == '__main__':
    reader = WandInputReader()
    wands = WandId()

    for i in reader.get_codes():
        print(wands.best_wand_match(i['wand']))
