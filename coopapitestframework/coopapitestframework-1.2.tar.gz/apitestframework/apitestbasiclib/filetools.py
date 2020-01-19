# coding:utf-8

import yaml
import os

def get_env_config(filepath,envname):
    '''
    【功能】从yaml文件中读取配置
    【参数】filepath：yaml文件的路径
            envname：读取的配置名称，如fat，sit等
    【返回】返回响应的配置信息，字典类型
    '''
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = curPath[:curPath.find("yamlapi\\")+len("yamlapi\\")]
    # file = open(rootPath+filepath,'r')
    file = open(filepath, 'r')
    file_data = file.read()
    file.close()
    result = yaml.load(file_data, Loader=yaml.FullLoader)
    return result[envname]

def get_testcases(filepath):
    '''
    【功能】从指定的yaml文件读取用例数据
    【参数】filepath：用例数据文件路径，函数自动获取项目根目录路径，然后和filepath拼接成完整路径
    【返回】返回yaml文件中的所有用例，列表类型
    '''
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # rootPath = curPath[:curPath.find("yamlapi\\")+len("yamlapi\\")]
    # print('rootpath=%s'%rootPath)
    # file = open(rootPath+filepath,'r',encoding='utf-8')
    file = open(filepath, 'r')
    file_data = file.read()
    file.close()
    result = yaml.load(file_data,Loader=yaml.FullLoader)
    return result
#==============================================================

if __name__=='__main__':
    config = get_env_config('/config/env_config.yaml','fat')
    print(config)
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("yamlapi\\")+len("yamlapi\\")]
    file = open(rootPath+'/testcases/testcase.yaml','r' ,encoding='utf-8')
    file_data = file.read()
    file.close()
    result = yaml.load(file_data, Loader=yaml.FullLoader)
    print(result)