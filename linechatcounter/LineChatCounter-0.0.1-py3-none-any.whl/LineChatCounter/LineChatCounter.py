import re

class LineChatCounter():
    
    fileText = ""
    def __init__(self, LineChatFileText):
        self.fileText = LineChatFileText

    def total(self):
        arr = re.findall(r"[0-9]+:[0-9]+\s", self.fileText)
        return len(arr)

    def sticker(self):
        arr = re.findall(r"\(.+\)|\[貼圖\]", self.fileText)
        arr2 = re.findall(r"[0-9]+:[0-9]+\s", self.fileText)
        return len(arr),round(len(arr)/len(arr2),4)

    def photo(self):
        arr = re.findall(r"\(.+\)|\[照片\]", self.fileText)
        arr2 = re.findall(r"[0-9]+:[0-9]+\s", self.fileText)
        return len(arr),round(len(arr)/len(arr2),4)

    def search(self, regex):
        arr = re.findall(regex, self.fileText)
        arr2 = re.findall(r"[0-9]+:[0-9]+\s", self.fileText)
        return len(arr),round(len(arr)/len(arr2),6) 

    def user(self, username):
        arr = re.findall(r"[0-9]+:[0-9]+\s" + username, self.fileText)
        arr2 = re.findall(r"[0-9]+:[0-9]+\s", self.fileText)
        return len(arr),round(len(arr)/len(arr2),6) 

    def AllChatUser(self):
        print("測試中功能")
        arr = re.findall(r"[0-9]+:[0-9]+\t(.+)\t+", self.fileText)
        arr = list(set(arr))
        #arr.sort(key=lambda item: (len(item), item))
        return arr