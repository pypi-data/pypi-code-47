import requests

fields = {
    'token': '83388E9616D81747C28A748A0C281DBC',
    'content': 'metadata',
    'format': 'xml'
}


r = requests.post('https://redcap.sun.ac.za/api/', data=list(fields.items()))

data = r.content

with open("record.xml", "wb") as f:
    f.write(data)

from lxml import etree
root = etree.fromstring(data)


"""
import pandas as pd
df = pd.DataFrame(data)
df.to_csv("record.csv")
"""
