from eor import *
import pandas as pd

edin_df = pd.read_csv('eor.csv')
edin_df = edin_df.drop(['selected'], axis=1)
edin_df.head(10)

exxon_eor_df, screening_table_df, field_data_df = exxon_eor(edin_df)
print(exxon_eor_df.head(10))
print(screening_table_df.head(10))
print(field_data_df.head(10))
# exxon_eor_df.to_csv("exxon_eor_df.csv")

uom_eor_df, screening_table_2019_df, p_value_2019_df, field_data_2019_df = uom_eor(edin_df)
print(uom_eor_df.head(10))
print(screening_table_2019_df.head(10))
print(p_value_2019_df.head(10))
print(field_data_2019_df.head(10))
# uom_eor_df.to_csv("uom_eor_df.csv")