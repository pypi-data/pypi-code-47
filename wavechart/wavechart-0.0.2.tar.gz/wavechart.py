""""
some utils to show audio wave
"""
__author__ = "Xiangkui Li"

import wave

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


############################################################
# dynamic wave chart
############################################################

class DynamicWaveChart:
    """
    this class is used to show dynamic audio wave chart
    """

    def __init__(self, wave_queue, title='Audio Wave', figsize=(12, 8), max_x=5000, max_y=2 ** 16,
                 channels=2, sample_gap=10, interval=20):
        """
        initial chart
        :param wave_queue: numpy data queue
        :param title: chart title
        :param figsize: chart size
        :param max_x: max value of x axis
        :param max_y: max value of y axis
        :param channels: audio channels
        :param sample_gap: chart sound waveform sampling gap
        :param interval: draw interval
        """

        self.wave_queue = wave_queue
        self.title = title
        self.figsize = figsize
        self.max_x = max_x
        self.max_y = max_y
        self.channels = channels
        self.sample_gap = sample_gap
        self.interval = interval
        self.x = np.arange(0, max_x)
        self.y = np.zeros((channels, max_x))
        self.np = np
        self.plt = plt
        # 绘图参数
        self.fig = plt.figure(figsize=self.figsize)
        self.fig.canvas.set_window_title(self.title)
        self.fig.suptitle(self.title, fontsize=30)
        # 绘图颜色
        self.colors = ['green', 'orange']
        # 图表列表
        self.ax_list = [self.fig.add_subplot(211 + i) for i in range(channels)]
        self.line_list = [self.ax_list[i].plot([], [], color=self.colors[i])[0] for i in range(channels)]

    def _init(self):
        # set axis and title
        for i, ax in enumerate(self.ax_list):
            ax.set_xlim(0, self.max_x)
            ax.set_ylim(-self.max_y, self.max_y)
            ax.set_title('Channel %s' % i)
        return self.line_list

    def _update(self, step):
        """
        update chart
        :param step:
        :return:
        """
        while not self.wave_queue.empty():
            data = self.wave_queue.get()
            self.y = self.np.concatenate((self.y, data[::, ::self.sample_gap]), axis=1)[::, -self.max_x:]
        for i, line in enumerate(self.line_list):
            line.set_data(self.x, self.y[i])
        return self.line_list

    def show(self):
        FuncAnimation(self.fig, self._update, init_func=self._init, interval=self.interval, blit=True)
        plt.show()


############################################################
# static wave chart
############################################################

class StaticWaveChart:
    """
    this class is used to show static audio wave chart
    """

    def __init__(self, path, title='Audio Wave', figsize=(12, 8)):
        """
        initial chart

        :param path: audio file path
        :param title: chart title
        :param figsize: chart size
        """

        self.title = title
        self.figsize = figsize
        file = wave.open(path, "rb")
        params = file.getparams()
        self.channels, self.rate, self.frames = params[0], params[2], params[3]
        frame_data = np.fromstring(file.readframes(self.frames), dtype=np.short)
        file.close()
        # 拆分channel
        frame_data.shape = (-1, self.channels)
        self.data = frame_data.T

    def show(self):
        # scale x-axis unit to second
        time = np.arange(0, self.frames) / self.rate
        # draw wave chart
        figure = plt.figure(figsize=self.figsize)
        figure.canvas.set_window_title(self.title)
        plt.suptitle(self.title, fontsize=30)
        colors = ['green', 'orange']
        for i in range(0, self.data.shape[0]):
            ax = plt.subplot(211 + i)
            ax.set_title('Channel %s' % i)
            plt.ylim(-2 ** 16, 2 ** 16)
            plt.plot(time, self.data[i], color=colors[i])
        plt.show()
