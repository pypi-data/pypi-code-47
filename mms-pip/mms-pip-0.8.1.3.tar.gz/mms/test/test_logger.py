from mms.logger.cloud_run_logger import CloudRunLogger


if __name__ == '__main__':

    logger = CloudRunLogger(service_name='th-testservice',
                            trace_id='1234',
                            project_id='spielwiese-tobias',
                            revision_version='latese',
                            location='europe-west1')


    logger.error('This is a test error')
    logger.info('This is a test info')

