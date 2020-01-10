# -*- coding: utf-8 -*-
from PyQt5.QtCore import QFile, QIODevice

resources = []


def read_file(path):
    for r in resources:
        if r['path'] == path:
            return r['value']
    file = QFile(path)
    isOK = file.open(QIODevice.ReadOnly)
    if isOK:
        qbr = file.readAll()
        file.close()
        resources.append({
            "path": path,
            "value": qbr
        })
        return qbr
    else:
        file.close()
        raise OSError("资源文件不存在：{}".format(path))


def read_str_file(path):
    return str(read_file(path), encoding="utf-8")
