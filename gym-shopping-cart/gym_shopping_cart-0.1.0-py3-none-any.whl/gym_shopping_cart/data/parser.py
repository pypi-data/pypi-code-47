import logging
import tarfile
import time
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

LOGGER = logging.getLogger(__name__)


class InstacartData:
    RAW_N_PRODUCTS = 49383
    MAX_DAYS_SINCE_PRIOR = (
        30
    )  # From https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b
    N_OBSERVATIONS = 49416

    def __init__(self, gz_file: Path, max_products=None):
        self.directory = gz_file.parent / "instacart_2017_05_01"
        self.max_products = max_products
        if not self.directory.exists():
            LOGGER.info("Extracting data from {} to {}".format(gz_file, self.directory))
            with tarfile.open(gz_file, "r:gz") as tar:
                tar.extractall(path=gz_file.parent)

    def orders_for_user(self, id: np.uint32 = None) -> np.ndarray:
        raw = self._raw_orders_for_user(id)
        return self._format(raw)

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

    @staticmethod
    def _common_products(data: pd.DataFrame) -> pd.DataFrame:
        return (
            data[["product_id", "order_id"]]
            .groupby(by="product_id")
            .count()
            .sort_values(by="order_id", ascending=False)
            .reset_index()["product_id"]
        )

    @staticmethod
    def _filter_common_products(
        data: pd.DataFrame, max_products: int = None
    ) -> pd.DataFrame:
        s = InstacartData._common_products(data).head(max_products)
        return data[data["product_id"].isin(s)]

    def _format(self, data: pd.DataFrame) -> pd.DataFrame:
        LOGGER.info(
            "Formatting data with {} orders".format(len(data["order_number"].unique()))
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
            grouped, InstacartData.RAW_N_PRODUCTS, "product_id", zero_indexed=False
        )

        if self.max_products is not None:
            common_products = InstacartData._common_products(data).head(
                self.max_products
            )
            cols = encoded_products.columns[common_products.values.tolist()]
            encoded_products = encoded_products[cols]

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
        res = pd.concat(
            [encoded_products, encoded_dow, encoded_hod, encoded_days_since], axis=1
        )
        return res.sort_index()

    def _raw_orders_for_user(self, id: np.uint32 = None) -> pd.DataFrame:
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
        orders_df = orders_df[orders_df["eval_set"] == "prior"]

        if id is None:
            g = orders_df.groupby(by=["user_id"])["order_id"].count()
            g = g[g >= 50]
            large_user_ids = g.index
            id = np.random.choice(large_user_ids)
        LOGGER.info("Loading data for user {}".format(id))

        orders_df = orders_df[orders_df["user_id"] == id]
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))

        n_orders = len(orders_df.groupby(by="order_id"))
        if n_orders < 50:
            LOGGER.warning("This user only has {} orders".format(n_orders))

        LOGGER.info("Loading prior orders")
        start = time.process_time()
        order_products_prior_df = pd.read_csv(
            self.directory / "order_products__prior.csv",
            dtype={
                "order_id": np.uint32,
                "add_to_cart_order": np.uint8,
                "reordered": np.bool,
                "product_id": np.uint16,
            },
        )
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))

        LOGGER.info("Loading products")
        start = time.process_time()
        products_df = pd.read_csv(
            self.directory / "products.csv",
            dtype={
                "aisle_id": np.uint8,
                "department_id": np.uint8,
                "product_id": np.uint16,
                "product_name": np.str,
            },
        ).drop(["product_name"], axis=1)
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))

        LOGGER.info("Joining data")
        start = time.process_time()
        df_prior = pd.merge(
            orders_df, order_products_prior_df, how="left", on="order_id"
        )
        df_prior = pd.merge(df_prior, products_df, how="left", on="product_id")
        LOGGER.debug("Took {:0.2f} s".format(time.process_time() - start))
        return df_prior

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
        return self.orders_for_user().columns

    def n_products(self) -> int:
        if self.max_products is not None:
            return self.max_products
        else:
            return InstacartData.RAW_N_PRODUCTS
