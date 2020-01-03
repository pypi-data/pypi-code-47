from mms.base_logger import BaseLogger
from google.cloud.logging.resource import Resource


class KubernetesLogger(BaseLogger):

    def __init__(self, service_name='', trace_id='', project_id='', cluster_name='', container_name='',
                 location='', namespace='', local_run=False):
        super().__init__(service_name=service_name,
                         run_id=trace_id,
                         project_id=project_id)
        self.cluster_name = cluster_name,
        self.container_name = container_name,
        self.location = location,
        self.namespace = namespace
        self.local_run = local_run

        if self.local_run is False:
            self.res = Resource(type='k8s_container', labels={
                "cluster_name": self.cluster_name,
                "container_name": self.container_name,
                "project_id": super().get_project_id(),
                "location": self.location,
                "namespace_name": self.namespace,
                "pod_id": ''
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