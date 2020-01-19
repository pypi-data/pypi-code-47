import sys
import os
import uuid

broker_path = os.environ.get("PROJECT_BROKER")
sys.path.append(broker_path)
from utils import BeelineUtils, Config, Logger, date


class StockBeeline(object):
    stock = {}

    def __init__(self, *args, **kwargs):
        # self.bl = BeelineUtils.__init__(self)
        Config.__init__(self)
        Logger.__init__(self)
        self.stock = self.conf["control"]["broker"].get("winfut")

    def saveBroker(self, stock = {}):
        bl = BeelineUtils()
        # try:
        # import ipdb; ipdb.set_trace()
        job = self.stock.copy()
        job.update({
            "id": str(uuid.uuid1()),            # Id unico de execucao do job
            "job_type": "alerts",               # Identificador do script
            "job_name": "alerts-send",          # Identificador do alerta
            "job_status": "STARTED",            # Marca job como iniciado
            "message": "",                      # Marca job como iniciado
            "start_time": date.now(),           # Momento de inicio
            "finish_time": "",                  # Momento de finalizacao
            "price": stock.get("price"),
            "dt_foto": date.now()               # Particao = dia atual
        })
        hql_update = self.updateBroker(**job)
        bl.beelineExec(hql=hql_update)
        # except:
        #     hql_create = self.createTableBroker()
        #     bl.beelineExec(hql=hql_create)

    def updateBroker(self, **job):
        # INSERT INTO {control[database]}.{control[table]}
        query_broker = """
            INSERT INTO broker.WINFUT_MINUTE
            PARTITION(dt_foto='{dt_foto}')
            SELECT
                '{id}' AS id,
                '{job_type}' AS job_type,
                '{job_name}' AS job_name,
                '{job_status}' AS status,
                '{message}' AS message,
                '{start_time}' AS start_time,
                '{finish_time}' AS finish_time,
                '{price}' AS price
            FROM (SELECT 1) AS dual;
            """.strip().replace("\n", "").format(**job)
        return query_broker

    def createTableBroker(self):
        # CREATE TABLE IF NOT EXISTS `${hiveconf:tez.task.database_name}.WINFUT_MINUTE`(
        query_broker = """
            CREATE TABLE IF NOT EXISTS `broker.WINFUT_MINUTE`(
                id STRING COMMENT 'Identificador unico de execucao - gerenciado pela aplicacao',
                job_type STRING COMMENT 'Tipo de job - kpi, forecast, alert',
                job_name STRING COMMENT 'Nome do job - ALT-0001, KPI-CICLO-FATURAMENTO, etc.',
                status STRING COMMENT 'Status de execucao do job - STARTED, FINISHED or ERROR',
                message STRING COMMENT 'Mensagem gerada em caso de erro',
                start_time TIMESTAMP COMMENT 'Momento de inicio',
                finish_time TIMESTAMP COMMENT 'Momento de finalizacao',
                price STRING COMMENT 'Ultimo Price'
            )
            COMMENT 'Controle de execucoes dos job. Todos os jobs processados devem possuir pelo menos duas entradas nesta tabela. Uma de inicio e outra de fim'
            PARTITIONED BY (dt_foto STRING COMMENT 'Dia de processamento - formato AAAA-MM-DD')
            STORED AS ORC
            TBLPROPERTIES (
                'orc.compress'='SNAPPY');
            """.strip().replace("\n", "")
        return query_broker



