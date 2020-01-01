import os
import time
import pickle
import shutil
class Pkl:
    def __init__(self,path="tdata",task='data',plimit=10000000):
        """
        进程名字
        保存目录
        多少数据保存一次
        
        """
        self.path =path
        self.plimit =plimit
        self.task =task
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
    def clear(self):
        """
        删除指定进程的数据
        """
        # shutil.rmtree(os.path.join(self.path))
        # os.makedirs(os.path.join(self.path))
        for fname in self.file_list(self.path):
            if fname.find(self.task)>=0:
                print("删除",fname)
                os.remove(fname)


    def save(self,data):
        """保存数据,支持添加"""
        batch_data=[]
        for i,item in enumerate(data):
            batch_data.append(item)
            
            if i%self.plimit==0 and i!=0:
                self.save_batch(batch_data)
                batch_data=[]
        self.save_batch(batch_data)
        batch_data=[]

    def save_batch(self, batch_data):
        """保存一次片段"""
        with open(os.path.join(self.path,self.task+'_'+str(time.time())+'.pkl'), 'wb') as f:
            pickle.dump(batch_data, f)
    def load(self,max=10000):
        """
        加载所有保存的数据
        迭代输出
        如果数据过少会自动追加下一个片段数据
        """
        
        result =[]
        for fname in self.file_list(self.path):
            if fname.find(self.task)>=0:
                print("加载数据:",fname)
                data=self.load_plk(fname)
                # if len(data)<max:
                #     result=result+data
                # else:
                #     print(len(data))
                yield data


    def load_plk(self,fname):
        """加载一个plk文件"""
        with open(fname, 'rb') as f:
            return pickle.load(f)

    # 遍历目录文件夹
    def file_list(self, path, type='pkl'):
        """
        遍历目录文件夹
        支持潜逃目录
        >>> file_list('/home/','txt')
        """
        files = []
        
        for file in self.all_path(dirname = path):

            if file.endswith("." + type):
                # print(path+file)
                files.append(file)
        return files

    def all_path(self ,dirname):
        """遍历文件夹下的所有文件
        >>> all_path(dirname)
        """

        result = []#所有的文件
        for maindir, subdir, file_name_list in os.walk(dirname):

            # print("1:",maindir) #当前主目录
            # print("2:",subdir) #当前主目录下的所有目录
            # print("3:",file_name_list)  #当前主目录下的所有文件

            for filename in file_name_list:
                apath = os.path.join(maindir, filename)#合并成一个完整路径
                result.append(apath)

        return result
