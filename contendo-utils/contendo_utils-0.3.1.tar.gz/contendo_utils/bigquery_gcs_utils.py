import os
import logging

from google.cloud import bigquery
from google.cloud import storage
# from gcsfs import GCSFileSystem
from google.api_core.exceptions import BadRequest

from contendo_utils import *

class BigqueryUtils:
    @contendo_classfunction_logger
    def __init__(self, project=None):
        if project:
            self.__bigquery_client = bigquery.Client(project=project)
            self._storage_client = storage.Client(project=project)
        else:
            self.__bigquery_client = bigquery.Client()
            self._storage_client = storage.Client()

    # String upload/download to a file.
    @contendo_classfunction_logger
    def upload_string_to_gcp(self, data: str, bucketName: str, targetFileName: str) -> None:
        bucket = self._storage_client.get_bucket(bucketName)
        blob = bucket.blob(targetFileName)
        res = blob.upload_from_string(data)
        return 'gs://{}/{}'.format(bucketName, targetFileName)

    @contendo_classfunction_logger
    def read_string_from_gcp(self, bucketName, fromFileName):
        data = None
        try:
            bucket = self._storage_client.get_bucket(bucketName)
            blob = bucket.blob(fromFileName)
            data = blob.download_as_string()
        # except storage. NotFound as e:
        #    print('Info: File not found in BigqueryUtils.read_string_from_gcp({}, {})', bucketName, fromFileName)
        except Exception as e:
            print('Error in BigqueryUtils.read_string_from_gcp({}, {}) {}, trace {}', bucketName, fromFileName, e,
                  type(e))

        return data

    # File upload/download with optional timestamp check.
    @contendo_classfunction_logger
    def upload_file_to_gcp(self, bucketName: str, inFileName: str, targerFileName: str, timestamp: bool = False) -> str:
        if timestamp:
            ts = str(os.path.getctime(inFileName))
            self.upload_string_to_gcp(data=ts, bucketName=bucketName, targetFileName=targerFileName + '.timestamp')
        bucket = self._storage_client.get_bucket(bucketName)
        blob = bucket.blob(targerFileName)
        res = blob.upload_from_filename(inFileName)
        return 'gs://{}/{}'.format(bucketName, targerFileName)

    @contendo_classfunction_logger
    def download_from_gcp(
            self,
            bucketName: str,
            fromFileName: str,
            toFileName: str,
            checkTimestamp: bool = False
    ) -> bool:
        try:
            bucket = self._storage_client.get_bucket(bucketName)
            blob = bucket.blob(fromFileName)
            if os.path.exists(toFileName) and checkTimestamp:
                try:
                    ts = self.read_string_from_gcp(bucketName=bucketName, fromFileName=fromFileName + '.timestamp')
                    if float(ts) <= os.path.getctime(toFileName):
                        return False
                except Exception as e:
                    print('File not exists %s', fromFileName + '.timestamp')

            ProUtils.create_path_directories(toFileName)
            data = blob.download_to_filename(toFileName)
        # except storage. NotFound as e:
        #    raise FileNotFoundError('Info: File not found in BigqueryUtils.read_string_from_gcp({}, {})'.format(bucketName, fromFileName))

        except Exception as e:
            print('Error in BigqueryUtils.read_string_from_gcp({}, {}) {}, trace {}', bucketName, fromFileName, e,
                  type(e))
            raise e

        return True

    #
    #  BigQuery - Google cloud storage - convenience functions.
    #
    @contendo_classfunction_logger
    def save_table_to_gcs(
            self,
            datasetId,
            tableId,
            bucketName,
            targetFileName,
            fileType=bigquery.SourceFormat.CSV,
    ):
        _datasetRef = self.__bigquery_client.dataset(datasetId)
        _tableRef = _datasetRef.table(tableId)
        destinationURI = "gs://{}/{}".format(bucketName, targetFileName)

        extract_job = self.__bigquery_client.extract_table(
            _tableRef,
            destinationURI,
            location='US')
        result = extract_job.result()  # Extracts results to the GCS
        return result

    # creating a dataset if does not exist
    @contendo_classfunction_logger
    def create_dataset(self, datasetId: str) -> None:
        #
        # Make sure the target dataset exists, or create it.
        try:
            assert datasetId in [dataset.dataset_id
                                 for dataset in list(self.__bigquery_client.list_datasets())]
        except AssertionError:  # dataset doesn't exist
            datasetReference = self.__bigquery_client.dataset(datasetId)
            dataset = bigquery.Dataset(datasetReference)
            dataset.location = 'US'
            dataset = self.__bigquery_client.create_dataset(dataset)
        return

    @contendo_classfunction_logger
    def create_table_from_gcp_file(
            self,
            gcpFileURI: str,
            datasetId: str,
            tableId: str,
            writeDisposition: str = 'WRITE_APPEND',
            fileType=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            max_bad_records: int = 0
    ):
        datasetRef = self.__bigquery_client.dataset(datasetId)
        _jobConfig = bigquery.LoadJobConfig()
        _jobConfig.autodetect = True
        _jobConfig.max_bad_records = max_bad_records,
        _jobConfig.write_disposition = writeDisposition
        _jobConfig.source_format = fileType
        load_job = self.__bigquery_client.load_table_from_uri(
            gcpFileURI,
            datasetRef.table(tableId),
            job_config=_jobConfig
        )
        try:
            result = load_job.result()
            if load_job.errors and len(load_job.errors) > 0:
                logger.error('Error occured while loading file %s, errors: \n%s', gcpFileURI, load_job.errors)
        except BadRequest as be:
            logger.error('Error loading file %s, errors: %s', gcpFileURI, load_job.errors)
            raise be

        return result

    @contendo_classfunction_logger
    def create_table_from_local_file(self, localFile, datasetId, tableId, writeDisposition='WRITE_TRUNCATE',
                                     fileType=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, schema=None):
        datasetRef = self.__bigquery_client.dataset(datasetId)
        _jobConfig = bigquery.LoadJobConfig()
        _jobConfig.autodetect = True
        _jobConfig.write_disposition = writeDisposition
        _jobConfig.source_format = fileType
        # _jobConfig.max_bad_records = 100
        if schema and False:
            tableSchema = []
            for field in schema:
                tableSchema.append(bigquery.schema.SchemaField.from_api_repr(field))
            _jobConfig.schema = tableSchema
        fileObj = open(localFile, 'rb')
        load_job = self.__bigquery_client.load_table_from_file(
            fileObj,
            datasetRef.table(tableId),
            job_config=_jobConfig,
        )
        fileObj.close()

        try:
            result = load_job.result()
            if load_job.errors and len(load_job.errors) > 0:
                logger.error('Error occured while loading file %s, errors: \n%s', localFile, load_job.errors)
        except BadRequest as be:
            logger.error('Error loading file %s, errors: %s', localFile, load_job.errors)
            raise be

        return result

    @contendo_classfunction_logger
    def get_table_schema(self, datasetId, tableId):

        datasetRef = self.__bigquery_client.dataset(datasetId)
        tableRef = datasetRef.table(tableId)
        table = self.__bigquery_client.get_table(tableRef)  # API Request

        schema = []
        for schemaField in table.schema:
            schema.append(schemaField.to_api_repr())

        return schema

    @contendo_classfunction_logger
    def execute_query(self, query: str):
        _jobConfig = bigquery.QueryJobConfig()
        query_job = self.__bigquery_client.query(query)
        result = query_job.result()
        return result

    @contendo_classfunction_logger
    def execute_query_to_df(self, query, fillna=''):
        query_job = self.__bigquery_client.query(query)
        ret_df = query_job.result().to_dataframe().fillna(fillna)
        return ret_df

    @contendo_classfunction_logger
    def execute_query_to_dict(self, query, fillna=''):
        query_job = self.__bigquery_client.query(query)
        ret_df = query_job.result().to_dataframe().fillna(fillna)
        retDict = {}
        retDict['nRows'] = ret_df.shape[0]
        retDict['Columns'] = list(ret_df.columns)
        rows = []
        for i, row in ret_df.iterrows():
            rows.append(dict(row))
        retDict['Rows'] = rows
        return retDict

    @contendo_classfunction_logger
    def execute_query_with_schema_and_target(self, query: str, targetDataset: str, targetTable: str, schemaDataset=None,
                                             schemaTable=None):
        #
        # Reset the table based on schema
        writeDisposition = 'WRITE_TRUNCATE'
        if schemaDataset is not None and schemaTable is not None:
            _copyJobConfig = bigquery.CopyJobConfig()
            _copyJobConfig.write_disposition = 'WRITE_TRUNCATE'
            copy_job = self.__bigquery_client.copy_table(
                self.__bigquery_client.dataset(schemaDataset).table(schemaTable),
                self.__bigquery_client.dataset(targetDataset).table(targetTable),
                job_config=_copyJobConfig
            )
            writeDisposition = 'WRITE_APPEND'

        #
        # Set job configuration & execute
        _jobConfig = bigquery.QueryJobConfig()
        _jobConfig.destination = self.__bigquery_client.dataset(targetDataset).table(targetTable)
        _jobConfig.write_disposition = writeDisposition
        metrics_query_job = self.__bigquery_client.query(query, job_config=_jobConfig)
        nRows = metrics_query_job.result().total_rows
        return nRows

    def test():
        _bqu = BigqueryUtils()
        # _bqu.download_from_gcp

    if __name__ == '__main__':
        contendo_logging_setup(default_level=logging.DEBUG)
        os.chdir('{}/tmp'.format(os.environ['HOME']))
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
        test()
