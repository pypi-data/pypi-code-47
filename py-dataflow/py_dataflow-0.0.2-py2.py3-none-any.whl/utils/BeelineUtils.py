import random
import os
import subprocess
import shlex


class BeelineUtils():

    def __init__(self):
        test  = "asd"

    def beelineExec(self, hql, queue = "default"):
        # server.bigdata.redecorp.br:2181
        # servers = ["localhost:10000",
                    # "localhost:10000"]
        servers = "192.168.99.100:10000"
        base = "default"
        queue = "default"
        # hql = "show tables;"
        # self.gerarListaRandom(servers)
        # --hiveconf mapreduce.job.queuename=broker
        beeline_cmd = """beeline -u \"jdbc:hive2://{servers}/{base} ?mapred.job.queue.name={queue};serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2\" \
                    --hiveconf tez.queue.name={base} \
                    --showheader=false \
                    --outputformat=tsv2 \
                    --silent=true \
                    -e \"{hql}\" """.format(servers=servers, base=base, queue=queue, hql=hql)

        # bl_out = os.system(beeline_cmd)
        process = subprocess.Popen(shlex.split(beeline_cmd),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                close_fds=True,
                shell=False)
        output = process.stdout.read() #.strip()
        out_clean = output.splitlines()[3:]
        return out_clean

    def gerarListaRandom(self, servers):
        #random zookeeper
        random.shuffle(servers)
        serverShuf = ",".join(servers)
        return serverShuf

    
