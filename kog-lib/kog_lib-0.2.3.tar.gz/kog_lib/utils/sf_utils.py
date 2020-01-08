import os,shutil,re,math
import Levenshtein as lvst
from collections import Counter
from pprint import pprint

class SFUtils:
    @staticmethod
    def help():
        print("""
        ------------------SFUtil类 使用介绍-----------------------------------------
        import kog_lib\n
        按行读文件：
            kog_lib.SFUtils.get_file_lines(path)\n
        按行读文件并去重：
            kog_lib.SFUtils.get_uniq_lines_from_file(path)\n
        列表去重：
            kog_lib.SFUtils.uniq_lines(lines)\n
        列表写入文件：
            kog_lib.SFUtils.write_lines(filepath,lines)\n
        行（字符串）切割，并清洗：
            kog_lib.SFUtils.split_clean_line(line,split_char,begin_re,end_re,clean_chinese)
                line:要切割的字符串
                split_char:以这个字符切分
                begin_re: 清洗字符串line头部的正则，默认 儿童英语项目的正则
                end_re: 清洗字符串line尾部的正则，默认 儿童英语项目的正则
                clean_chinese: 是否清除汉字，默认 清除汉字\n
        根据正则表达式re_str清洗某行：
            kog_lib.SFUtils.clean_line(line,re_str)\n
        根据正则表达式re_str按行清洗某列表：
            kog_lib.SFUtils.clean_lines(lines,re_str)\n
        根据正则表达式re_str按行清洗某列表，返回列表元素是(新行，原行)的元组：
            kog_lib.SFUtils.clean_lines_map_list(line,re_str)\n
        比较两个list，返回A中不再B的元素：
            kog_lib.SFUtils.diff_list(A,B)\n
        以空格区分，返回某行的词数：
            kog_lib.SFUtils.get_wordcount_from_line(line)\n
        以空格区分，返回某列表次数：
            kog_lib.SFUtils.get_wordcount_from_line(lines)\n
        对列表lines分组，每组requaired_lines行，返回组列表的列表：
            kog_lib.SFUtils.lines_split_2_sublines(lines,requaired_lines)\n
        获取str1到str2的编辑距离：
            kog_lib.SFUtils.get_edit_distance(str1,str2)\n
        获取str1到str2的编辑步骤：
            kog_lib.SFUtils.get_edit_ops(str1,str2)\n
        打印str1转换到str2的详细步骤：
            kog_lib.SFUtils.print_edit_ops(str1,str2)\n
        打印列表：
            kog_lib.SFUtils.print_lines(lines)\n
        打印字典：
            kog_lib.SFUtils.print_dict(dict)\n
        批量重命名：
            kog_lib.SFUtils.modify_name(path,prefix="",suffix="",mode="add",deep=False)
                path: 修改path路径下文件和文件夹的名称，不含path
                prefix: 要加的前缀
                suffix: 要加的后缀
                mode: 模式，add/minus
                deep: True：深度重命名（遍历path下文件及文件夹）
                      False：仅对path下文件和文件夹进行重命名
        -------------------------------------------------------------------------------
        """)

    @staticmethod
    def get_file_lines(file):
        new_lines = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                new_lines.append(line.strip())
        return new_lines

    @staticmethod
    def get_uniq_lines_from_file(file):
        new_lines = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                new_line = line.strip()
                if new_line not in new_lines:
                    new_lines.append(new_line)
        return new_lines

    @staticmethod
    def uniq_lines(lines):
        new_lines = []
        for line in lines:
            new_line = line.strip()
            if new_line not in new_lines:
                new_lines.append(new_line)
        return new_lines    
    
    @staticmethod
    def write_lines(file_path: str, lines: list):
        with open(file_path, "w", encoding="utf-8") as f:
            con = "\n".join(lines)
            f.write(con)

    @staticmethod
    def split_clean_line(line, split_char,begin_re=None,end_re=None,clean_chinese=True):
        """
        通过给定的字符切割一行为多行，并新行进行清洗
        :param line:
        :param split_char:
        :return:
        """
        lines = []
        sublines = [s for s in line.split(split_char) if len(s.strip()) > 0]
        if not len(sublines) > 0:
            return lines

        for l in sublines:
            new_line = LineCleaner(l)
            if begin_re:
                new_line.set_begin_re(begin_re)
            if end_re:
                new_line.set_end_re(end_re)
            new_line.clean_line(clean_chinese)
            new_line = new_line.line  # 进行清洗行内容
            if len(new_line) > 0:  # 清除空行
                lines.append("{line}{char}".format(line=new_line, char=split_char))

        # 如果行不是一切割的符号结尾，需要去掉末尾的符号
        if not line.endswith(split_char):
            line_len = len(lines)
            lines[line_len - 1] = lines[line_len - 1][:-1]

        return lines

    @staticmethod
    def clean_line(line,re_str):
        return re.sub("\s+"," ",re.sub(re_str," ",line))

    @staticmethod
    def clean_lines_map_list(lines,re_str):
        new_lines = []
        for line in lines:
            clean_line = SFUtils.clean_line(line,re_str)
            if len(clean_line.strip())>0:
                new_lines.append([clean_line,line]) # 方便还原
        return new_lines

    @staticmethod
    def clean_lines(lines,re_str):
        new_lines = []
        for line in lines:
            clean_line = SFUtils.clean_line(line,re_str)
            if len(clean_line.strip()) > 0:
                new_lines.append(clean_line) 
        return new_lines     

    @staticmethod
    def diff_list(a_list, b_list):
        new_list = []
        for a in a_list:
            if a not in b_list:
                new_list.append(a)
        return new_list  
    
    @staticmethod
    def get_wordcount_from_line(line):
        return len(line.strip().split(" "))
    
    @staticmethod
    def get_wordcount_from_lines(lines):
        count = 0
        for line in lines:
            count += SFUtils.get_wordcount_from_line(line)
        return count

    @staticmethod
    def lines_split_2_sublines(lines,requaired_lines):
        sublines_list = []
        tmplist=[]
        left_lines=[]
        process_lines = lines.copy()
        countsublines = math.ceil(len(process_lines)/requaired_lines)
        for i in range(countsublines):
            countph=0
            if len(process_lines) < requaired_lines:
                # 剩余的句子不足写成一个SCR文件时，将剩余的句子计入left_lines返回，同时返回写入了几个SCR
                left_lines=process_lines.copy()
                writenfiles = i
                break
            # 将要写入SCR的句子先计入tmplist
            for j in process_lines:
                if countph < requaired_lines:
                    tmplist.append(j)
                    countph +=1
                else:
                    break
            # 删除lines中templist含有的line
            for k in tmplist:
                process_lines.remove(k)
            
            sublines_list.append(tmplist)
            tmplist = []
        sublines_list.append(left_lines)
        return sublines_list
     
    @staticmethod
    def get_edit_ops(str1,str2):
        return lvst.editops(str1,str2)
    
    @staticmethod
    def get_edit_distance(str1,str2):
        return lvst.distance(str1,str2)
    
    @staticmethod
    def print_lines(lines):
        for line in lines:
            print(line)
    
    def print_dict(adict):
        for key in adict.keys():
            print(key," : ",adict[key])
            

    @staticmethod
    def print_edit_ops(str1,str2):
        print(str1,"<CONVERT-TO>",str2)
        print("  相似的：",str(lvst.ratio(str1,str2)))
        print("  编辑步骤：")
        editops = lvst.editops(str1,str2)
        # editopsstr = ""
        # for step in editops:
        #     temp = "        "
        #     for item in step:
        #         temp += str(item)+","
        #     editopsstr += ("->"+temp+"\n")
        # print(editopsstr)
        for ind in range(len(editops)):
            print("    ",editops[ind],":",lvst.apply_edit(editops[:ind+1],str1,str2))

    @staticmethod
    def modify_name(path,prefix="",suffix="",mode="add",deep=False):
        """
        批量增减path下 子目录名，不递归
        """
        def check_minus(file,prefix,suffix):
            # 文件或目录是否可以进行减的操作
            if not file.startswith(prefix):
                print(file,"不是以",prefix,"开头")
                return False
            if not file.endswith(suffix):
                print(file,"不是以",suffix,"结尾")
                return False
            return True
        def rename(root,old_name,prefix,suffix,mode):
            # 文件重命名
            if mode == "add":
                new_name = prefix + old_name + suffix
            if mode == "minus":
                if len(suffix) == 0:
                    new_name = old_name[len(prefix):]
                else:
                    new_name = old_name[len(prefix):-len(suffix)]
            
            new_path = os.path.join(root,new_name)
            old_path = os.path.join(root,old_name)
            os.rename(old_path,new_path)
            print(old_path,"  ->\n      ",new_path)

        if mode not in ["add","minus"]:
            # 模式是否正确
            print("mode error")
            return
        for root,dirs,files in os.walk(path):
            # 检测是否可进行减操作
            if mode == "minus":
                for file in files:
                    if not check_minus(file,prefix,suffix):
                        return
                for folder in dirs:
                    if not check_minus(folder,prefix,suffix):
                        return
        if not deep:
            for f in os.listdir(path):
                rename(path,f,prefix,suffix,mode)
            return
        all_folder = []
        for root,dirs,files in os.walk(path):
            # 重命名文件
            all_folder.append(root)
            for file in files:
                print(file)
                rename(root,file,prefix,suffix,mode)

        all_folder.reverse()
        all_folder.pop()
        for folder in all_folder:
            # 重命名目录
            folder_name = os.path.basename(folder)
            folder_root = os.path.dirname(folder)
            rename(folder_root,folder_name,prefix,suffix,mode)

class LineCleaner:
    """
    针对少儿英语项目原料数据。清理得出可用的一行语料
    """

    def __init__(self, line: str):
        self.line = line
        # 默认针对少儿英语项目原料数据。清理得出可用的一行语料
        self.begin_re = "^[^a-zA-Z]+"
        self.end_re = "[^a-zA-Z\?\.!]+$"  

    def set_begin_re(self,begin_re):
        self.begin_re = begin_re
    
    def set_end_re(self,end_re):
        self.end_re = end_re

    def show_current_re(self):
        print("begin_re:",self.begin_re)
        print("end_re:",self.end_re)

    def clean_line(self,clean_chinese=True):
        """
        清理一行
        :return:
        """
        # 0. 多个空白行合成一个
        self._merge_multi_space_2_one()

        # 1. 清理行首部，清理4数字，符号的#特殊字符
        self._clean_line_begin()

        # 2. 清理行末尾，清理数字，符号的特殊字符
        self._clean_line_end()

        # 3. 清理行内容中的中文
        if clean_chinese:
            self._clean_Chinese()

        # 4. 清除乱码
        self.to_utf8()

        # 5. 清理前后空格
        self.line = self.line.strip()

    def _merge_multi_space_2_one(self):
        """
        多个空白合并一个
        :return:
        """
        self.line = re.sub("\s+", ' ', self.line)

    def _clean_line_begin(self):
        """
        非英文开头的行去掉首部的特殊字符
        :return:
        """
        self.line = re.sub(self.begin_re, " ", self.line)

    def _clean_line_end(self):
        """
        清理行末尾，清理数字，符号的特殊字符
        :return:
        """
        self.line = re.sub(self.end_re, ' ', self.line)

    def _clean_Chinese(self):
        """
        清理行末尾，清理数字，符号的特殊字符
        :return:
        """
        self.line = re.sub("[\u4e00-\u9fa5]+", ' ', self.line)

    def to_utf8(self):
        """
        1. 转码
        2. 清除乱码
        :return:
        """
        return self.line.encode('utf-8', 'ignore').decode('utf-8')

    def __len__(self):
        return len(self.line)

    def __str__(self):
        return self.line

    def __repr__(self):
        return str(self)


