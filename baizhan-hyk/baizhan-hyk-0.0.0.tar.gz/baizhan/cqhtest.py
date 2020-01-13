#coding=utf-8
import os
import shutil

def copyAllFiles(path):   #递归拷贝所有文件
    childFiles = os.listdir(path)   #获取所有文件
    for file in childFiles:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            copyAllFiles(filepath)
        elif filepath.endswith(".max"):  #给max文件改名
            shutil.copyfile(filepath, output + "/" + child_dir.split("/")[-1] + ".max")
        else:
            shutil.copyfile(filepath, output + "/" + file)

dir_input = "D:/cqh_input/"     #定义输入目录
dir_output = "D:/cqh_output/"     #定义输出目录
child_input = os.listdir(dir_input)    #获取输入目录的子目录

for child_dir in child_input: #
    output = dir_output + child_dir.split("/")[-1]    #准备创建输出目录的文件夹
#    print(dir_output)
    if not os.path.exists(output):#判断文件夹是否存在，不存在就创建
        os.makedirs(output)
    filepath = os.path.join(dir_input, child_dir)
    print(filepath)
    if os.path.isdir(filepath):#判断路径是否为文件夹，如果是文件夹就执行拷贝所有文件的方法
        copyAllFiles(filepath)








