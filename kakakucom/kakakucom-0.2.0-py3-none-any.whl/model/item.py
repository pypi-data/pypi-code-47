from dataclasses import dataclass, field
from pyspark.sql import SparkSession, DataFrame
from pyspark import SparkContext
from catscore.db.mysql import MySQLConf

@dataclass(frozen=True)
class Item:
    id: str
    name: str
    url: str
    img_src: str
    category: str
    
class RankedItemTable:
    _table_name = "kakakucom_ranked_item"
    
    @property
    @classmethod
    def table_name(cls):
        return cls._table_name
    
    @classmethod
    def from_local_as_df(cls, spark:SparkSession, input_path:str):
        """
        """
        input_path = f"{input_path}/*.csv"
        print(f"RankedItemTable: input path is {input_path}")
        df = spark.read.option("header", "true").csv(input_path).drop("_c0")
        return df
    
    @classmethod
    def overwrite_table(cls, spark:SparkSession, df:DataFrame, mysql_conf:MySQLConf):
        df.write.jdbc(mysql_conf.connection_uri, table=cls._table_name, mode='overwrite')

@dataclass(frozen=True)
class RankedItem:
    item_id: str
    ranking_url: str
    item_name: str
    item_img_src: str
    item_maker: str
    item_category: str
    item_rank: int
    rank_category: str
    rank_gathered_date: str
    item_url: str
    item_min_price: str
    item_review_rate: str
    item_bbs_num: str
    update_date: str