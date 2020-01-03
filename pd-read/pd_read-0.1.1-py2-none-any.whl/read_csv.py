import pandas as pd
import numpy as np
from .base_class import BaseClass

class ReadCSV(BaseClass):
    def __init__(self, file_path):
        self.file_name = file_path
        # need to check valid extension
        self.df = pd.read_csv(self.file_name)
        return

    def get_data(self, columns=[], rows=None):
        if columns:
            data = self.df[columns]
        else:
            data = self.df

        if rows:
            data = data.head(rows)
        return data

    def set_df_data(self):
        pass

    def make_df(self, object_var):
        return pd.DataFrame(object_var)

