import os,collections

class SFMetadata:
    def __init__(self):
        self.__metadata_dict = collections.OrderedDict()
        self.__init_metadata_dict()

    def __init_metadata_dict(self):
        self.__metadata_dict["LHD"] = ""
        self.__metadata_dict["DBN"] = ""
        self.__metadata_dict["SES"] = ""
        self.__metadata_dict["BLANK1"]=""
        self.__metadata_dict["SRC"] = ""
        self.__metadata_dict["DIR"] = ""
        self.__metadata_dict["LBN"] = ""
        self.__metadata_dict["CCD"] = ""
        self.__metadata_dict["BEG"] = ""
        self.__metadata_dict["END"] = ""
        self.__metadata_dict["REP"] = ""
        self.__metadata_dict["RED"] = ""
        self.__metadata_dict["RET"] = ""
        self.__metadata_dict["BLANK2"]=""
        self.__metadata_dict["SAM"] = ""
        self.__metadata_dict["SNB"] = ""
        self.__metadata_dict["SBF"] = ""
        self.__metadata_dict["SSB"] = ""
        self.__metadata_dict["QNT"] = ""
        self.__metadata_dict["NCH"] = ""
        self.__metadata_dict["BLANK3"]=""
        self.__metadata_dict["SCD"] = ""
        self.__metadata_dict["SEX"] = ""
        self.__metadata_dict["AGE"] = ""
        self.__metadata_dict["ACC"] = ""
        self.__metadata_dict["ACT"] = ""
        self.__metadata_dict["BIR"] = ""
        self.__metadata_dict["BLANK4"]=""
        self.__metadata_dict["MIP"] = ""
        self.__metadata_dict["MIT"] = ""
        self.__metadata_dict["SPP"] = ""
        self.__metadata_dict["SCC"] = ""
        self.__metadata_dict["BLANK5"]=""
        self.__metadata_dict["LBR"] = ""
        self.__metadata_dict["BLANK6"]=""

    def load_template(self,filepath):
        lines = self.__get_file_lines(filepath)
        self.__metadata_dict.clear()
        count = 0
        try:
            for line in lines:
                if line.strip() == "":
                    count += 1
                    key,value = "BLANK"+str(count),""
                elif " " not in line.strip():
                    key,value = line,""
                else:
                    key,value = line.split(" ",1)
                if key not in self.__metadata_dict.keys():
                    self.__metadata_dict[key] = value
                else:
                    self.__metadata_dict.clear()
                    self.__init_metadata_dict()
                    raise TypeError(f"{filepath}中有重复的key:{key}")
        except Exception as e:
            raise ValueError(f"{e}:{line}")
            raise ValueError(f"{filepath}模板内容有问题，无法区分key-value")


    def set_metadata_element(self, key, value):
        try:
            self.__metadata_dict[key] = value
        except Exception as e:
            raise ValueError(e)
        return True

    def get_metadata_element(self, key):
        if key in self.__metadata_dict:
            return self.__metadata_dict[key]
        else:
            raise ValueError(e)
    
    def make_metadata(self,output):
        if not output.endswith(".metadata"):
            print(f"文件后缀有误: {output}")
            return False
        write_list = []
        try:
            for key,value in self.__metadata_dict.items():
                if "BLANK" in key:
                    write_list.append("")
                    continue
                write_list.append(key+" "+value)
            self.__write_lines(output,write_list)
        except Exception as e:
            raise ValueError(e)
        return True

    def __get_file_lines(self,file_path):
        new_lines = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                new_lines.append(line.strip())
        return new_lines 
    
    def __write_lines(self,file_path, write_list, mode="w"):
        write_str = "\n".join(write_list)
        self.__write_file(file_path, write_str, mode=mode)

    def __write_file(self,file_path, write_str, mode="w"):
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(write_str + "\n")

    @staticmethod
    def help():
        print("""
        ------------SFMetadata类 使用方法---------------------------------------------
        import kog_lib\n
        实例化: 
            my_metadata = kog_lib.SFMetadata()
                此时会实例化一个默认的metadata模板\n
        导入metadata模板: 
            my_metadata.load_template(filepath)
                也可以读取现有的metadata文件作为模板\n
        修改metadata文件内容: 
            my_metadata.set_metadata_element(key,value)
                如: my_metadata.set_metadata_element("BIR","北美")\n
        获取metadata某个key的值: 
            my_metadata.get_metadata_element(key)
                如: value = my_metadata.get_metadata_element("BIR") # value="北美"\n
        生产metadata文件: 
            my_metadata.make_metadata(output)
                如: my_metadata.make_metadata("/data/xxxx.metadata")
        ----------------------------------------------------------------------------
        """)

    