#!/usr/bin/env python3
#
#

import os
import sys
import os.path

def j(*args):
    if not args: return
    todo = list(map(str, filter(None, args)))
    return os.path.join(*todo)

if sys.version_info.major < 3:
    print("you need to run koning with python3")
    os._exit(1)

try:
    use_setuptools()
except:
    pass

try:
    from setuptools import setup
except Exception as ex:
    print(str(ex))
    os._exit(1)

target = "koning"
upload = []

def uploadfiles(dir):
    upl = []
    if not os.path.isdir(dir):
        print("%s does not exist" % dir)
        os._exit(1)
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if not os.path.isdir(d):
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl

def uploadlist(dir):
    upl = []

    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)

    return upl

with open('README') as file:
    long_description = file.read()

setup(
    name='koning',
    version='38',
    url='https://bitbucket.org/bthate/koning',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="de koning bekent schuld aan genocide.",
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    install_requires=["botd"],
    scripts=["bin/koning"],
    packages=['koning', ],
    long_description="""De Koning is op de hoogte (zie http://koning.rtfd.io) dat de medicijnen toegedient met behulp van de nog in te voeren wetten gif zijn en dus moet hij ook weten dat met het in werking laten treden van deze wetten h
Natuurlijk dient er voor het volksbelang direct opgetreden te worden (zie http://president.rtfd.io) , mischien voor de opvolger van deze minister president die schuldig is aan straffeloosheids zekeringen (zie http
Ondertussen is er al aangifte tegen de koning gedaan voor zijn genocide (zie http://genocide.rtfd.io).

BRIEF
=====

| Bart Thate
| Raadhuisplein 53
| 1701 EH Heerhugowaard

| Z.M. Koning Willem-Alexander
| Paleis Noordeinde
| Postbus 30412
| 2500 GK Den Haag

Heerhugowaard, 20-09-2018

Betreft: bewijs dat antipsychotica gif zijn

Geachte Majesteit,

er is bewijs dat medicijnen (antipsychotica) gebruikt in de GGZ gif zijn:

    1. olanzapine (zyprexa) - https://echa.europa.eu/substance-information/-/substanceinfo/100.125.320 
    2. clozapine (leponex) - https://echa.europa.eu/substance-information/-/substanceinfo/100.024.831 
    3. aripriprazole (abilify) https://echa.europa.eu/substance-information/-/substanceinfo/100.112.532 

op 6-2-2019 geedit naar niet schadelijk:

    4. haloperiodol (haldol) - https://echa.europa.eu/substance-information/-/substanceinfo/100.000.142 

De Eerste Kamer heeft wetten aangenomen (de Wet Zorg en Dwang, Wet verplichte Geestelijke Gezondheid Zorg, Wet Forensische Zorg) die een wettelijk voorschrift voor het toedienen van medicatie voorzien, het betreft

Ik hoop dat u de wetenschap dat het hier gif betreft zult gebruiken om deze wetten niet in werking te laten treden.

Hoogachtend,

Bart Thate

""",
    long_description_content_type='text/markdown',
    data_files=[("docs", ["docs/conf.py","docs/index.rst"]),
               (j('docs', 'jpg'), uploadlist(os.path.join("docs","jpg"))),
               (j('docs', 'txt'), uploadlist(os.path.join("docs", "txt"))),
               (j('docs', '_templates'), uploadlist(os.path.join("docs", "_templates")))
              ],
    package_data={'': ["*.crt"],
                 },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
