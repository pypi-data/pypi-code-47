from typing import Dict
import os
from lesscli import Application
import re
import json
import random

from arms.utils.common import camelize, replace_all
from arms.ubuntu import ubuntu_entry
from arms.spring import do_spring_tool
from pathlib import Path

PY2 = (type(b'') == str)


def makedir(real_path):
    from pathlib import Path
    Path(real_path).mkdir(parents=True, exist_ok=True)


def print_help():
    text = """

    arms init -e                : setup CI/CD (-e for manual input environs)
    arms docker prune           : prune docker container/image/volume
    arms paste [format]         : change coped content into another format
    arms ubuntu                 : install requirements such as docker
    arms runner [domain]        : register gitlab-runner
    arms -h                     : show help information
    arms -v                     : show version


    """
    print(text)


def print_version():
    """
    显示版本
    """
    from arms import __version__
    text = """
    arms version: {}

    """.format(__version__)
    print(text)


def run_init():
    """
    项目初始化工具
    运行arms init后，按照提示输入，即可完成项目初始化。
    """
    # [1/6]判断本地有.git目录
    if not os.path.isdir('.git'):
        print('Please change workdir to top! or run "git init" first.')
        return
    # [2/6]加载index.json
    os.system('git clone http://gitlab.parsec.com.cn/qorzj/arms-tool.git .arms-tool')
    index_json = {}
    try:
        index_json.update(json.loads(open('.arms-tool/templates/index.json').read()))
    finally:
        os.system('rm -rf .arms-tool')
    # [3/6]生成env
    env: Dict[str, str] = {}
    # 获取top_opt
    opts = sorted(index_json.keys())
    top_opt = input('请选择(' + ','.join(opts) +')：')
    assert top_opt in opts
    index_json = index_json[top_opt]
    # 获取second_opt
    opts = sorted(index_json.keys())
    second_opt = input('请选择(' + ','.join(opts) +')：')
    assert second_opt in opts
    index_json = index_json[second_opt]
    for param in index_json['params']:
        name = param['name']
        if 'default' in param:  # 生成参数
            default_rules = param['default'].split()
            if default_rules[0] == '@rand-port':
                value = str(random.randint(10000, 59999))
            elif default_rules[0] == '@low-camel':
                value = camelize(env[default_rules[1]], upper=False)
            else:
                raise NotImplementedError('功能暂不支持!')
            env[name] = value
        else:  # 输入参数
            value = input('请输入%s：' % (param.get('description') or name))
            assert re.match('^' + param.get('valid-pattern', '.*') + '$', value) is not None
            env[name] = value
    print(env)
    # [4/7]拉取模版项目
    os.system('mv .git .git_arms_bak')
    os.system('git clone %s .arms_tpl' % index_json['git-template'])
    os.system('cd .arms_tpl && tar -czf ../.arms_tpl.tgz .')
    os.system('tar -zxf .arms_tpl.tgz && rm -f .arms_tpl.tgz && rm -rf .arms_tpl')
    os.system('rm -rf .git && mv .git_arms_bak .git')
    # [5/7]替换文件
    curpath = Path('.')
    for p in curpath.rglob('*'):
        if p.is_dir() or str(p).startswith(('.git/', '.idea/')):
            continue
        try:
            text = p.open().read()
            changed, new_text = replace_all(text, env)
            if changed:
                with p.open('w') as f:
                    f.write(new_text)
        except Exception as e:
            print(str(e) + ' ' + str(p))
    # [6/7]文件重命名
    for i in range(20):  # 最大循环20轮
        touched = False
        renames = []
        for p in curpath.rglob('*'):
            full_path = str(p)
            changed, new_path = replace_all(full_path, env)
            if changed:
                renames.append({'from': full_path, 'to': new_path})
        renames.extend(index_json.get('renames', []))
        for item in renames:
            from_path, to_path = item['from'], item['to']
            if Path(from_path).exists():  # 前面的重命名可能会影响后面的重命名
                os.rename(from_path, to_path)  # os.rename非常强大
                touched = True
        if not touched:  # 若一轮操作没有产生重命名则退出
            break
    # [7/7]git add
    os.system('git add *')
    os.system('git add .gitlab-ci.yml .gitignore')
    print('---- arms init succeed :) ----')


def entrypoint():
    if PY2:
        print('arms已不再支持python2，请安装python3.5+')
        exit(1)
    Application('armstrong')\
        .add('version', print_version)\
        .add('docker', ubuntu_entry())\
        .add('init', run_init)\
        .add('spring', do_spring_tool)\
        .run()
