from typing import Dict, Tuple, List
import json
from pathlib import Path
import re
from lesscli import Application
from arms.spring_tpl import from_model_tpl, from_mapper_tpl, from_mapper_xml_tpl, get_real_table_comment
from arms.utils.common import camelize, ArmsTpl
from arms.utils.database import init as database_init, make_session

PACKAGE_ROOT = ''
MODEL_PATH = Path()
MAPPER_PATH = Path()
MAPPERXML_PATH = Path()
CONTROLLER_PATH = Path()


model_comment_map: Dict[str, str] = {}  # Dict[modelname] -> table_comment


def load_config() -> Dict:
    global PACKAGE_ROOT
    global MODEL_PATH
    global MAPPER_PATH
    global MAPPERXML_PATH
    global CONTROLLER_PATH
    config = json.loads(open('.arms/config.json').read())
    PACKAGE_ROOT = config['PACKAGE_ROOT']
    MODEL_PATH = Path(config['MODEL_PATH'])
    MAPPER_PATH = Path(config['MAPPER_PATH'])
    MAPPERXML_PATH = Path(config['MAPPERXML_PATH'])
    CONTROLLER_PATH = Path(config['CONTROLLER_PATH'])
    return config


def touch_models(db_session) -> None:
    """
    查询数据库，根据需要创建Model, Mapper, Xml
    :param db_session:
    """
    rows = db_session.execute('show tables')
    for row in rows:
        tablename: str = row[0]
        if tablename.startswith('flyway_') or tablename in ['tbl_acl', 'tbl_directory']:
            continue
        if tablename.startswith('Tbl'):
            modelname = tablename[3:]
        elif tablename.startswith('tbl_'):
            modelname = ''.join(x.capitalize() for x in tablename[4:].split('_'))
        else:
            continue
        # 判断Model文件是否存在
        model_path = MODEL_PATH / f'{modelname}.java'
        table_comment = parse_table_comment(db_session, tablename)
        mysql_dict = parse_table(db_session, tablename)
        table_comment = get_real_table_comment(mysql_dict, table_comment)
        model_comment_map[modelname] = table_comment  # 为创建controller准备数据
        if not model_path.is_file():
            # 需要创建Model文件
            with model_path.open('w') as f:
                f.write(from_model_tpl(PACKAGE_ROOT, modelname, tablename, mysql_dict, table_comment))
            print('Created: ' + str(model_path))
        # 判断Mapper文件是否存在
        mapper_path = MAPPER_PATH / f'{modelname}Mapper.java'
        if not mapper_path.is_file():
            # 需要创建Mapper文件
            with mapper_path.open('w') as f:
                f.write(from_mapper_tpl(PACKAGE_ROOT, modelname))
            print('Created: ' + str(mapper_path))
        elif need_create_xml(mapper_path.open().read()):
            xml_path = MAPPERXML_PATH / f'{modelname}Mapper.xml'
            if not xml_path.is_file():
                # 需要创建MapperXml文件
                MAPPERXML_PATH.mkdir(parents=True, exist_ok=True)
                with xml_path.open('w') as f:
                    f.write(from_mapper_xml_tpl(PACKAGE_ROOT, modelname))
                print('Created: ' + str(xml_path))


def need_create_xml(mapper_content):
    return '@Mapper' in mapper_content and ';' in mapper_content.split('@Mapper', 1)[-1]


def parse_model_tablename(content: str) -> str:
    """
    :param content: Java的实体类代码内容
    :return: tablename
    """
    content = ' '.join(content.splitlines())
    match_ret = re.match(r'.*@Table\(name *= *"(.*?)"\)', content)
    tablename = match_ret and match_ret.group(1)
    return tablename


def java_comment_in_swagger(source: str):
    tmp = re.findall(r'@ApiModelProperty\(value *= *"(.*?)"\)', source)
    return tmp[0] if tmp else ''


def parse_model(content: str) -> Dict[str, Tuple[str, str]]:
    """
    :param content: Java的实体类代码内容
    :return: {name: (java_type, comment)}
    """
    java_dict: Dict[str, Tuple[str, str]] = {}
    content = ' '.join(content.splitlines())
    content = content.split(' public class ', 1)[-1]
    at_tokens = re.findall(r'@.*?[;{]', content)
    for at_token in at_tokens:
        at_token: str
        if at_token.endswith(';') and '@Transient' not in at_token:
            java_type, name = at_token.strip(';').strip().split()[-2:]
            comment = java_comment_in_swagger(at_token)
            java_dict[name] = (java_type, comment)

    return java_dict


def parse_table_comment(db_session, tablename: str) -> str:
    """
    :param db_session: 数据库session
    :return: table_comment
    """
    table_schema = db_session.execute(f'show create table {tablename}').fetchone()[1]
    last_line = table_schema.splitlines()[-1]
    return last_line.split(" COMMENT='", 1)[-1].rsplit("'", 1)[0] if ' COMMENT=' in last_line else ''


def parse_table(db_session, tablename: str) -> Dict[str, Tuple[str, str]]:
    """
    :param db_session: 数据库session
    :return: {name: (sql_type, comment)}
    """
    mysql_dict: Dict[str, Tuple[str, str]] = {}
    table_schema = db_session.execute(f'show create table {tablename}').fetchone()[1]
    for line in table_schema.splitlines():
        matched = re.match(r'`(.+?)` +([^ (]+)', line.strip())
        if matched is not None:
            comment = line.split(" COMMENT '", 1)[-1].rsplit("'", 1)[0] if ' COMMENT ' in line else ''
            name, sql_type = matched.groups()
            mysql_dict[name] = (sql_type, comment)

    return mysql_dict


def compare_model_and_table(java_dict, mysql_dict, tablename) -> List[str]:
    """
    :param java_dict: parse_model()的结果
    :param mysql_dict:  parse_table()的结果
    :return: 错误日志的数组
    """
    error_logs: List[str] = []
    for name, (java_type, java_comment) in java_dict.items():
        if not name in mysql_dict:
            error_logs.append(f'{tablename}表缺失{name}字段：{java_comment}')
            continue
        sql_type, sql_comment = mysql_dict[name]
        sql_type = sql_type.lower()
        if (java_type in ['Integer', 'Boolean', 'Long'] and not 'int' in sql_type) or \
                (java_type in ['String'] and not sql_type in ['varchar', 'char', 'text']) or \
                (java_type in ['JSONObject', 'JSONArray'] and not sql_type in ['json']):
            error_logs.append(f'{tablename}.{name}字段类型不兼容：{sql_type} <=> {java_type}')
        elif java_comment.strip() != sql_comment.strip():
            error_logs.append(f'{tablename}.{name}字段注释有差异：{sql_comment} <=> {java_comment}')

    for name, (_, sql_comment) in mysql_dict.items():
        if not name in java_dict:
            error_logs.append(f'{tablename}表的{name}字段在Model中缺失：{sql_comment}')

    return error_logs


def do_create_controller(role, model):
    model = camelize(model, upper=True)
    if model not in model_comment_map:
        print(f'Model:{model}不存在!')
        return
    table_comment = model_comment_map[model]
    data = {}
    data['PACKAGE_ROOT'] = PACKAGE_ROOT
    data['modelname'] = model
    data['modelname_lower'] = camelize(model, upper=False)
    data['table_comment'] = table_comment
    role = role or ''
    if role:
        data['ROLE_PATH'] = camelize(role, upper=False) + '/'
        data['ROLE_IN_PKG'] = '.' + camelize(role, upper=False)
    else:
        data['ROLE_PATH'] = data['ROLE_IN_PKG'] = ''
    data['ROLE_IN_VAR'] = camelize(role, upper=True)
    text = open('.arms/controller.tpl').read()
    path = CONTROLLER_PATH
    if role:
        path = CONTROLLER_PATH / role
        path.mkdir(parents=True, exist_ok=True)
    path = path / f'{model}{data["ROLE_IN_VAR"]}Controller.java'
    with path.open('w') as f:
        f.write(ArmsTpl(text).render(**data))
    print('Created: ' + str(path))


def do_spring_tool(role: str=None, model: str=None):
    """
    spring代码校验工具

    需先修改.arms-config.json中的数据库设置
    功能1：排查代码风险和生成模版代码
    直接运行arms spring

    功能2：排查代码风险，然后生成controller模版代码
    例如运行arms spring --model=Staff --role=mgr 或 arms spring --model=Staff

    """
    error_logs = []
    config = load_config()
    mysql_conf = config['MYSQL']
    database_init(
        username=mysql_conf['USERNAME'], password=mysql_conf['PASSWORD'],
        host=mysql_conf['HOST'], port=mysql_conf['PORT'],
        database=mysql_conf['DATABASE']
    )
    with make_session() as session:
        for filepath in MODEL_PATH.iterdir():
            model_content = filepath.open().read()
            tablename = parse_model_tablename(model_content)
            assert tablename, filepath
            java_dict = parse_model(model_content)
            mysql_dict = parse_table(session, tablename)
            error_logs.extend(compare_model_and_table(java_dict, mysql_dict, tablename))
        touch_models(session)

    for error_log in error_logs:
        print(error_log)

    if model is not None:
        do_create_controller(role, model)
