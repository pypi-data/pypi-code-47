import logging
import tarfile
import time
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

directory = Path("data/instacart_2017_05_01")

orders_df = pd.read_csv(directory / "orders.csv")
orders_df = orders_df[orders_df["user_id"] == 129182]
orders_df.to_csv("data/orders.csv", index=False)


def filter_dataframes(data_df: pd.DataFrame, in_df: pd.DataFrame, key: str):
    return data_df[data_df[key].isin(in_df[key])]


def load_and_save(filename: str, filter_df: pd.DataFrame, filter_key: str):
    df = pd.read_csv(directory / filename)
    df = filter_dataframes(df, filter_df, filter_key)
    df.to_csv(Path("data") / filename, index=False)
    return df


prior_df = load_and_save("order_products__prior.csv", orders_df, "order_id")
products_df = load_and_save("products.csv", prior_df, "product_id")
department_df = load_and_save("departments.csv", products_df, "department_id")
aisles_df = load_and_save("aisles.csv", products_df, "aisle_id")
