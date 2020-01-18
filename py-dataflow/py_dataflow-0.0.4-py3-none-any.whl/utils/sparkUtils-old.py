
from pyspark.sql import Row, SparkSession


def getSparkSession(fonte = "default", queue = "faturamento", qt_exec_master = "*"):

    import os
    os.system("rm -R /opt/spark-2.3.0/metastore_db")

    fonte = "default" 
    queue = "default"
    # resourceManager = "brtlvlts0077co.redecorp.br:8088"
    # resourceManager = "localhost:8088"
    resourceManager = "192.168.99.100:8088"

    _spark = SparkSession.builder\
        .appName("fatura" + fonte)\
        .enableHiveSupport()\
        .getOrCreate()

    return _spark


# def getSparkSession(fonte = "default", queue = "faturamento", qt_exec_master = "*"):

#     fonte = "default" 
#     queue = "default"
#     # resourceManager = "brtlvlts0077co.redecorp.br:8088"
#     # resourceManager = "localhost:8088"
#     resourceManager = "192.168.99.100:8088"

#     _spark = SparkSession.builder\
#         .appName("fatura" + fonte)\
#         .config("spark.master", "yarn")\
#         .config("spark.yarn.queue", queue)\
#         .config("spark.shuffle.service.enabled", "true")\
#         .config("spark.sql.catalogImplementation", "hive")\
#         .config("spark.shuffle.compress", "true")\
#         .config("spark.shuffle.service.port","7337")\
#         .config("spark.executor.cores", "2")\
#         .config("spark.executor.memory", "2G")\
#         .config("spark.yarn.executor.memoryOverhead", "1000")\
#         .config("spark.driver.memory", "2G")\
#         .config("spark.yarn.driver.memoryOverhead", "1000")\
#         .config("spark.scheduler.mode", "FIFO")\
#         .config("spark.ui.port", "4066")\
#         .config("spark.dynamicAllocation.enabled", "true")\
#         .config("spark.hadoop.yarn.resourcemanager.webapp.address", resourceManager)\
#         .config("yarn.scheduler.maximum-allocation-mb", "2G")\
#         .config("spark.sql.broadcastTimeout", "36000")\
#         .config("spark.eventLog.enabled", "false")\
#         .enableHiveSupport()\
#         .getOrCreate()

#     #old 
#     # .config("spark.executor.extraJavaOptions", "-XX:+PrintGCDetails -XX:+PrintGCTimeStamps")\
#     # .config("spark.driver.extraJavaOptions", "-XX:+UseG1GC -Dhdp.version=2.6.4.0-91 -XX:ConcGCThreads=4")\
#     # .config("spark.executor.extraJavaOptions", "-XX:+UseG1GC -Dhdp.version=2.6.4.0-91 -XX:ConcGCThreads=4")\

#     return _spark


#'spark.executor.extraJavaOptions=-XX:+UseParallelGC -XX:ParallelGCThreads=16' \
# Spark SQL
#'/usr/hdp/current/spark2-client/bin/spark-sql' \
# '--master' \
# 'yarn'
# '--conf' \
# 'spark.app.name=spark-sql' \
# '--conf' \
# 'spark.task.maxFailures=12' \
# '--conf' \
# 'spark.sql.codegen=true' \
# '--conf' \
# 'spark.executor.extraJavaOptions=-XX:+UseG1GC -XX:ParallelGCThreads=16' \
# '--conf' \
# 'spark.dynamicAllocation.executorIdleTimeout=60s' \
# '--conf' \
# 'spark.dynamicAllocation.minExecutors=3' \
# '--conf' \
# 'spark.executor.memory=12g' \
# '--conf' \
# 'spark.kryoserializer.buffer.max=2000m' \
# '--conf' \
# 'spark.dynamicAllocation.initialExecutors=3' \
# '--conf' \
# 'spark.sql.tungsten.enabled=true' \
# '--conf' \
# 'spark.driver.maxResultSize=15g' \
# '--conf' \
# 'spark.executor.cores=10' \
# '--conf' \
# 'spark.ui.port=5100' \
# '--conf' \
# 'spark.streaming.backpressure.enabled=true' \
# '--conf' \
# 'spark.driver.memory=18g' \
# '--conf' \
# 'spark.network.timeout=300' \
# '--conf' \
# 'spark.dynamicAllocation.schedulerBacklogTimeout=1s' \
# '--conf' \
# 'spark.executor.instances=3' \
# '--conf' \
# 'spark.speculation=true' \
# '--conf' \
# 'spark.shuffle.service.enabled=true' \
# '--conf' \
# 'spark.sql.unsafe.enabled=true' \
# '--conf' \
# 'spark.executor.heartbeatInterval=60006' \
# '--conf' \
# 'spark.dynamicAllocation.enabled=true' \
# '--conf' \
# 'spark.yarn.queue=faturamento' \
# '--conf' \
# 'spark.yarn.driver.memoryOverhead=3000' \
# '--conf' \
# 'spark.sql.orc.filterPushdown=true' \
# '--conf' \
# 'spark.kryoserializer.buffer=64k' \
# '--conf' \
# 'spark.yarn.am.waitTime=10' \
# '--conf' \
# 'spark.dynamicAllocation.cachedExecutorIdleTimeout=120s' \
# '--conf' \
# 'spark.dynamicAllocation.sustainedSchedulerBacklogTimeout=1s' \
# '--conf' \
# 'spark.yarn.scheduler.heartbeat.interval-ms=2000' \
# '--conf' \
# #'spark.dynamicAllocation.maxExecutors=250' \
# '--conf' \
# 'spark.yarn.containerLauncherMaxThreads=25' \
# '--conf' \
# 'spark.serializer=org.apache.spark.serializer.KryoSerializer' \
# '--conf' \
# 'spark.yarn.am.memoryOverhead=1843' \
# '--conf' \
# 'spark.yarn.executor.memoryOverhead=3000' $@

