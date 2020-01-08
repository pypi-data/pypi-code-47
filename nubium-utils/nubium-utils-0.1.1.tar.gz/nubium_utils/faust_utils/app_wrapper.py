from abc import ABC, abstractmethod
import os
import sys
from nubium_utils.metrics import MetricsManager
from .instrumented_app import InstrumentedApp


class FaustAppWrapper(ABC):
    """
    A wrapper around the Faust app so that it may be more easily unit tested.
    """

    def __init__(self, faust_config, avro_client, metrics_manager: MetricsManager):
        self.faust_config = faust_config
        self.avro_client = avro_client

        self.app = InstrumentedApp(**self.faust_config)
        self.app.wrapper = self
        self.metrics_manager = metrics_manager

        self._init_serializers()
        self._init_records()
        self._init_topics()
        self._init_tables()
        self._init_agents()
        self._init_metrics_pushing()

    def get_schema_path(self, file, schema_path_from_src_root='./schemas'):
        """
        Ensures that the Faust app's schema files are always correctly referenced/loaded regardless of your init path.
        :param file: name of the schema file
        :param schema_path_from_src_root: based on the root of the app, where the schemas folder is located.
        :return: relative path to load the schema at runtime
        """
        runtime_path = os.getcwd()
        app_file_path = os.path.abspath(sys.modules[self.__module__].__file__)
        common_path = os.path.commonpath([runtime_path, app_file_path])
        rel_path = os.path.relpath(common_path, runtime_path)
        return os.path.join(runtime_path, rel_path, schema_path_from_src_root, file)

    @abstractmethod
    def _init_serializers(self):
        pass

    @abstractmethod
    def _init_records(self):
        pass

    @abstractmethod
    def _init_topics(self):
        pass

    @abstractmethod
    def _init_tables(self):
        pass

    @abstractmethod
    def _init_agents(self):
        pass

    def agent_exception(self, exc):
        """
        Increments the message errors metric by one
        :param exc:
        :return:
        """
        self.metrics_manager.inc_message_errors(exc)

    def _init_metrics_pushing(self):
        """
        Defines method for updating metrics from Faust sensor and pushing data
        :return: None
        """

        @self.app.timer(2)
        async def push_metrics():
            """
            Updates gauges from Faust and pushes data to prometheus pushgateways
            :return: None
            """
            self.set_gauges()
            self.metrics_manager.push_metrics()

    def set_gauges(self):

        self.metrics_manager.messages_consumed.labels(
            job=self.metrics_manager.job,
            app=self.metrics_manager.app
        ).set(self.app.monitor.messages_received_total)
        self.metrics_manager.messages_produced.labels(
            job=self.metrics_manager.job,
            app=self.metrics_manager.app
        ).set(self.app.monitor.messages_sent)
