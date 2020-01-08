class SettingKeyNotFoundError(Exception):
    """Webサービス指定キー見つからないエラー基底クラス"""

    def __init__(self, key_name: str, *args, **kwargs):
        self.key_name = key_name
        self.file_path = ''
        super(SettingKeyNotFoundError, self).__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.file_path}内に{self.key_name}キーが存在しません。'


class YamlKeyNotFoundError(SettingKeyNotFoundError):
    """Yamlファイル"""

    def __init__(self, key_name, yaml_path, *args, **kwargs):
        super(YamlKeyNotFoundError, self).__init__(key_name, *args, **kwargs)
        self.file_path = yaml_path


class JsonKeyNotFoundError(SettingKeyNotFoundError):
    """Jsonファイル"""

    def __init__(self, key_name, json_path, *args, **kwargs):
        super(JsonKeyNotFoundError, self).__init__(key_name, *args, **kwargs)
        self.file_path = json_path


class InvalidExtensionError(Exception):
    pass
