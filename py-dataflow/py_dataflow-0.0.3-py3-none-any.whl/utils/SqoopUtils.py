import os
import subprocess
import shlex


class SqoopUtils():

    # def __init__(self):
    #     config  = {}

    def sqoopExec(self, hql, hcatalogDatabase, hcatalogTable, queue = "default"):
        sqoop_cmd = """nohup sqoop import \\
            -D mapred.child.java.opts="-Djava.security.egd=file:/dev/../dev/urandom" \\
            "-Dorg.apache.sqoop.splitter.allow_text_splitter=true" \\
            -Dmapreduce.job.queuename={queue} \\
            --connect jdbc:oracle:thin:DRECA/Dreca@10.238.36.76:1521:GRECPR1 \\
            --username DRECA \\
            --password Dreca \\
            --query {hql} \\
            --hcatalog-database {hcatalogDatabase} \\
            --hcatalog-table {hcatalogTable} \\
            --hive-overwrite \\
            --split-by SBSCRP_ID
        """.format(hcatalogDatabase=hcatalogDatabase, hcatalogTable=hcatalogTable, queue=queue, hql=hql)

        try:
            # sqoop_out = os.system(sqoop_cmd)
            process = subprocess.Popen(shlex.split(sqoop_cmd),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    close_fds=True,
                    shell=False)
            sqoop_out = process.stdout.read() #.strip()
        except:
            return sqoop_cmd
        return sqoop_out