"""
    module(file_csv) - csv文件读写操作.

    Main members:

        # write_csv_file - 输出csv文件.
        # read_csv_file - 读取csv文件内容，列表形式返回.
        # read_csv_file_iter - 读取csv文件内容，迭代器形式返回.
"""
__all__ = [
    'write_csv_file',
    'read_csv_file',
    'read_csv_file_iter'
]

import codecs
import csv


def write_csv_file(file_name, titles, row_datas):
    """ 输出csv文件，需保证title与行的内容个数一致.

        @params:
            file_name - 文件名称.
            titles - 标题列表.
            row_datas - 每一行的数据，每个元素也是一个列表或者元组.
    """
    with codecs.open(file_name, mode='w', encoding='utf-8') as csvout:
        writer = csv.writer(csvout)
        # 写入表头
        writer.writerow(titles)
        for row_data in row_datas:
            writer.writerow(row_data)


def read_csv_file(file_name):
    """ 读取csv文件内容，列表形式返回.

        @params:
            file_name - 文件名.

        @return:
            On success - 返回每行数据的列表，列表元素为每行数据的字典形式.
    """
    with codecs.open(file_name, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        csv_datas = list()
        for row_data in reader:
            csv_datas.append(row_data)
        return csv_datas


def read_csv_file_iter(file_name):
    """ 读取csv文件内容，迭代器形式返回.

        @params:
            file_name - 文件名.

        @return:
            On success - 返回每行数据的迭代器，迭代器元素为每行数据的字典形式.
    """
    with codecs.open(file_name, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row_data in reader:
            yield row_data
