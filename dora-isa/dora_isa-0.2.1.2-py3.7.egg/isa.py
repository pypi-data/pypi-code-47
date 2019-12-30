"""
Projeto ISA
"""
import datetime
import logging
import json
import re
import os
from time import sleep 
import hashlib
import pymysql
import sqlparse 
import boto3
from pyspark.sql import Row
from pyspark.sql.utils import AnalysisException
from pyspark.sql.utils import ParseException
from IPython.core import magic_arguments 
from IPython.core.magic import Magics 
from delta.tables import DeltaTable 

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(getattr(logging, os.environ.get('LOG_LEVEL','INFO')))
AWS_REGION    = os.environ.get('AWS_DEFAULT_REGION') 
CACHE_DB      = os.environ.get('CACHE_DB') 
DELTA_DB      = os.environ.get('DELTA_DB') 
DORA_BUCKET   = os.environ.get('DORA_BUCKET') 
DORA_USER     = os.environ.get('DORA_USER') 
INSTANCE_TYPE = os.environ.get('INSTANCE_TYPE','P') 
DORA_STORAGE  = os.environ.get('DORA_STORAGE')
class ISAContext: 
    """ 
    Contextualiza as consultas a serem executadas 
    """ 
    r_date=r"""'([0-9]{4}-[0-9]{2}-[0-9]{2})'""" 
    r_user_connections = r"""^show[\s]*connections$"""
    r_cache_tables = r"""^show[\s]*cache$"""
    r_version=r"""'[0-9]{1,}'""" 
    r_table = r"""(?:[\s]+)([\d\w\$_]+\.[\d\w\$_]+\.[\d\w\$_]+)(?:(?:[\s])+|\Z|;|\))""" 
    r_history = r"""^history[\s]*""" + r_table +r"""$"""
    r_export =r"""EXPORT\s+?TABLE\s+?(?:(?:IF NOT EXISTS)(.+?)|(.+?))\s+?AS\s"""
    r_select = r"""[\s]?(FROM|JOIN)[\s]?""" + r_table
    r_d_table = r"""DROP[\s]+TABLE(?:[\s]+IF[\s]+EXISTS)?[\s]+(([\d\w\$_]+)|([\d\w\$_]+\.[\d\w\$_]+))(?:(?:[\s])+|\Z|;|\))"""
    r_drop = r"""DROP[\s]?TABLE[\s]?""" + r_table
    r_asof = r"""(asof+)(?:(?:[\s])+|\Z|\))"""
    r_delta = f"""{r_table}{r_asof}({r_date}|{r_version})""" 

    def __init__(self,spark,debug=False): 
        """ 
        Parameters 
        ---------- 
        spark : object 
            recebe o contexto spark 
        schema : str 
            default: 'cache' 
            Identificador do schema de chache no metastore do dora 
        debug : boolean 
            quando true ativa o modo debug 
        """ 
        self.spark = spark 
        self.verbose = debug 
        self.steps = boto3.client('stepfunctions', region_name=AWS_REGION)
        _user_db  = f"DORA_{DORA_USER.upper()}"
        self.spark.sql(f"CREATE DATABASE IF NOT EXISTS `{_user_db}` COMMENT 'Sandbox for {os.environ.get('EMAIL',DORA_USER)}' LOCATION '{DORA_STORAGE}://{DORA_BUCKET}/workspaces/{DORA_USER}/data/'")
        self.spark.sql(f"USE `{_user_db}`")
        dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
        self.table_status = dynamodb.Table(os.environ.get('CATALOG_TABLES'))
         
    def printd(self,*messages): 
        """ 
        Utilitário usado para exibir as mensagem quando o modo debug está ativado 
        ---------- 
        messages : list 
            Lista de todas as mensagems a serem printadas  
        """ 
        if self.verbose: 
            for message in messages: 
                print(message) 
     
    def get_table_status(self,table_list): 
        """ 
        Consulta os metadados das tabelas solicitadas no Dora Metastore 
        ---------- 
        table_list : list 
            Lista de todas as tabelas solicitadas na query  
        Returns 
        ------- 
        Dict 
            Retorna um dicionário com os metadados de todas as tabelas solicitadas 
        """
        tables = dict()
        for table in table_list:
            table_id = table.upper().replace('.','_')
            table_meta = self.table_status.get_item(Key={"identifier": table_id}).get("Item")
            LOGGER.debug("%s:%s", table, table_id)
            if table_meta is None:
                _dbs, _sch, _tbl = table.split('.')
                LOGGER.warning("%s is not found in DORA metastore, starting import process...", table)
                tables[table] = {'identifier':table_id,'base':_dbs,'catalog':_sch,'objectName':_tbl,'outdated':True}
                continue
            last_update = datetime.datetime.strptime(table_meta['lastUpdate'], "%Y-%m-%d")
            next_update = last_update + datetime.timedelta(days=int(table_meta['cacheDays']))
            LOGGER.debug("last update:%s, next update:%s", last_update, next_update)
            tables[table] = table_meta
            if next_update >= datetime.datetime.now():
                LOGGER.info("%s is updated: %s (%s days)", table, table_meta['lastUpdate'],table_meta['cacheDays'])
                tables[table]['outdated'] = False
                continue
            if next_update < datetime.datetime.now():
                LOGGER.warning("%s is outdated: %s (%s days)", table, table_meta['lastUpdate'],table_meta['cacheDays'])
                tables[table]['outdated'] = True
                continue
        return tables
     
    def load_tables(self, table_list): 
        """ 
        Agenda a execução de todas as tableas que precisam ser atualizadas 
        ---------- 
        table_list : list 
            Lista de todas as tabelas desatualizadas 
        Returns 
        ------- 
        List 
            Retorna a lista das execuções agendadas via Step-Function 
        """ 
        responses=list() 
        for tbl in table_list:
            if tbl.get("execution") is not None:
                # Verifica se já existe um processo em execução
                execution = self.steps.describe_execution(executionArn=tbl['execution'])
                if execution['status'] == 'RUNNING':
                    # Em caso positivo adiciona a lista de execução para o processo de waiting
                    responses.append(execution['executionArn'])
                    continue
            # Caso não exista nenhuma execução em andamento submete uma nova
            input_data = {
                "username":DORA_USER,
                "connection_name":tbl['base'],
                "schema":tbl['catalog'],
                "table":tbl['objectName'],
                "condition":tbl.get("condition"),
                "partition":tbl.get("partition")}
            LOGGER.debug('load_tables:input_data: %s',input_data)
            responses.append(self.start_execution(input_data)['executionArn']) 
        return responses

    def start_execution(self, input_data):
        """
        Função responsável pela submissão dos processos de importação de dados via maquina de estados
        ---------- 
        input_data : json 
            dados que serão submetidos ao processo de DoraImportMachine
        """
        state_machine = os.environ.get('STATE_MACHINE')
        LOGGER.debug('import:state_machine:%s', state_machine)
        execution=self.steps.start_execution(stateMachineArn=state_machine,input=json.dumps(input_data))
        if execution['ResponseMetadata']['HTTPStatusCode'] != 200:
            LOGGER.error('import:execution:%s', execution)
            raise ValueError(f"Error on start execution:{execution}")
        describe_execution = self.steps.describe_execution(executionArn=execution['executionArn'])
        if describe_execution['ResponseMetadata']['HTTPStatusCode'] != 200:
            LOGGER.error('import:describe_execution:%s', describe_execution)
            raise ValueError("Error on start describe_execution:{describe_execution}")
        return describe_execution

    def wait_execution(self, executions): 
        """ 
        Verifica o andamento das Step-Functions em execução 
        ---------- 
        executions : list 
            Lista de todas as execuções em andamento  
        Returns 
        ------- 
        List 
            Retorna a lista das execuções concluídas 
        """ 
        responses=list() 
        while len(executions) > 0: 
            sleep(2) 
            for execution in executions: 
                execution_status=self.steps.describe_execution(executionArn=execution) 
                if execution_status.get('status') != 'RUNNING': 
                    responses.append(execution_status) 
                    LOGGER.debug('wait_execution:execution_status:%s',execution_status) 
                    # TODO: Atualizar a cache das tabelas no Spark
                    # input_data = json.loads(execution_status['input']) 
                    # cache_table = f"{CACHE_DB}.{input_data['connection_name']}_{input_data['schema']}_{input_data['table']}" 
                    # self.spark.sql(f"REFRESH TABLE {cache_table}") 
                    executions.remove(execution) 
        return responses 

    def get_history(self, table):
        """ 
        Cria a tabela de versões, utilziada para localização dos dados de cada versão do objeto 
        ---------- 
        table : string 
            Nome interno da tabela no databse cache 
        Returns 
        ------- 
        string 
            Nome da tabela temporária contendo os dados das versões que compõe a tabela 
        """ 
        _conn, _catalog, _table = table.upper().split('.')
        _table = table.replace('.','_').upper()
        _path = f"""{DORA_STORAGE}://{DORA_BUCKET}/delta/{_conn}/{_catalog}/{_table}/"""
        _history = f"""H_{_table}"""
        try:  
            self.spark.catalog.isCached(_history)  
        except AnalysisException:
            LOGGER.warning("Creating Table History for %s", table)
            DeltaTable.forPath(self.spark, _path).history().createOrReplaceTempView(_history)
        return _history

    def get_version_of(self, table, version): 
        """ 
        Consulta as versões de uma determinada tabela 
        ---------- 
        table : string 
            Nome interno da tabela no databse cache 
        version : string 
            Numero da versão ou data que se deseja consultar 
        alias : string 
            Nome funcional da tabela, para apresentação 
        Returns 
        ------- 
        string 
            Nome da tabela temporária contendo os dados da versão solicitada 
        """ 
        _version = int(version.replace("'",""))
        _conn, _catalog, _table = table.upper().split('.')
        _table = table.replace('.','_').upper()
        _path = f"""{DORA_STORAGE}://{DORA_BUCKET}/delta/{_conn}/{_catalog}/{_table}/"""
        _history = self.get_history(table)
        _table_v = f"""V{_version}_{_table}"""
        LOGGER.debug("History Table: %s", _history)
        try:  
            self.spark.catalog.isCached(_table_v)  
        except AnalysisException:
            LOGGER.warning("Creating cache for %s in version %s", table, version)
            self.spark.read.format("delta").option("versionAsOf", _version).load(_path).createOrReplaceTempView(_table_v)
        return _table_v

    def sql_parser(self, sql): 
        """ 
        Realiza o parser do SQL utilizado para geração do HASH 
        ---------- 
        sql : string 
            Recebe a query bruta. 
        Returns 
        ------- 
        list 
            Retorna a lista de todos os itens da query formatados 
        """ 
        for statement in sqlparse.parse(sql):
            if statement.get_type() != 'SELECT': 
                raise ValueError(f"Only 'SELECT' statements are allowed") 
            query = list() 
            for keys, value in enumerate(statement.tokens):
                if value.is_whitespace: 
                    continue 
                if value.is_keyword: 
                    query.append(value.normalized.upper()) 
                else: 
                    query.append(value.normalized) 
            return query 

    def sql(self, query, **kwargs): 
        """ 
        Executa query usando SparkSQL 
        ---------- 
        query : string 
            Recebe a query bruta. 
        kwargs : dict 
            Argumentos enviados pelo usuário pelo Magic Comand 
        Returns 
        ------- 
        Dataframe 
            retorna o dataframe da query. 
        """ 
        timestamp = datetime.datetime.now()  
        # Palavras reservadas para acesso dos dados diretamente da workspace do usuário
        query = query.replace("workspace://", f"{DORA_STORAGE}://{DORA_BUCKET}/workspaces/{DORA_USER}/")
        query = query.replace("cloud://", f"{DORA_STORAGE}://{DORA_BUCKET}/workspaces/{DORA_USER}/")
        # Habilita a versão verbosa da execução
        self.verbose = kwargs.get("verbose")
        LOGGER.debug('sql:parameters:%s',kwargs)
        # Consulta adhoc
        if kwargs.get("connection") is not None: 
            parser = self.sql_parser(query) 
            table_name = hashlib.sha1(''.join(parser).encode('utf8')).hexdigest() 
            output_path = f"{DORA_STORAGE}://{DORA_BUCKET}/adhoc/{kwargs['connection']}/{table_name}"
            input_data = {"username":DORA_USER,"connection_name":kwargs["connection"],"adhoc": {"query":query ,"output": output_path}}
            LOGGER.debug('adhoc:input_data:%s', input_data)
            try:
                if kwargs.get("refresh"):
                    LOGGER.warning('adhoc:Forced refresh data by user %s', DORA_USER)
                    raise ValueError("Force Refresh")
                return self.spark.read.parquet(output_path)
            except Exception as miss_ex:
                LOGGER.debug('adhoc:spark:%s', miss_ex)
                execution_status = self.start_execution(input_data)
                LOGGER.info('adhoc:DoraImportMachine:%s', execution_status['executionArn'])
                while True:
                    sleep(2)
                    execution_status = self.steps.describe_execution(executionArn=execution_status['executionArn'])
                    if execution_status.get('status') != 'RUNNING': 
                        break
                LOGGER.debug('adhoc:status:%s', execution_status)
                if execution_status.get('status') == 'SUCCEEDED':
                    LOGGER.debug('adhoc:output:%s', execution_status.get('output'))
                    output = json.loads(execution_status['output'])
                    return self.spark.read.parquet(output['data_file'])
                failed_event = self.steps.get_execution_history(executionArn=execution_status['executionArn'],maxResults=1,reverseOrder=True)
                LOGGER.debug('adhoc:failed:event:%s', failed_event)
                fail_cause = failed_event['events'][0]['executionFailedEventDetails']['cause']
                LOGGER.error('adhoc:error:%s', fail_cause)
                try:
                    error_log = json.loads(fail_cause)
                except:
                    error_log = {"errorType":fail_cause}
                return self.spark.sparkContext.parallelize(Row({"errorType":error_log['errorType']})).toDF()
            finally:
                time_after_spark = datetime.datetime.now()
                LOGGER.info("Execution Time: %s", (time_after_spark - timestamp).total_seconds())
        # Informar o usuário de que o comando de refresh é utilizado apenas para consultas do tipo "adhoc"
        if kwargs.get("refresh"):
            LOGGER.warning('The "refresh" parameter is only used for adhoc queries.')
        # Não é possível realizar drop em tabelas controladas pelo dora
        if len(re.findall(self.r_drop, query, re.MULTILINE | re.IGNORECASE)) > 0:
            error_message = "Is not possible to DROP a DORA's external table"
            LOGGER.error(error_message)
            return self.spark.sparkContext.parallelize(Row({"errorType":error_message})).toDF()
        # Lista as conexões que o usuário tem acesso
        if re.findall(self.r_user_connections, query, re.MULTILINE | re.IGNORECASE):
            connection = pymysql.connect( host=os.environ.get('HIVE_BASE') \
                                        , user=os.environ.get('HIVE_USER') \
                                        , password=os.environ.get('HIVE_PASS') \
                                        , db='isa', cursorclass=pymysql.cursors.DictCursor) 
            try: 
                with connection.cursor() as cursor: 
                    cursor.execute(f"SELECT connection, jdbc, dialect FROM isa.user_connections_v WHERE username='{DORA_USER}'")
                    data = cursor.fetchall()
                    return self.spark.sparkContext.parallelize(data).toDF()
            except:
                LOGGER.warning("You dont have any connections")
                return self.spark.sparkContext.parallelize(Row({"connection":"No Connection","dialect":"null","jdbc":"null"})).toDF()
            finally: 
                connection.close() 
        # Lista das informações de atualização e configuração das tabelas em cache
        if re.findall(self.r_cache_tables, query, re.MULTILINE | re.IGNORECASE):
            object_keys = ['objectKey','lastUpdate','cacheDays','condition','partition']
            response = self.table_status.scan(AttributesToGet=object_keys)['Items']
            if response:
                return self.spark.sparkContext.parallelize(response).toDF()
            return self.spark.sparkContext.parallelize(Row({'objectKey':'You dont have any tables in cache'})).toDF()
        # Lista das informações de atualização e configuração das tabelas em cache
        history_match = re.match(self.r_history, query, re.MULTILINE | re.IGNORECASE)
        if history_match:
            return self.spark.table(self.get_history(history_match[1]))
        # Altera o create table para view
        results = re.match(self.r_export, query, re.MULTILINE | re.IGNORECASE)
        if results:
            try:
                _query = query.replace(results[0],f"CREATE OR REPLACE VIEW DORA.{results[2]} AS ")
                LOGGER.debug("executing:\n%s", _query)
                return self.spark.sql(_query)
            except ParseException as parser_ex:
                LOGGER.error("ParseException:\n%s", parser_ex)
                return self.spark.sparkContext.parallelize(Row({"error":parser_ex})).toDF() 
            finally:
                time_after_spark = datetime.datetime.now()
                LOGGER.info("Execution Time: %s", (time_after_spark - timestamp).total_seconds())
        # Leitura de versão histórica das tabelas
        for n, match in enumerate(re.finditer(self.r_delta, query, re.MULTILINE | re.IGNORECASE), start=1):  
            table_name = self.get_version_of(match.group(1),match.group(3))
            LOGGER.info("table_name: %s", table_name)
            query=query.replace(match.group(0),f" {table_name}")
        # Recupera a lista de tabelas de acordo com a sintaxe DORA
        table_list = set([v.group(2) for k,v in enumerate(re.finditer(self.r_select, query, re.MULTILINE | re.IGNORECASE), start=1)]) 
        LOGGER.debug("sql:table_list: %s", table_list)
        # Recupera os metadados salvos no metastore do DORA
        table_meta = self.get_table_status(table_list) 
        # Filtra pela tabelas que estão desatualizadas
        outdated_tables = [table_meta[t] for t in table_meta if table_meta[t]['outdated']]
        LOGGER.debug('sql:outdated_tables: %s', outdated_tables) 
        # Inicia o processo de importalçao de todas as tabelas que estejam com dados desatualizados, ou novas
        executions = self.load_tables(outdated_tables)
        LOGGER.debug('sql:executions: %s', executions)
        # Após aguardar pela finalização de todos os processos
        for execution in self.wait_execution(executions): 
            # Verifica se algum terminou com falha
            if execution['status']=='FAILED':
                # Em caso de falha recupera os detalhes da ultima etapa executada
                failed_event = self.steps.get_execution_history(executionArn=execution['executionArn'],maxResults=1,reverseOrder=True)
                LOGGER.debug('sql:import:failed:event:%s', failed_event)
                fail_cause = failed_event['events'][0]['executionFailedEventDetails']['cause']
                LOGGER.error('sql:import:error:%s', fail_cause)
                raise ValueError("ImportProcess: %s", fail_cause)
        # Substituir as chaves pelas tabelas em cache do metastore
        for table_id in table_meta: 
            query = query.replace(table_id, f"{table_meta[table_id]['base']}.{table_meta[table_id]['identifier']}") 
        LOGGER.debug('sql:query:%s', query)
        # Os timers são para identificação dos tempos de execução do spark
        time_before_spark = datetime.datetime.now() 
        try:
            return self.spark.sql(query)
        except AnalysisException as analysis_exception:
            LOGGER.error('sql:spark:error:%s', analysis_exception)
            return self.spark.sparkContext.parallelize(Row({"error":analysis_exception})).toDF() 
        finally:
            time_after_spark = datetime.datetime.now()
            LOGGER.debug("Query Time: %s", (time_after_spark - time_before_spark).total_seconds()) 
            LOGGER.info("Execution Time: %s", (time_after_spark - timestamp).total_seconds())

    def query(self, query, **kwargs):
        """ 
            [WARNING]: This method will be deprecated.
            Faz um wrapper do método sql, alterando alguns parâmetros 
            para manter a compatibilidade com a versão antiga 1.x. 
        
            ---------- 
            query : string 
                Recebe a query bruta. 
            kwargs : dict 
                Argumentos enviados pelo usuário pelo Magic Comand 
            Returns 
            ------- 
            Dataframe 
                retorna o dataframe da query. 
         """
        if kwargs.get("base_name"):
            kwargs["connection"] = kwargs.pop("base_name")
        if kwargs.get("show"):
            return self.sql(query, **kwargs).show()
        return self.sql(query, **kwargs)

        

class ISAMagic(Magics): 
    """
    Jupyter magic command
    """
    from IPython.core.magic import register_cell_magic 
    ipython  = get_ipython() 
    def __init__(self, ISAContext): 
        self.isa = ISAContext 
        self.ipython.register_magic_function(self.sql, 'cell')
        self.ipython.register_magic_function(self.asql, 'cell')
 
    @magic_arguments.magic_arguments() 
    @magic_arguments.argument('--connection', '-c', default=None, help='Connection Name') 
    @magic_arguments.argument('--limit', '-l', type=int, default=100, help='Show limit') 
    @magic_arguments.argument('--verbose', '-v',action='store_true',help='Print Debug messages') 
    @magic_arguments.argument('--out', '-o',help='The variable to return the results in')
    @magic_arguments.argument('--refresh', '-r', help='Refresh cache data', action='store_true')
    def sql(self, line, query): 
        """Execute Spark SQL Query with Dora Engine 
 
        :param query: Spark SQL Query 
 
        :returns: Spark Dataframe 
        :rtype: Dataframe 
 
        Dora Version (2.0) 
        ------- 
        ISA 0.1.4 
        """ 
        args = magic_arguments.parse_argstring(self.sql, line)
        args = vars(args)
        if args.get("out") is None: 
            return self.isa.sql(query,**args).limit(args.get("limit")).toPandas() 
        else: 
            df = self.isa.sql(query,**args) 
            self.ipython.user_ns[args.get("out")] = df 
            return df 
        
    @magic_arguments.magic_arguments() 
    @magic_arguments.argument('--connection', '-c', default=None, help='Connection Name') 
    @magic_arguments.argument('--limit', '-l', type=int, default=100, help='Show limit') 
    @magic_arguments.argument('--verbose', '-v',action='store_true',help='Print Debug messages') 
    @magic_arguments.argument('--out', '-o',help='The variable to return the results in')
    @magic_arguments.argument('--refresh', '-r', help='Refresh cache data', action='store_true')
    def asql(self, line, query): 
        """
        [WARNING]: This method will be deprecated, use sql instead.
        Execute Spark SQL Query with Dora Engine.
    
        :param query: Spark SQL Query 
        
        :returns: Spark Dataframe
        :rtype: Dataframe 
        
        """ 
        args = magic_arguments.parse_argstring(self.sql, line)
        args = vars(args)
        if args.get("out") is None: 
            return self.isa.query(query,**args).limit(args.get("limit")).toPandas()
        else: 
            df = self.isa.query(query,**args) 
            self.ipython.user_ns[args.get("out")] = df 
            return df 
# dora=ISAContext(spark)
# asql = ISAContext(spark)
# ISAMagic(dora)
# ISAMagic(asql)
