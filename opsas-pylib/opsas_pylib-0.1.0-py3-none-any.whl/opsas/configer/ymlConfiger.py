import yaml

from .BaseConfiger import BaseConfiger


class YmlConfiger(BaseConfiger):
    """
    Get Config from yaml files
    """

    def __init__(self, ordered_file_paths, logger=None):
        super().__init__(logger)
        self.ordered_file_lists = ordered_file_paths
        self.data_map = self.render_data_map()

    @staticmethod
    def load_yaml(yaml_path):
        """
        Get data in yaml files
        :param yaml_path:
        :return: dict|list
        """
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        return data

    def render_data_map(self) -> dict:
        """
        Load yaml from multi file. duplicated keys will be overide by later orderd yaml
        :return: dict
        """
        data_sources = [(file_path, self.load_yaml(file_path),) for file_path in self.ordered_file_lists]
        data_map = {}
        for file_path, yaml_data in data_sources:
            for k, v in yaml_data.items():
                if v is None:
                    self.logger.info(f"Ignore None value for {k} in {file_path}")
                    continue
                data_map[k] = {
                    "value": v,
                    "source": file_path
                }
        return data_map
