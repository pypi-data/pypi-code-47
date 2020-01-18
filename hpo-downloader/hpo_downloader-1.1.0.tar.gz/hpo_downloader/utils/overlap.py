import warnings
import pandas as pd


def overlap(df1: pd.DataFrame, df1_name: str, df2: pd.DataFrame, df2_name: str, key: str):
    df1_unique = df1[key].unique()
    miss = len(set(df1_unique) - set(df2[key].unique()))
    percentage = miss/df1_unique.shape[0]
    if miss:
        warnings.warn("Given index {key} is not matched for {miss} times ({percentage:.2%}) between {df1_name} and {df2_name}.".format(
            key=key,
            miss=miss,
            percentage=percentage,
            df1_name=df1_name,
            df2_name=df2_name
        ))
