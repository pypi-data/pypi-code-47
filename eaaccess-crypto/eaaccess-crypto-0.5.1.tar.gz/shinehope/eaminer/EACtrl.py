from datetime import datetime

class EACtrl:
    command:int = 0             # 0 --> 無指示; 11 --> 停止運作, 即將重開機 ; 21 --> 手動平倉
    data:str = ""               # "" ==> 無其它指示;  "zzzzzz" ==> 總倉平倉;  若是其它值(MT4#) 則為單倉平倉
    timestamp:int = 0   # 命令發出時的時間戳

    def __init__(self):
        dTime = datetime.now()
        timestamp = int(dTime.timestamp())