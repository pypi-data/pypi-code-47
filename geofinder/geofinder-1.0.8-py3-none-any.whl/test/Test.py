import os
from pathlib import Path

import Geodata

# Load test data
directory = os.path.join(str(Path.home()), "Documents")
directory = os.path.join(directory, "geoname_data")

cache_directory = os.path.join(directory, 'cache')
geodata = Geodata.Geodata(directory_name=directory, progress_bar=None, enable_spell_checker = True)
error: bool = geodata.read()
if error:
    print("Missing geodata support Files.")
    raise ValueError('Cannot open database')

# Read in Geoname Gazeteer file - city names, lat/long, etc.
print("loading data")
error = geodata.open()

if error:
    print("Missing geoname Files.")
    print('Requires ca.txt, gb.txt, de.txt from geonames.org in folder username/geoname_test')
    raise ValueError('Missing ca.txt, gb.txt, de.txt from geonames.org')
print("initialized")

for item in ['gothland', 'matemoutier ']:
    res = geodata.geo_files.spellcheck.lookup(item)
    print(f'==={item}')
    print (res)
