# -*- coding: utf-8 -*-
# 对文件进行预处理
import requests
import tkitFile
import os

class Http:
    def __init__(self):
        pass #

    def download(self,url,name,dirname='tfiles'):
        """下载远程文件"""
        # url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
        r = requests.get(url)
        # 获取当前文件路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件的父目录
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        tfile=os.path.join(father_path,dirname)
        tkitFile.File().mkdir(tfile)  #创建文件夹
        path= os.path.join(tfile,name)
        with open(path, 'wb') as f:
            f.write(r.content)
        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        data ={"status_code":r.status_code,
                        "content-type":r.headers['content-type'],
                        'path':path,
                        'file':"tfiles/"+name
        }
        return data

th=Http()
url="https://files.pythonhosted.org/packages/64/f8/434a36c186aefada16735bc6d8b489fbeaa0144419cf2a5f15033d0d129a/tkitFile-0.0.1.2.tar.gz"
path="tkitFile-0.0.1.2.tar.gz"
data=th.download(url,path)
print(data)