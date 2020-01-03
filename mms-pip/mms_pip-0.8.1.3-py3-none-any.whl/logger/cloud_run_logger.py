from mms.base_logger import BaseLogger
from google.cloud.logging.resource import Resource


class CloudRunLogger(BaseLogger):

    def __init__(self, service_name='', trace_id='', project_id='', revision_version='', location='', local_run=False):
        super().__init__(service_name=service_name,
                         run_id=trace_id,
                         project_id=project_id)
        self.location = location
        self.revision_version = revision_version
        self.local_run = local_run

        if self.local_run is False:
            self.res = Resource(type='cloud_run_revision', labels={
                "configuration_name": str(super().get_service_name()),
                "location": self.location,
                "project_id": str(super().get_project_id()),
                "revision_name": self.revision_version,
                "service_name": str(super().get_service_name())
            })

        self.logger = super().create_logger()

    def update_trace_id(self, new_trace_id):
        super().update_trace_id(new_trace_id=new_trace_id)

    def info(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': str(super().get_trace_id()),
                                    'service_name': str(super().get_service_name())},
                                   resource=self.res,
                                   severity='INFO')
        else:
            print('Info: {}'.format(message))

    def warning(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': super().get_trace_id(),
                                    'service_name': super().get_service_name()},
                                   resource=self.res,
                                   severity='WARNING')
        else:
            print('Warning: {}'.format(message))

    def error(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': str(super().get_trace_id()),
                                    'service_name': str(super().get_service_name())},
                                   resource=self.res,
                                   severity='ERROR')
        else:
            print('Error: {}'.format(message))

    def critical(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': str(super().get_trace_id()),
                                    'service_name': str(super().get_service_name())},
                                   resource=self.res,
                                   severity='CRITICAL')
        else:
            print('Critical: {}'.format(message))

    def debug(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': super().get_trace_id(),
                                    'service_name': super().get_service_name()},
                                   resource=self.res,
                                   severity='DEBUG')
        else:
            print('Debug: {}'.format(message))