"""
@project: TeachClass
@author : Go_Fight_Now(WangSen)
@file   : dailySentence.py
@time   : 2019/12/31 10:40
@docs   : https://docs.python.org/zh-cn/3/
"""
"""
属性名	    属性值类型	说明
sid	        string	    每日一句ID	
tts	        string	    音频地址	
content	    string	    英文内容	
note	    string	    中文内容	
love	    string	    每日一句喜欢个数	
translation	string	    词霸小编	
picture	    string	    图片地址	
picture2	string	    大图片地址	
caption	    string	    标题	
dateline	string	    时间	
s_pv	    string	    浏览数	
sp_pv	    string	    语音评测浏览数	
tags	    array	    相关标签	
fenxiang_img string	    合成图片，建议分享微博用的
"""
import urllib.request, json, threading, os, pickle, time


class Iciba:
    log_path = os.path.dirname(__file__) + os.path.sep + "fight_day_log.pkl"
    _instance_lock = threading.Lock()
    dailySentence = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(Iciba, "_instance"):
            with Iciba._instance_lock:
                if not hasattr(Iciba, "_instance"):
                    Iciba._instance = super().__new__(cls)
        return Iciba._instance

    def __init__(self, date="", type="") -> None:
        self.__get_iciba_everyday(date, type)

    def __get_iciba_everyday(self, date="", type="") -> dict:
        """请求并返回所有内容"""
        url = "http://open.iciba.com/dsapi/"
        data = urllib.parse.urlencode({'date': date, 'type': type}).encode('utf-8')
        fileOk = False
        if os.path.exists(self.log_path):
            at_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            file_create_time = time.strftime('%Y-%m-%d', time.localtime(os.path.getctime(self.log_path)))
            if at_time == file_create_time:
                fileOk = True

        if fileOk:
            with open(self.log_path, 'rb') as pickle_file:
                self.dailySentence = pickle.load(pickle_file)
        else:
            try:
                self.dailySentence = json.loads(urllib.request.urlopen(url, data=data).read().decode('utf-8'))
                with open(self.log_path, 'wb') as pickle_file:
                    pickle.dump(self.dailySentence, pickle_file)
            except:
                self.dailySentence = {'content': "网络错误", 'note': "请检查您的网络之后重试"}

    def get_content_en_zh(self) -> tuple:
        """返回tuple(英文，中文)"""
        return self.dailySentence.get('content'), self.dailySentence.get('note')

    def get_translation(self):
        """返回小编的话"""
        translation = self.dailySentence.get('translation')
        return "" if translation == '新版每日一句' else translation

    def get_pic(self) -> tuple:
        """返回tuple(小图片，大图片)"""
        return self.dailySentence.get('picture'), self.dailySentence.get('picture2')

    def get_sid_tts_dateline(self) -> dict:
        """返回Id(sid)，音频(tts)，日期(dateline)"""
        dic = {'sid': self.dailySentence.get('sid'),
               'tts': self.dailySentence.get('tts'),
               'dateline': self.dailySentence.get('dateline')}
        return dic
