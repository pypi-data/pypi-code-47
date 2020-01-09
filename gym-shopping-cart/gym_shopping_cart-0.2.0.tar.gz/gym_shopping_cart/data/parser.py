import logging
import tarfile
import time
from pathlib import Path
from typing import List
from functools import lru_cache

import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class InstacartData:
    RAW_N_PRODUCTS = 50000
    MAX_DAYS_SINCE_PRIOR = (
        30
    )  # From https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b
    RAW_N_OBSERVATIONS = 32

    def __init__(self, gz_file: Path, max_products=None, cache_data=True):
        self.cache_data = cache_data
        if self.cache_data:
            LOGGER.info("Caching data in memory")
        self.directory = gz_file.parent / "instacart_2017_05_01"
        self.max_products = max_products
        if self.directory.exists():
            LOGGER.warning("Overwriting {}".format(self.directory))
        LOGGER.info("Extracting data from {} to {}".format(gz_file, self.directory))
        with tarfile.open(gz_file, "r:gz") as tar:
            tar.extractall(path=gz_file.parent)

    def orders_for_user(self, id: np.uint32 = None) -> np.ndarray:
        raw = self._raw_orders_for_user(id)
        return self._format_orders(raw), self._format_purchases(raw)

    @staticmethod
    def _encode(
        grouped: pd.DataFrame, n_classes: int, key: str, zero_indexed: bool = False
    ) -> pd.DataFrame:
        # If not zero-indexed then add an extra buffer column to make indexing easier.
        if zero_indexed:
            encoded = np.zeros((len(grouped), n_classes))
        else:
            encoded = np.zeros((len(grouped), n_classes + 1))
        for i, p in enumerate(grouped[key].apply(np.array)):
            if zero_indexed:
                encoded[i, p.astype(int) - 1] = 1
            else:
                encoded[i, p.astype(int)] = 1
        return pd.DataFrame(data=encoded, index=grouped.size().index).add_prefix(
            key + "_"
        )

    @lru_cache(maxsize=None)
    def _common_products(self) -> pd.DataFrame:
        return (
            (
                self._prior_products()[["product_id", "order_id"]]
                .groupby(by="product_id")
                .count()
                .sort_values(by="order_id", ascending=False)
                .reset_index()["product_id"]
            )
            .head(self.max_products)
            .values
        )

    def _format_purchases(self, data: pd.DataFrame) -> pd.DataFrame:
        LOGGER.info(
            "Formatting purchaces with {} orders".format(
                len(data["order_number"].unique())
            )
        )

        grouped = data[
            [
                "order_number",
                "order_dow",
                "order_hour_of_day",
                "days_since_prior_order",
                "product_id",
            ]
        ].groupby("order_number")

        # One-hot encode product numbers for each order
        encoded_products = InstacartData._encode(
            grouped, self.RAW_N_PRODUCTS, "product_id", zero_indexed=False
        )

        # Remove all but the most popular products
        if self.max_products is not None:
            LOGGER.info(
                "Returning the {} most common products".format(self.max_products)
            )
            encoded_products = encoded_products[
                encoded_products.columns[self._common_products()]
            ]

        return encoded_products.sort_index()

    def _format_orders(self, data: pd.DataFrame) -> pd.DataFrame:
        LOGGER.info(
            "Formatting orders with {} orders".format(
                len(data["order_number"].unique())
            )
        )

        grouped = data[
            [
                "order_number",
                "order_dow",
                "order_hour_of_day",
                "days_since_prior_order",
                "product_id",
            ]
        ].groupby("order_number")

        # One-hot encode days of the week
        encoded_dow = InstacartData._encode(grouped, 7, "order_dow", zero_indexed=True)

        # One-hot encode hours of the day
        encoded_hod = InstacartData._encode(
            grouped, 24, "order_hour_of_day", zero_indexed=True
        )

        # Normalise days since prior order
        encoded_days_since = (
            data[["order_number", "days_since_prior_order"]]
            .drop_duplicates()
            .set_index("order_number")
        ) / InstacartData.MAX_DAYS_SINCE_PRIOR

        # Merge other features with product encoding
        res = pd.concat([encoded_dow, encoded_hod, encoded_days_since], axis=1)
        res = res.fillna(0)
        return res.sort_index()

    @lru_cache(maxsize=None)
    def _orders(self) -> pd.DataFrame:
        LOGGER.info("Loading order data")
        start = time.process_time()
        orders_df = pd.read_csv(
            self.directory / "orders.csv",
            dtype={
                "order_dow": np.uint8,
                "order_hour_of_day": np.uint8,
                "order_number": np.uint8,
                "order_id": np.uint32,
                "user_id": np.uint32,
                "days_since_prior_order": np.float16,
                "eval_set": np.str,
            },
        )
        # Remove all data that is not in the "prior" dataset
        orders_df = orders_df[orders_df["eval_set"] == "prior"]

        # Remove users with small numbers of orders (to reduce data size)
        orders_df = orders_df[
            orders_df["user_id"].map(orders_df["user_id"].value_counts()) >= 50
        ]
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))
        return orders_df

    @lru_cache(maxsize=None)
    def _prior_products(self) -> pd.DataFrame:
        LOGGER.info("Loading prior orders")
        start = time.process_time()
        prior_products = pd.read_csv(
            self.directory / "order_products__prior.csv",
            dtype={
                "order_id": np.uint32,
                "add_to_cart_order": np.uint8,
                "reordered": np.bool,
                "product_id": np.uint16,
            },
        )
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))
        return prior_products

    @lru_cache(maxsize=None)
    def _products(self) -> pd.DataFrame:
        LOGGER.info("Loading products")
        start = time.process_time()
        products = pd.read_csv(
            self.directory / "products.csv",
            dtype={
                "aisle_id": np.uint8,
                "department_id": np.uint8,
                "product_id": np.uint16,
                "product_name": np.str,
            },
        ).drop(["product_name"], axis=1)
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))
        return products

    @lru_cache(maxsize=None)
    def _merged_data(self) -> pd.DataFrame:
        prior_products_df = self._prior_products()
        orders_df = self._orders()

        LOGGER.info("Joining data")
        start = time.process_time()
        df_prior = pd.merge(orders_df, prior_products_df, how="left", on="order_id")
        df_prior = pd.merge(df_prior, self._products(), how="left", on="product_id")
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))
        return df_prior

    def _raw_orders_for_user(self, id: np.uint32 = None) -> pd.DataFrame:
        data = self._merged_data()

        if not self.cache_data:
            self._orders.cache_clear()
            self._prior_products.cache_clear()
            self._products.cache_clear()
            self._merged_data.cache_clear()

        if id is None:
            g = data.groupby(by=["user_id"])["order_id"].count()
            id = np.random.choice(g.index)
        LOGGER.info("Loading data for user {}".format(id))
        # df_prior = df_prior[df_prior["user_id"] == id]
        return data[data["user_id"] == id]

    def product_str(self, id: int) -> str:
        df = pd.read_csv(
            self.directory / "products.csv",
            dtype={
                "aisle_id": np.uint8,
                "department_id": np.uint8,
                "product_id": np.uint16,
                "product_name": np.str,
            },
            index_col="product_id",
        ).drop(["aisle_id", "department_id"], axis=1)
        if id in df.index:
            return df.loc[id][0].strip()
        else:
            raise ValueError("Unknown product id")

    def columns(self) -> List[str]:
        _, purchases = self.orders_for_user()
        return purchases.columns

    def n_products(self) -> int:
        if self.max_products is None:
            return InstacartData.RAW_N_PRODUCTS + 1  # Because of non-zero indexing
        else:
            return self.max_products

    def n_observations(self) -> int:
        return InstacartData.RAW_N_OBSERVATIONS
