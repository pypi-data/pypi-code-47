import os,textgrid,re,chardet

class SFTextGrid:
    def __init__(self,filepath = None):
        dir(textgrid)
        if filepath:
            if not os.path.isfile(filepath):
                raise FileNotFoundError('文件{}不存在'.format(filepath))
            else:
                self.textgrid_content = self.load(filepath)
                self.textgrid_path = filepath
    @staticmethod
    def help():
        print("""
        ------------------SFTextGrid类 使用方法-----------------------------------------
        from kog_lib.textgrid import sf_textgrid\n
        类实例化
            方式1: 
                my_tg = sf_textgrid.SFTextGrid() 
                my_tg.load(path)
            方式2: 
                my_tg = sf_textgrid.SFTextGrid(path)\n
        获取有效时长等信息：
            : t_file, t_effect, t_invalid, n_invalid = 
                            my_tg.get_textgrid_stat(re_str)  # re_str是正则表达式
            : 返回， 总时长、有效时长、无效时长、无效个数\n
        修改textgrid中相关内容
            : my_tg.sup_interval(item_ind,interval_ind,type,sup_str)
                item_ind: item的序号, 0 或者 1
                ind_ininterval_indterval:interval的序号，从1开始
                type: 修改interval的哪个字段,maxtime、mintime、mark
                sup_str:修改成sup_str
        -------------------------------------------------------------------------------
        """)

    def load(self,filepath):
        tg = textgrid.TextGrid()
        self.textgrid_path = filepath
        try:
            tg.read(filepath)
        except:
            self.__convert2UTF8()
            self.__restructuretextgrid()
            # raise IOError('文件{}读取失败'.format(filepath))
        finally:
            tg.read(filepath)
            self.textgrid_content = tg
            return tg

    def get_textgrid_stat(self,re_str):
        if not self.textgrid_content:
            raise ValueError('尚未读取TextGrid文件')
        return self.__get_textgrid_stat(re_str,self.textgrid_content)

    def sup_interval(self,item_ind,interval_ind,type,sup_str):
        if not self.textgrid_content:
            raise ValueError('尚未读取TextGrid文件')
        self.__sup_interval(item_ind,interval_ind,type,sup_str)

    def check(self):
        for item in self.textgrid_content.tiers:
            if item.minTime != self.textgrid_content.minTime or item.maxTime != self.textgrid_content.maxTime:
                errinfo = f'{item}时间区域和文件{file}不相等'
                # print(errinfo)
                return False,errinfo
            minTime = item.minTime
            for ind, interv in enumerate(item, 1):
                if ind == 1:
                    if interv.minTime != item.minTime:
                        errinfo = f'{interv.mark}的开始时间和{item.name}的开始时间不符'
                        # print(errinfo)
                        return False,errinfo
                # 如果这个Interval的最小值和上一个最小值相等，pass
                # 否则报错
                if ind == len(item):
                    if interv.maxTime != item.maxTime:
                        errinfo = f'{interv.mark}的结束时间和{item.name}的结束时间不符'
                        # print(errinfo)
                        return False,errinfo
        return True,""

    def __convert2UTF8(self):
        try:
            with open(self.textgrid_path,'rb') as fc:
                data = fc.read()
            filecode = chardet.detect(data)
            filecode = filecode['encoding']
            with open(self.textgrid_path, 'r', encoding = filecode) as fr:
                new_content = fr.read()
            data = new_content
            if self.has_bom(new_content):
                data = self.clean_bom(new_content)
            with open(self.textgrid_path, 'w', encoding = 'UTF-8') as fw:
                fw.write(data)
            print("convert from",filecode,"to UTF-8:",self.textgrid_path)
        except IOError as err:
            print("I/O error: {0}".format(err))

    @staticmethod
    def has_bom(text):
        if text.startswith(u'\ufeff'):
            return True
        return False

    @staticmethod
    def clean_bom(text):
        return text.encode('utf8')[3:].decode('utf8')

    def __restructuretextgrid(self):
        print("restruct",self.textgrid_path)
        lines = self.get_file_lines(self.textgrid_path)
        # 将textgrid内容去除所有空行 以及所有缩进
        # 将所有xmin、xmax、等需要缩进的行增加缩进
        intervalsize = []
        count = 0
        for ind,line in enumerate(lines):
            if "xmin" in line or "xmax" in line or "text" in line:
                lines[ind] = ' '*12+line
            if "intervals [" in line or "intervals:" in line or "name =" in line or ("class = " in line and "Object" not in line):
                lines[ind] = ' '*8+line
            if "item [" in line and "item []" not in line:
                lines[ind] = ' '*4+line
            if "intervals:" in line:
                intervalsize.append(int(line[line.rfind('=',0)+1:].strip()))
            if len(line.strip()) == 0:
                del lines[ind]
        # 第三行加一个空行
        lines.insert(2, '')
        # textgrid和item的 xmax xmin 缩进与intervals不同，逐一修改
        lines[3] = lines[3].strip()
        lines[4] = lines[4].strip()
        lines[11] = ' '*8+lines[11].strip()
        lines[12] = ' '*8+lines[12].strip()
        intervalsize.pop()
        for x in intervalsize:
            lines[12+4*x+6] = ' '*8+lines[12+4*x+6].strip()
            lines[12+4*x+7] = ' '*8+lines[12+4*x+7].strip()

        # 在操作的文件夹上一级，创建restructfiles文件夹，写入调整了格式的textgrid文件 
        # basefolder,filename = os.path.split(self.textgrid_path)
        # basefolder,folder = os.path.split(basefolder)
        # restrucfilefolder = os.path.join(basefolder,'restructfiles')
        # if not os.path.exists(restrucfilefolder):
        #     os.mkdir(restrucfilefolder)
        
        # restructfilespath = os.path.join(restrucfilefolder,filename)
        self.write_lines(self.textgrid_path,lines)
        # print_with_color(f"restruct {filename}, and saved as {restructfilespath}",'green')
        # 返回重新生成的textgrid路径
        return restructfilespath

    def write_lines(self,file_path,lines):
        with open(file_path, "w", encoding="utf-8") as f:
            con = "\n".join(lines)
            con += "\n"
            f.write(con)

    def get_file_lines(self,file):
        new_lines = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                # print(88)
                new_lines.append(line.strip())
        return new_lines

    def __sup_interval(self,item_ind,interval_ind,type,sup_str):
        try:
            tg = self.textgrid_content
            if type == "mark":
                tg.tiers[item_ind][interval_ind-1].mark = sup_str
            elif type == "maxTime":
                tg.tiers[item_ind][interval_ind-1].maxTime = sup_str
            elif type == "minTime":
                tg.tiers[item_ind][interval_ind-1].minTime = sup_str
            else:
                print("type error:",type)
                return False
            tg.write(self.textgrid_path)
            return True
        except Exception as e:
                print("error:",e)
                return False

    def __get_textgrid_stat(self,re_str,tg_content):
        t_invalid = 0  # 无效时长
        n_invalid = 0  # 无效的Interval的个数
        t_effect = 0
        t_file = tg_content.maxTime - tg_content.minTime
        for interv in tg_content.tiers[0]:
            # 等于空， 或者 (即匹配不到中文，也匹配不到大写
            if re.search(re_str, interv.mark):
                t_effect += interv.duration()
            else:
                n_invalid += 1
                t_invalid += interv.duration()
        # 文件总时长 有效时长  无效时长  无效个数
        return t_file, t_effect, t_invalid, n_invalid

