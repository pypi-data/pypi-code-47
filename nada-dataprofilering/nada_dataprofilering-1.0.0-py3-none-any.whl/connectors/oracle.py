import cx_Oracle
from urllib import parse
import pandas as pd


class OracleConnector:

    def __init__(self, connection_string):
        pcs = self._parse_connection_string(connection_string)
        dsn = self._make_dsn(pcs)

        self._conn, self._cur = self.establish_db_conn(pcs, dsn)

    def execute(self, query, binds=[]):
        self._cur.execute(query, binds)

    def execute_select(self, query, binds=[]):
        self._cur.execute(query, binds)
        response = self._cur.fetchall()

        if len(response) == 1 and len(response[0]):
            return response[0][0]
        else:
            return response

    def to_pandas(self, query):
        return pd.read_sql(query, self._conn)

    def commit(self):
        self._conn.commit()

    def close_conn(self):
        self._cur.close()

    @staticmethod
    def establish_db_conn(parsed_conn_string, dsn):
        conn = cx_Oracle.connect(
            user=parsed_conn_string['user'],
            password=parsed_conn_string['password'],
            dsn=dsn,
            encoding='utf-8'
        )
        return conn, conn.cursor()

    @staticmethod
    def _make_dsn(parsed_conn_string):
        dsn = cx_Oracle.makedsn(host=parsed_conn_string['host'],
                                port=parsed_conn_string['port'],
                                service_name=parsed_conn_string['service_name'])
        return dsn

    @staticmethod
    def _parse_connection_string(connection_string):
        res = parse.urlparse(connection_string)

        return {
            'user': res.username,
            'password': res.password,
            'host': res.hostname,
            'port': res.port,
            'service_name': res.path[1:]
        }


