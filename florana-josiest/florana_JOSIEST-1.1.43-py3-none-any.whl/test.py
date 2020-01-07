import extract
import itertools
from collections import OrderedDict

def main():
    fn = 'Calystegia05f_map.pdf'
    text = extract.load_treatment(fn)
    genus = extract.genus_in(text)

    #name_gens = [extract.keys_in(subgroup, genus)
    #             for subgroup in extract.subgroups(text)]
    #names = sorted(itertools.chain(*name_gens),
    #               key=lambda s: int(s.split('.')[0]))
    #names = OrderedDict.fromkeys(names).keys()
    #print('\n'.join(name.strip() for name in names))

    for block, name in extract.partition(text, genus):
        if 'macrostegia' in name and 'intermedia' in name:
            print(', '.join(extract.locs_in(block)))
            #print('Found block; first line:')
            #print(block.split('\n')[0])

if __name__ == '__main__':
    main()
