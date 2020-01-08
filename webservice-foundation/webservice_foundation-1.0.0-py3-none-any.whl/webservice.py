import argparse
import importlib
import os

from tornado.ioloop import IOLoop
from tornado.web import Application

from .baserequest import BaseRequestHandler
from .error import *

import logging

logger = logging.getLogger('webservice_foundation').getChild('WebService')


class WebService:

    def __init__(self):
        self.app: Application = None

    def load_setting_yaml(self, yaml_path):
        import yaml
        with open(yaml_path, 'r') as f:
            yaml_data = yaml.safe_load(f)
        del yaml
        return yaml_data

    def load_setting_json(self, json_path):
        import json
        with open(json_path, 'r') as f:
            json_data = json.load(f)
        del json
        return json_data

    def load_key(self, key, obj):
        if key in obj:
            return obj[key]
        raise self.raise_(key, self.webservice_file)

    def __call__(self, webservice_file, port, address='', **kwargs):
        start = kwargs.pop('start', True)
        self.make_app(webservice_file)
        self.app.listen(port, address, **kwargs)
        if start:
            logger.info('WebService Start')
            IOLoop.current().start()
            logger.info('WebService End')

    def make_app(self, webservice_file):
        import importlib
        setting_data = {}
        self.raise_ = Exception
        _, ext = os.path.splitext(webservice_file)
        if ext in ['.yaml', '.yml']:
            setting_data = self.load_setting_yaml(webservice_file)
            self.raise_ = YamlKeyNotFoundError
        elif ext == '.json':
            setting_data = self.load_setting_json(webservice_file)
            self.raise_ = JsonKeyNotFoundError
        else:
            raise InvalidExtensionError(
                '指定された拡張子は読み込めません。(%s)' % webservice_file)

        self.webservice_file = webservice_file
        routers = []
        # serviceセクション
        services: dict = self.load_key('services', setting_data)
        service: dict = None
        for name, service in services.items():
            # ハンドラーキー
            module_name: str = self.load_key('module', service)
            # モジュール動的インポート
            module = importlib.import_module(module_name)
            # エンドポイントキー
            endpoint: str = self.load_key('endpoint', service)
            # イベントセクション
            events: dict = service.get('events', None)
            if events:
                for event, value in events.items():
                    # event内容に応じて変更
                    req = None
                    if event == 'http':
                        # HTTPメソッドキー
                        methods: dict = self.load_key('methods', value)
                        for method, func in methods.items():
                            # 呼び出す関数実体取得
                            func = getattr(module, func)
                            # HTTPメソッドの設定
                            methods[method] = func

                        # RequestHandlerのインスタンス生成（サブクラスとして生成）
                        req = type(f'{name}Handler',
                                   (BaseRequestHandler,), methods)

                    elif event == 'websocket':
                        pass
                    else:
                        continue
                routers.append((endpoint, req))
                continue

            # オリジナルクラス
            cls_: dict = service.get('cls', None)
            if cls_:
                # モジュールからオリジナルクラスの実体を生成
                req = getattr(module, cls_['handler'])
                routers.append((endpoint, req))
                continue

        envs = setting_data.get('environment', {})
        for key, value in envs.items():
            # 環境変数は先勝ち
            if not os.environ.get(key, False):
                os.environ[key] = value
        settings = setting_data.get('app_setting', {})
        self.app = Application(routers, **settings)
        del importlib


def main():
    import sys
    sys.path.append(os.getcwd())
    WEBSERVICE_FILENAME = 'webservice.yaml'
    PORT = '8080'
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="webサービス設定ファイル(default:%s)" % WEBSERVICE_FILENAME,
                        default=WEBSERVICE_FILENAME)
    parser.add_argument(
        '-p', '--port', help="webサービスのポート番号(default:%s)" % PORT, default=PORT)
    args = parser.parse_args()
    WebService()(args.file, int(args.port))
