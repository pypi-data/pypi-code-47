import configparser
from jinja2 import Template

conf = configparser.ConfigParser()
# 用config对象读取配置文件
conf.read("base.config.ini")
sections = conf.sections()
dit = {}


def analyze_ini():
    '''
    分析ini配置文件读取的数据，放到dit里面
    :return:
    '''
    for classname in sections:
        print(classname, conf.items(classname))
        classnamelist = classname.split('.')
        while classnamelist:
            subcl = '_'.join(classnamelist)
            subcl_pop = classnamelist.pop()
            baseclassname = '_'.join(classnamelist)
            if baseclassname == '':
                baseclassname = 'conf'
            key = dit.get(baseclassname)
            if key:
                if key.get('subclass'):
                    key['subclass'].update({subcl_pop: subcl})
                else:
                    key['subclass'] = {subcl_pop: subcl}
            else:
                dit[baseclassname] = {'subclass': {subcl_pop: subcl}}

            subkey = dit.get(subcl)
            if subkey is None:  # 不存在
                dit[subcl] = {'subclass': {}, 'args': []}

        classnamelast = classname.replace('.', '_')
        # print(classnamelast)
        dit[classnamelast]['args'] = conf.items(classname)


def analyze_subclass():
    '''
    分析子类继承关系，修改dit的内容
    :return:
    '''
    for k in dit.keys():
        for name, value in dit.items():
            args = value.get('args')
            if args:
                for argtuple in value['args']:
                    nickname = f'{name}_{argtuple[0]}'
                    if nickname == k:
                        dit[k]['string'] = argtuple[1]
                        value['args'].remove(argtuple)
            else:
                value['args'] = []


t_demo = '''
class _{{class}}:{% for k,v in subclass.items() %}
    {{k}} = _{{v}}(){% endfor %}{% for arg,value in args %}
    {{arg}} = "{{value}}"{% endfor %}
    {% if string %}
    def __str__(self):
        return "{{ string }}"{% endif %}

'''
html = '# -*- coding:utf-8 -*-'
t = Template(t_demo)


def get_subclass(classname, body):
    '''
    获取subclass的数据，拼接html
    :param classname:
    :param body:
    :return:
    '''
    global html
    subclass = body.get('subclass')
    if subclass:
        for subname in subclass.values():
            get_subclass(subname, dit[subname])
    result = {'class': classname, **body}
    html = html + t.render(result)


def build(a):
    '''
    获取分析的类关系，然后生成html
    :param a:
    :return:
    '''
    body = a.get('conf')
    get_subclass('conf', body)
    print(html)
    with open('./config.py', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    analyze_ini()
    analyze_subclass()
    build(dit)
