from .marketdata import BarData
import shinehope.eaaccess.settings as settings
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# import matplotlib.dates as mdates
# import pandas as pd
import numpy as np
import talib

class CustomCursor(object):

    def __init__(self, axes, lypos, col, xlimits, ylimits, **kwargs):
        self.items = np.zeros(shape=(len(axes),3), dtype=np.object)
        self.col = col
        self.focus = 0
        i = 0
        for ax in axes:
            axis = ax
            axis.set_gid(i)
            lx = ax.axvline(ymin=ylimits[0],ymax=ylimits[1],color=col, ls='--', lw=0.5)
            # ly = ax.axhline(xmin=xlimits[0],xmax=xlimits[1],color=col, ls='--', lw=0.5)
            # if i == 0:
            #     ly = ax.axhline(8000, xmin=xlimits[0],xmax=xlimits[1],color=col, ls='--', lw=0.5)
            # else:
            #     ly = ax.axhline(xmin=xlimits[0],xmax=xlimits[1],color=col, ls='--', lw=0.5)
            ly = ax.axhline(lypos[i], xmin=xlimits[0],xmax=xlimits[1],color=col, ls='--', lw=0.5)            
            item = list([axis,lx,ly])
            self.items[i] = item
            i += 1
    def show_xy(self, event):
        if event.inaxes:
            self.focus = event.inaxes.get_gid()
            for ax in self.items[:,0]:
                self.gid = ax.get_gid()                                     
                for lx in self.items[:,1]:
                    lx.set_xdata(event.xdata)
                if event.inaxes.get_gid() == self.gid:
                    self.items[self.gid,2].set_ydata(event.ydata)
                    self.items[self.gid,2].set_visible(True)
        plt.draw()

    def hide_y(self, event):
        for ax in self.items[:,0]:
            if self.focus == ax.get_gid():
                self.items[self.focus,2].set_visible(False)

class UIReport(object):
    def __init__(self):
        super().__init__()

        ## for BackTest Graph show
        self.xaxis = []
        # self.xaxislbl = []
        # self.yaxis = []

        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volumn = []

        self.accPrice = 0.0
        self.accVol = 0.0

    def kline_bar_new(self, bar: BarData):
        dTime = datetime.fromtimestamp(bar.timestamp / 1000)
        # sTime = dTime.strftime("%Y-%m-%d %H:%M:%S")
        # VWAP是先計算得每一K棒的平均股價，如(H+L+C)/3、或(H+L+2C)/4，再乘以該K棒對應的成交量，
        # avgp = round((bar.high_price + bar.low_price + 2 * bar.close_price) / 4, 8)
        # vwPrice = avgp * bar.volume
        # self.accPrice = vwPrice
        # self.accVol = bar.volume
        # self.yaxis.append(avgp)
        # self.yaxis.append(bar.close_price)
        self.xaxis.append(dTime)
        # self.xaxislbl.append(datetime.strftime(dTime, "%m-%d %H:%M"))
        self.open.append(bar.open_price)
        self.high.append(bar.high_price)
        self.low.append(bar.low_price)
        self.close.append(bar.close_price)
        self.volumn.append(bar.volume)

    def kline_bar_update(self, bar: BarData):
        # avgp = round((bar.high_price + bar.low_price + 2 * bar.close_price) / 4, 8)
        # vwPrice = avgp * bar.volume
        # self.accPrice += vwPrice
        # self.accVol += bar.volume
        # self.yaxis[-1] = round(self.accPrice / self.accVol, 8)        
        # self.yaxis[-1] = bar.close_price

        self.open[-1] = bar.open_price
        self.high[-1] = bar.high_price
        self.low[-1] = bar.low_price
        self.close[-1] = bar.close_price
        self.volumn[-1] = bar.volume

    def report_profit(self, dbaccess, timeTo):
        """
            Show Backtest UI result
        """
        #導入蠟燭圖套件
        import mpl_finance as mpf

        # plt.style.use("bmh")
        #創建圖框
        # fig = plt.figure(figsize=(12, 5))
        # ax = fig.add_subplot(1, 1, 1)
        #用add_axes創建副圖框
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_axes([0.07,0.5,0.9,0.45]) ##左下角座標 (0,0.2)，寬高 (1,0.5)
        # ax2 = fig.add_axes([0.07,0.1,0.9,0.2])  ##左下角座標 (0,0)，寬高 (1,0.2)
        ax2 = fig.add_axes([0.07,0.3,0.9,0.2], sharex=ax)  ##左下角座標 (0,0)，寬高 (1,0.2)
        ax3 = fig.add_axes([0.07,0.1,0.9,0.2], sharex=ax)  ##左下角座標 (0,0)，寬高 (1,0.2)
        
        ax.set_title("Paper Trades")

        #設定座標數量及所呈現文字
        #使用mpl_finance套件candlestick2_ochl
        mpf.candlestick2_ohlc(ax, self.open, self.high, self.low, self.close, 
            width=0.5, colorup='g', colordown='r', alpha=0.75)
        mpf.volume_overlay(ax3, self.open, self.close, self.volumn, colorup='g', colordown='r', width=0.5, alpha=0.8)


        ax.xaxis.set_major_formatter(ticker.FuncFormatter(self.mydate))
        ax.xaxis.set_major_locator(ticker.MaxNLocator(10))

        # scatter
        trades = dbaccess.fetchBackTestTrades()
        for trade in trades:
            tradeID = trade[0].strip()
            dTime = datetime.fromtimestamp(trade[1] / 1000)
            # i = next((i for i, x in enumerate(self.xaxis) if x == dTime), -1)
            idx = self.xaxis.index(dTime)
            # tStamp = int(trade[1] / 1000)
            side = trade[2].strip()
            price = round(trade[3], 8)
            if side == "buy":
                # ax.scatter(dTime, price, color='green')
                ax.scatter(idx, price, color='green')
            else:
                # ax.scatter(dTime, price, color='red')
                ax.scatter(idx, price, color='red')

        # ax.plot(self.yaxis)
        naClose = np.array(self.close)
        minVal = naClose.min()
        maxVal = naClose.max()
        axhlVal = int((minVal + maxVal) / 2)
        sma_5 = talib.SMA(naClose, 5)
        sma_30 = talib.SMA(naClose, 30)
        ax.plot(sma_5, '-k', label='5_days_SMA', linewidth=0.5)
        ax.plot(sma_30, '-b', label='30_days_SMA', linewidth=0.5)
        # ax.legend(loc='upper left')
        """
            'best' : 0,          
            'upper right'  : 1,
            'upper left'   : 2,
            'lower left'   : 3,
            'lower right'  : 4,
            'right'        : 5,
            'center left'  : 6,
            'center right' : 7,
            'lower center' : 8,
            'upper center' : 9,
            'center'       : 10,
        """
        ax.legend(loc='best')
        ax.grid(True)
        # 會造成 ax, ax2, ax3 的 xtick labels 全消失
        # ax.set_xticklabels([])
        # ax.xaxis.set_ticklabels([])

        # frame1 = plt.gca()
        # for xlabel_i in frame1.axes.get_xticklabels():
        #     xlabel_i.set_visible(False)
        #     xlabel_i.set_fontsize(0.0)
        # for xlabel_i in frame1.axes.get_yticklabels():
        #     xlabel_i.set_fontsize(0.0)
        #     xlabel_i.set_visible(False)
        # for tick in frame1.axes.get_xticklines():
        #     tick.set_visible(False)
        # for tick in frame1.axes.get_yticklines():
        #     tick.set_visible(False)
        for xlabel_i in ax.get_xticklabels():
            xlabel_i.set_visible(False)
            # xlabel_i.set_fontsize(0.0)

        # dif: 12， 与26日的差别
        # dea:dif的9日以移动平均线
        # 计算MACD指标
        dif, dea, macd_hist = talib.MACD(naClose, fastperiod=12, slowperiod=26, signalperiod=9)
        # 绘制dif, dea线
        # naDiff = np.array(dif)
        # naDea = np.array(dea)
        # https://www.cnblogs.com/darkknightzh/p/6117528.html
        ax2.plot(dif, color="b", label="DIFF", linewidth=0.7, alpha=1)
        ax2.plot(dea, color="darkorange", label="DEA", linewidth=0.7, alpha=1)
        ax2.legend(loc='best')
        # 绘制MACD柱状图
        # 分开正负画
        # 画第一个bar， macd_hist，如果大于0， 保留当前值，如果小于0，变为0，得出一个red_hist
        # 画出第二个bar，macd_hisr，如果小于0， 保留当前值，如果大于0，直接变为0
        where_are_NaNs = np.isnan(macd_hist)
        macd_hist[where_are_NaNs] = 0
        green_hist = np.where(macd_hist > 0, macd_hist, 0)
        red_hist = np.where(macd_hist < 0, macd_hist, 0)

        nums = range(0, len(self.xaxis), 1)
        ## bar 的功能, 在數目多時會造成效能上的 issue; 因此改為使用 fill_between 模擬 bar 
        # # ax2.bar(nums, red_hist, label="r-MACD", color='r')
        # # ax2.bar(nums, green_hist, label="g-MACD", color='g')
        # ax2.fill_between(nums, 0, red_hist, facecolor='red', alpha=0.75, step='mid')
        # ax2.fill_between(nums, 0, green_hist, facecolor='green', alpha=0.75, step='mid')
        # plt.plot(x1, y1, x2, y2, marker = 'o')
        ## bar 的功能, 在數目多時會造成效能上的 issue; 因此改為使用 vlines 模擬 bar 
        ax2.vlines(nums, [0], red_hist, color="red", linewidth=1)
        ax2.vlines(nums, 0, green_hist, color="green", linewidth=1)
        # ax2.grid(True)
        for xlabel_i in ax2.get_xticklabels():
            xlabel_i.set_visible(False)
            # xlabel_i.set_fontsize(0.0)

        ## Rotate date labels automatically
        # fig.autofmt_xdate()
        plt.xticks(rotation=30)

        fig.canvas.manager.window.wm_geometry("+150+50")
        fig.canvas.set_window_title("EAAccess/Crypto 1.0")

        # ylimits=[[6000, 12000], [0,1], [0,1]]
        # lypos = [9000, 0, 0]
        # lypos = settings._axhline
        lypos = [axhlVal, 0, 0]
        cc = CustomCursor([ax,ax2,ax3], lypos, col='red', xlimits=[0,1], ylimits=[0,1])
        # cc = CustomCursor([ax,ax2,ax3], col='red', xlimits=[0,1], ylimits=ylimits, markersize=30,)
        fig.canvas.mpl_connect('motion_notify_event', cc.show_xy)
        fig.canvas.mpl_connect('axes_leave_event', cc.hide_y)
        # plt.grid(True)
        # plt.tight_layout(pad=1.5)
        # ax.set_xbound(len(self.xaxis) - 300, len(self.xaxis) + 100)
        # ax.margins(x=0, y=-0.25)

        plt.show()


    def mydate(self, x, pos):
        '''function for labeling xticks as datetime objects'''
        try:
            # return self.xaxis[int(x)]
            return datetime.strftime(self.xaxis[int(x)], "%m-%d %H:%M")
        except IndexError:
            return ''

"""
Q：何謂Volume Weighted Average Price (VWAP)？如何應用？
A：以前曾提及，成交量的變動遠比股價變動劇烈。前、後兩K棒的股價出現數倍的變動，不太可能，但成交量出現數倍的變動，則屢見不鮮，
故成交量的影響，不易以個別指標評估。有些分析者乃以股價結合成交量的方式，發展成交量加權的指標，筆者以前介紹過、自行發展的VW-RSI與此處介紹的VWAP、
或前文介紹的Accumulation/Distribution皆屬成交量加權指標。
VWAP是先計算得每一K棒的平均股價，如(H+L+C)/3、或(H+L+2C)/4，再乘以該K棒對應的成交量，所得結果表該K棒對應的總成交金額。
再由某一起始點，隨著時間的進展，逐K棒壘加總成交金額與總成交量，則由累加的(總成交金額/總成交量)可得累加期間的平均股價，此即為VWAP值。
以圖一的15分線圖為例，由第1根K棒起始，往後逐K棒累加計算VWAP值，所得結果如圖中的藍色線所示。圖最左邊的累加起始點，VWAP與股價的平均值重疊，
此後逐K棒往右，第2個VWAP值表前兩K棒的成交量加權平均股價，第3個VWAP值表前三K棒的成交量加權平均股價，至圖最右側，累加了132根K棒，
其VWAP值表前132K棒的成交量加權平均股價。可知此藍色VWAP曲線上的每一點表不同週期的移動平均值。若取固定週期為20的成交量加權移動平均，則如紅色線所示。
圖二所示的藍色VWAP曲線，其起始點遠早於圖一的起始點，故為更長週期的成交量加權移動平均股價。起始點不同，則VWAP值不同，是應用此指標的投資人需有的認知。
VWAP指標，一般是應用於極短線的交易上。若累加起始點設於交易日的起始時間，則VWAP值表當日、不同時間的成交量加權平均交易成本，若股價高於VWAP曲線，
表股價高於當日、當時的平均成本。若累加起始點設於一周的起始時間，則VWAP值表當周、不同時間的成交量加權平均交易成本，若股價低於VWAP曲線，
表股價低於當周、當時的平均成本，依此類推。若考慮買進，在VWAP曲線以下，是較佳買點。
附帶一提，VWAP指標為針對短線交易的特殊用途指標，並非所有交易平台都提供此指標。
"""

"""
Notes

Format Strings

A format string consists of a part for color, marker and line:

fmt = '[marker][line][color]'
Copy to clipboard
Each of them is optional. If not provided, the value from the style cycle is used. Exception: If line is given, but no marker, the data will be a line without markers.

Other combinations such as [color][marker][line] are also supported, but note that their parsing may be ambiguous.

Markers

character	description
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker
Line Styles

character	description
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style
Example format strings:

'b'    # blue markers with default shape
'or'   # red circles
'-g'   # green solid line
'--'   # dashed line with default color
'^k:'  # black triangle_up markers connected by a dotted line
Copy to clipboard
Colors

The supported color abbreviations are the single letter codes

character	color
'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white
and the 'CN' colors that index into the default property cycle.

If the color is the only part of the format string, you can additionally use any matplotlib.colors spec, e.g. full names ('green') or hex strings ('#008000').
"""