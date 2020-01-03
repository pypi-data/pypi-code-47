from mms.base_logger import BaseLogger
from google.cloud.logging.resource import Resource



class AppEngineLogger(BaseLogger):

    def __init__(self, service_name='', trace_id='', project_id='', module_id='', version_id='', local_run=False):
        super().__init__(service_name=service_name,
                         run_id=trace_id,
                         project_id=project_id)
        self.module_id = module_id
        self.version_id = version_id
        self.local_run = local_run

        if self.local_run is False:
            self.res = Resource(type='gae_app', labels={
                "project_id": super().get_project_id(),
                "module_id": self.module_id,
                "version_id": self.version_id
            })

        self.logger = super().create_logger()

    def update_trace_id(self, new_trace_id):
        super().update_trace_id(new_trace_id=new_trace_id)

    def info(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': super().get_trace_id(),
                                    'service_name': super().get_service_name()},
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
                                    'trace_id': super().get_trace_id(),
                                    'service_name': super().get_service_name()},
                                   resource=self.res,
                                   severity='ERROR')
        else:
            print('Error: {}'.format(message))

    def critical(self, message):
        message = str(message)
        if self.local_run is False:
            self.logger.log_struct({'message': message,
                                    'trace_id': super().get_trace_id(),
                                    'service_name': super().get_service_name()},
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