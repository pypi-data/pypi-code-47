#! /usr/bin/env python3

from pywand.wandreader import WandInputReader

if __name__ == '__main__':
    reader = WandInputReader()

    for i in reader.get_codes():
        print(i['wand'])
