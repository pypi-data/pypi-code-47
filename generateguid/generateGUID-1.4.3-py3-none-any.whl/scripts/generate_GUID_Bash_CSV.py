#!/usr/bin/python
import sys
from generateGUID import generate_GUID
import pandas as pd

if len(sys.argv) > 1:

    if len(sys.argv) == 2:
        file = sys.argv[1]
        df = pd.read_csv(file, usecols=["subject_name", "Study_ID"])
        print(df)

        for index, row in df.iterrows():
            key = row['subject_name']+row['Study_ID']
            print(generate_GUID(key))

    else:
        print("mauvais nombre d'arguments")
