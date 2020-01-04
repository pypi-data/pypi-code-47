import pandas as pd
import psycopg2 as pg2

conn = pg2.connect(
    dbname = "django_finance", 
    user = "postgres", 
    password = "pass",
    host = '127.0.0.1',
    port = '5432',
)

file_path = r"C:/Users/Roberts/Downloads/Budget Tracker 2019.xlsx"

workbook = pd.read_excel(file_path, usecols="A:D", sheet_name=None)

category_list = []

for sheet_name in workbook:
    if sheet_name == "June 2019":
        break

    df = workbook[sheet_name].dropna()
    print(sheet_name.upper())
    
    with open(f'{sheet_name}.csv', 'a+') as f:
        for row in df.itertuples():
            row = list(row)
            if row[2][-1] == ":":
                row[2] = row[2][:-1]

            

            category_list.append(row[2])

    # print(df.groupby(["Category:"]).sum())
    print("\n")
    
print(set(category_list))

conn.close()
