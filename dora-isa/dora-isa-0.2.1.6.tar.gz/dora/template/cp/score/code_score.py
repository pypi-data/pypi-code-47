from pyspark import SparkContext
sc = SparkContext()
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
sc.setLogLevel("ERROR")
from pyspark.sql import HiveContext
spark = HiveContext(sc)
sc._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.s3a.impl","org.apache.hadoop.fs.s3a.S3A")

from dora.isa import ISAContext
from dora.isa import ISAMagic
from dora.ml import MLContext
from dora.ml import MLMagic
from dora.interface.Interfaces import Interfaces

dora = ISAContext(sqlContext)
ISAMagic(dora)
ml = MLContext(Interfaces.JUPYTER, variable="ml")
MLMagic(ml)
asql = ISAContext(sqlContext)
ISAMagic(asql)


