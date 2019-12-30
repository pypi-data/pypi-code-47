import numpy as np
import csv

class Csv:
    """
    处理各种csv数据
    """
    def __init__(self):
        pass
    # def reader(self,file_path='')
    def csv_data(self,file_path='',label=True):
        """
        自定义读取csv 自动将数据转化成对象列表
        数据需要第一行定义label
        """
        with open(file_path,'r') as csvfile:
            reader = csv.reader(csvfile)
            # print(reader)
                # # 建立空字典
            result = []
            for item in reader:
                # print(item)
                # # 忽略第一行

                if label==True and reader.line_num == 1:
                    # continue
                    labs=item
                else:
                #    result[item[0]] = item[1]
                    data={}
                    for i,it in enumerate(item):
                        data[labs[i]]=it
                    result.append(data)
            return result