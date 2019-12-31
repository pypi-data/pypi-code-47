import shinehope.eaaccess.settings as settings
from .brokers.importer import Importer
import sqlite3
import os
import time
from datetime import datetime

def syncCandlesticks(dbFile, tblSymbol, timeFrom, timeTo, limit=500) -> bool:
    isOK = False
    if not os.path.exists(dbFile):
        return isOK
    
    try:
        conn = sqlite3.connect(dbFile)
        cursor = conn.cursor()
        sql = f"SELECT symbol, seq_start, seq_end  from candles_sequence where symbol = '{tblSymbol}' order by seq_start asc"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cntRows = len(rows)
        if cntRows > 0:
            bFetch = False
            fetchTimes = []
            bFoundAll = False
            tmpFrom = timeFrom
            for i in range(0, cntRows):
                thisStart = rows[i][1]                           
                thisEnd = rows[i][2] + 1 * 60
                if tmpFrom < thisStart:         # {1 回測開始時間 < 區間啟始時間
                    if timeTo <= thisStart:     # {1-1 回測結束時間 <= 區間啟始時間  ((在所有區間前))
                        fetchTimes.append([tmpFrom, timeTo])        # 登錄下載區間為 [回測開始時間, 回測結束時間]
                        bFetch = True 
                        bFoundAll = True
                        break
                    elif timeTo <= thisEnd:     # {1-2 回測結束時間 <= 區間結束時間
                        fetchTimes.append([tmpFrom, thisStart])     # 登錄下載區間為 [回測開始時間, 區間啟始時間]
                        bFetch = True 
                        bFoundAll = True
                        break
                    else:                       # {1-3 回測結束時間 > 區間結束時間
                        fetchTimes.append([tmpFrom, thisStart])     # 登錄下載區間為 [回測開始時間, 區間啟始時間]
                        bFetch = True
                        tmpFrom = thisEnd                           # ==> 將回測時間改為區間結束時間, 遞回至下一個區間判斷
                elif tmpFrom >= thisEnd:        # {2 回測開始時間 >= 區間結束時間   ==> 遞回至下一個區間判斷 
                    pass
                else:                           # {3 回測開始時間 in 區間
                    if timeTo <= thisEnd:       # {3-1 回測結束時間 <= 區間區間結束時間 ==> 已包含相關資料不需再次下載
                        bFoundAll = True
                        break
                    else:                       # {3-2 回測開始時間 in 區間 and 回測結束時間 > 區間結束時間 
                        tmpFrom = thisEnd       # ==> 將回測時間改為區間結束時間, 遞回至下一個區間判斷
            
            if not bFoundAll:                      # {2.escape --> 回測開始時間 及 回測結束時間 在所有區間後
                fetchTimes.append([tmpFrom, timeTo])
                bFetch = True

            if bFetch:
                # pass
                importer = Importer(settings.exchangeName)
                isOK = importer.connect(settings.apiKey, settings.apiSecret)
                if isOK:
                    for timeFrom, timeTo in fetchTimes:
                        strFrom = datetime.fromtimestamp(timeFrom).strftime('%Y-%m-%d %H:%M:%S')
                        strTo =  datetime.fromtimestamp(timeTo).strftime('%Y-%m-%d %H:%M:%S')
                        print(f"fetch Candlesticks from {strFrom} to {strTo}")

                        sinceBegin = timeFrom * 1000        # convert to milliseconds
                        sinceEnd = timeTo * 1000
                        lastrowid = 0
                        lastSeq = 0
                        # while lastSeq < timeTo:
                        bFinish = False
                        retryCnts = 0
                        while not bFinish:
                            fetchTStamp = sinceBegin / 1000
                            strFrom = datetime.fromtimestamp(fetchTStamp).strftime('%Y-%m-%d %H:%M:%S')
                            print(f"....fetching {limit} candles from {strFrom}")
                            ohlcv = importer.fetch_ohlcv(settings.symbol, '1m', sinceBegin, limit)
                            if not ohlcv:
                                print(f"Error: get <empty> candles...")
                                break

                            try:
                                for idx, bar in enumerate(ohlcv, start=0):
                                    if bar[0] >= sinceEnd:
                                        # lastSeq = int(bar[0] / 1000)
                                        bFinish = True
                                        break
                                    sql = (f"INSERT INTO candles_{tblSymbol}(start, open, high, low, close, volume, trans_dtime) values("
                                        f"{bar[0]}, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, datetime('now', 'localtime'))")
                                    cursor.execute(sql)
                                    lastSeq = int(bar[0] / 1000)
                            except sqlite3.IntegrityError as ex:
                                print(ex)
                                print(idx, bar, sinceBegin)
                                if retryCnts < 3:
                                    retryCnts += 1
                                    print(f"retry({retryCnts})...after 5 seconds")
                                    conn.rollback()
                                    time.sleep(5)
                                    continue
                                else:
                                    isOK = False
                                    conn.rollback()
                                    break      

                            # lastSeq = ohlcv[idx][0]
                            try:
                                if lastrowid == 0:
                                    sql = ("INSERT INTO candles_sequence(symbol, seq_start, seq_end, trans_dtime) values( "
                                        f"'{tblSymbol}',{timeFrom}, {lastSeq}, datetime('now', 'localtime'))")
                                    cursor.execute(sql)
                                    lastrowid = cursor.lastrowid
                                else:
                                    sql = (f"UPDATE candles_sequence set seq_end = {lastSeq}, "
                                        f"trans_dtime = datetime('now', 'localtime') WHERE id = {lastrowid}")
                                    cursor.execute(sql)
                            except Exception as ex:
                                print(ex)
                                isOK = False
                                conn.rollback()
                                break                       
                            conn.commit()
                            sinceBegin += 1 * 60 * 1000 * limit     # 1m == 1 * 60 * 1000 (milliseconds)
                            time.sleep(2)

                    """ merge candles_sequence records for continue period
                    """
                    sql = f"SELECT symbol, seq_start, seq_end  from candles_sequence where symbol = '{tblSymbol}' order by seq_start asc"
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    cntRows = len(rows)
                    bMerge = False
                    if cntRows > 0:
                        finalStart = rows[0][1]
                        tmpEnd = rows[0][2] + 1 * 60
                        for i in range(1, cntRows):
                            tmpStart = rows[i][1]
                            if tmpStart == tmpEnd:
                                bMerge = True
                                finalEnd = rows[i][2]
                                delSql = f"DELETE from candles_sequence where symbol = '{tblSymbol}' and seq_start = {tmpStart}"
                                cursor.execute(delSql)
                                updSql = (f"UPDATE candles_sequence set seq_end = {finalEnd}, trans_dtime = datetime('now', 'localtime') "
                                    f"WHERE symbol = '{tblSymbol}' and seq_start = {finalStart}" )
                                cursor.execute(updSql)
                            else:
                                finalStart = tmpStart
                            tmpEnd = rows[i][2] + 1 * 60
                        if bMerge:
                            conn.commit()
            else:
                print("Candlestick is synchronized !")      

        else:
            strFrom = datetime.fromtimestamp(timeFrom).strftime('%Y-%m-%d %H:%M:%S')
            strTo =  datetime.fromtimestamp(timeTo).strftime('%Y-%m-%d %H:%M:%S')
            print(f"fetch Candlesticks from {strFrom} to {strTo}")
            importer = Importer(settings.exchangeName)
            isOK = importer.connect(settings.apiKey, settings.apiSecret)
            if isOK:
                sinceBegin = timeFrom * 1000        # convert to milliseconds
                sinceEnd = timeTo * 1000
                lastrowid = 0
                lastSeq = 0
                # while lastSeq < timeTo:
                bFinish = False
                retryCnts = 0
                while not bFinish:
                    fetchTStamp = sinceBegin / 1000
                    strFrom = datetime.fromtimestamp(fetchTStamp).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"....fetching {limit} candles from {strFrom}")
                    ohlcv = importer.fetch_ohlcv(settings.symbol, '1m', sinceBegin, limit)
                    if not ohlcv:
                        print(f"Error: get <empty> candles...")
                        break

                    try:
                        for idx, bar in enumerate(ohlcv, start=0):
                            if bar[0] >= sinceEnd:
                                # lastSeq = int(bar[0] / 1000)
                                bFinish = True
                                break
                            sql = (f"INSERT INTO candles_{tblSymbol}(start, open, high, low, close, volume, trans_dtime) values("
                                f"{bar[0]}, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, datetime('now', 'localtime'))")
                            cursor.execute(sql)
                            lastSeq = int(bar[0] / 1000)
                    except sqlite3.IntegrityError as ex:
                        print(ex)
                        print(idx, bar, sinceBegin)
                        if retryCnts < 3:
                            retryCnts += 1
                            print(f"retry({retryCnts})...after 5 seconds")
                            conn.rollback()
                            time.sleep(5)
                            continue
                        else:
                            isOK = False
                            conn.rollback()
                            break                             


                    # lastSeq = ohlcv[idx][0]
                    try:
                        if lastrowid == 0:
                            sql = ("INSERT INTO candles_sequence(symbol, seq_start, seq_end, trans_dtime) values( "
                                f"'{tblSymbol}',{timeFrom}, {lastSeq}, datetime('now', 'localtime'))")
                            cursor.execute(sql)
                            lastrowid = cursor.lastrowid
                        else:
                            sql = (f"UPDATE candles_sequence set seq_end = {lastSeq}, "
                                f"trans_dtime = datetime('now', 'localtime') WHERE id = {lastrowid}")
                            cursor.execute(sql)
                    except Exception as ex:
                        print(ex)
                        isOK = False
                        conn.rollback()
                        break                       
                    conn.commit()
                    sinceBegin += 1 * 60 * 1000 * limit     # 1m == 1 * 60 * 1000 (milliseconds)
                    time.sleep(2)
    finally:
        conn.close()
    return  isOK

