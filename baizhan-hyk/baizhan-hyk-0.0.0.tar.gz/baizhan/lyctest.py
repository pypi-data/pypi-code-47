#coding = utf-8
#拷贝表格中对应的文件到，表格所在目录
import os
import csv
import shutil
input_dir = "C:/Users/Administrator/Desktop/demo/2D/"
csv_dir = "C:/Users/Administrator/Desktop/demo/机加/机加.csv"  #输入需要执行文件的位置
all_file = 0
succed_file = 0
exist_file = 0
failed_file = 0
failedname = []
with open(csv_dir,"r",encoding="utf-8") as f:
    filename_list = csv.reader(f)
    for name in filename_list:  #循环名单数
        out_dir = os.path.dirname(csv_dir)+"/"  #获取输出地址
        file_list = os.listdir(input_dir)  #获取输入文件地址
        all_file += 1
        notFound = True
        for filename in file_list:  #循环匹配输入文件
            if name[0] == filename.split(" "[0])[0]:
#            if str(name) in str(failedname):
                out_file = out_dir + filename
                if os.path.exists(out_file):
#                    print("{0}文件已存在".format(out_file))
                    exist_file += 1
                    notFound = False
                else:
                    shutil.copyfile(input_dir+filename,out_file)
#                    print("{0}拷贝成功".format(name))
                    succed_file += 1
                    notFound = False
        if notFound:
            failedname.append(name)
    print("总共执行{0}次，其中文件已存在{1}个文件，成功复制{2}个文件,失败的文件有：{3}"
          .format(all_file,exist_file,succed_file,failedname))
input()