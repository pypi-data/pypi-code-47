import pandas as pd
from tqdm.auto import tqdm


def non_unique_mapping(df1: pd.DataFrame, df2: pd.DataFrame, key: str) -> pd.DataFrame:
    """Return dataframe containing non_unique mapping on given key from given dataframes."""
    df2 = df2[df2[key].isin(df1[key].unique())]
    df1 = df1[df1[key].isin(df2[key].unique())]
    return pd.DataFrame([
        {
            **df1_row.to_dict(),
            **df2_row.to_dict()
        }
        for _, df1_row in tqdm(
            df1.iterrows(),
            total=df1.shape[0],
            leave=False,
            dynamic_ncols=True,
            desc="Mapping dataframes"
        )
        for _, df2_row in df2[df2[key] == df1_row[key]].iterrows()
    ])
