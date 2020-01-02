#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:35:05 2019

@author: descentis
"""

from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
sparql.setQuery("""
SELECT ?sitelink ?itemLabel  WHERE {
    ?sitelink schema:about ?item;
    wikibase:badge wd:Q17437796. # Sitelink is badged as a Featured Article  
    ?sitelink schema:isPartOf <https://en.wikipedia.org/>.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" } .
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

names = []
for item in results['results']['bindings']:
    names.append({
        'Site Link': item['sitelink']['value'],
        'Label': item['itemLabel']['value']})

df = pd.DataFrame(names)
print(len(df))
df
