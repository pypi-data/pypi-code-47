# -*- coding: utf-8 -*-
import re
import sys
import json
import yaml
import os
from os.path import basename, dirname, isfile
from pyspark.sql import Row, SparkSession




def getSparkSession(fonte = "default", queue = "default", qt_exec_master = "*"):
    resourceManager = "192.168.99.131:8088"
    # .config("spark.ui.port", "7077")\
    # .config("spark.driver.host", "localhost")\
    # 
    # .config("spark.scheduler.mode", "FIFO")\
    try:
        _spark = SparkSession.builder\
            .appName("billing1-" + fonte)\
            .config("spark.yarn.queue", queue)\
            .config("spark.master", "spark://192.168.99.131:7077")\
            .config("hive.metastore.uris", "thrift://192.168.99.127:9083")\
            .config("spark.shuffle.compress", "true")\
            .config("spark.sql.warehouse.dir", "/user/hive/warehouse")\
            .config("spark.driver.bindAddress", "localhost")\
            .config("spark.shuffle.service.enabled", "true")\
            .config("spark.ui.port", "7077")\
            .config("spark.hadoop.yarn.resourcemanager.webapp.address", resourceManager)\
            .config("spark.shuffle.service.port","7337")\
            .config("spark.executor.cores", "1")\
            .config("spark.dynamicAllocation.maxExecutors", "12")\
            .config("spark.executor.memory", "1G")\
            .config("spark.driver.memory", "5G")\
            .config("spark.executor.instances", "5")\
            .config("tez.queue.name", queue)\
            .config("spark.sql.broadcastTimeout", "36000")\
            .config("spark.eventLog.enabled", "false")\
            .config("hive.exec.dynamic.partition.mode", "nonstrict")\
            .config("hive.exec.max.dynamic.partitions", "1500")\
            .config("spark.dynamicAllocation.enabled", "false")\
            .config("spark.dynamicAllocation.initialExecutors", "2")\
            .config("spark.sql.catalogImplementation", "hive")\
            .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")\
            .config("spark.speculation", "false")\
            .enableHiveSupport()\
            .getOrCreate()
        return _spark

    except Exception as e:
        print(e)


spark = getSparkSession()
spark.sql("show databases").show()

import pyrebase
import os, json
from datetime import datetime
config = {"apiKey": os.environ.get('API_KEY_FIREBASE'),
        "authDomain": os.environ.get('AUTH_DOMAIN_FIREBASE'),
        "databaseURL": os.environ.get('DATA_BASE_URL_FIREBASE'),
        "storageBucket": os.environ.get('STORAGE_BUCKET_FIREBASE')
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
day = datetime.today().strftime('%Y%m%d')
trade_day = db.child("invest").child(day).get().val()
js = json.dumps(trade_day)
context = spark.sparkContext.parallelize(js)
spark.read.json(context)