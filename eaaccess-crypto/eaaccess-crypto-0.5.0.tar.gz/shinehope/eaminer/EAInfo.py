import  datetime

class EAInfo:
    account = 0            # MT4 交易帳號
    acc_type = ""          # "DEMO" ==> 模擬倉;  "LIVE" ==> 真倉   
    # 2019.09.19 改為 acc_type; type() 是 python 的 function 

    lots_opentrade = 0.0    #目前在倉量
    lots_today = 0.0         #今日截至目前已結單量
    lots_1dayago = 0.0       #1天前已結單量
    lots_2dayago = 0.0       #2天前已結單量
    lots_3dayago = 0.0       #3天前已結單量
    lots_4dayago = 0.0       #4天前已結單量
    lots_5dayago = 0.0       #5天前已結單量
    lots_6dayago = 0.0       #5天前已結單量
    date_today = ""          #今日日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    date_1dayago = ""        #1天前日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    date_2dayago = ""        #2天前日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    date_3dayago = ""        #3天前日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    date_4dayago = ""        #4天前日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    date_5dayago = ""        #5天前日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    date_6dayago = ""        #6天前日期, MT4 平台的日期, 格式為 yyyy.MM.dd
    lots_thisweek = 0.0      #本週截至目前的交易量, MT4 平台日期星期一起算, 含目前(今日)已結量
    lots_thismonth = 0.0     #本月截至目前的交易量, MT4 平台日期 01 日起算, 含目前(今日)已結量
    lots_total = 0.0         #交易帳號開始交易起至目前的交易量, 含目前在倉量
    start_balance = 0.0      #局起算的本金; 場上無單下第一張單時當時的 MT4 balance
    balance = 0.0            #MT4 上的 balance
    equity = 0.0             #MT4 上的 equity
    inout_money = 0.0        #交易帳號開始交易起, 進出的帳號 的入金量及出金量
    start_money = 0.0        #交易者自行指定的局起算本金
    reason = ""              #傳送資料的理由  "TimeUP" ==> 定時傳送資訊
    timestamp= 0             #資料產生的時間; 使用 Unix epoch time 
    alert_code = 0  # 0 --> 無 alert  ; 11 --> 止損 ;  21 --> 平倉 ; 901 --> 發生 EA Alert
    alert_time = 0  # 0 --> 無 alert  ; 記錄發生 alert 時的 timestamp (unix)
    alert_msg = ""  # EA Alert 訊息 ((當 alert_code == 901 時)); 支援最大長度為 15 個中文字
    game_datas = "[]"  # 重新計算局應保留的最低基礎參數 ((使用 JSON string 格式), <empty> 時 php json_encode 會視為 [])
    orders_opentrade = 0        #目前場上單子數 (幾張單 ?)
    orders_today = 0            #今日截至目前已結單子數
    orders_1dayago = 0          #1天前已結單子數
    orders_2dayago = 0          #2天前已結單子數
    orders_3dayago = 0          #3天前已結單子數
    orders_4dayago = 0          #4天前已結單子數
    orders_5dayago = 0          #5天前已結單子數
    orders_6dayago = 0          #6天前已結單子數
    orders_thisweek = 0         #本週截至目前的已結單子數, MT4 平台日期星期一起算, 含目前(今日)已結單子數
    orders_thismonth = 0        #本月截至目前的已結單子數, MT4 平台日期 01 日起算, 含目前(今日)已結單子數
    orders_total = 0            #交易帳號開始交易起至目前的單子數, 含目前場上單子數
    
    def __init__(self):
        dTime = datetime.datetime.now()
        self.timestamp = int(dTime.timestamp())
