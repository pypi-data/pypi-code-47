#-*- coding:utf-8 -*-
import os

from flask import Flask
from extensions import db
import flask_excel as excel
from flask import current_app
import logging
from typhoonw.models import Total, PathDesc, RainstormDesc
from typhoonw.auth import auth_bp
from typhoonw.data import data_bp
from flask_bootstrap import Bootstrap

def create_app(test_config=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    logger = logging.getLogger('xuye')
    app.logger.info(test_config)

    # 获取项目根目录
    root_path = os.path.dirname(os.path.dirname(__file__))

    if not test_config:
        # 获取开发环境配置文件
        config_path = os.path.join(root_path, 'config_dev.py')
    else:
        # 获取测试环境配置文件
        config_path = os.path.join(root_path, 'config_test.py')
    app.config.from_pyfile(config_path, silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 注册插件
    register_extensions(app)
    # 注册路由
    register_blueprints(app)

    # 测试页面
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/db')
    def db_create():
        init_db()
        return 'ok!'

    return app

def register_extensions(app):
    # app与flask-sqlalchemy绑定
    db.init_app(app)
    excel.init_excel(app)
    Bootstrap(app)

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(data_bp)

def init_db():
    db.create_all()