#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# basic functions for crossplot

import sys, os
import numpy as np
import matplotlib.pyplot as plt
#
sys.path.append(os.path.dirname(__file__)[:-9][:-4][:-13])
from cognitivegeo.src.basic.matdict import matdict as basic_mdt
from cognitivegeo.src.vis.font import font as vis_font
from cognitivegeo.src.vis.messager import messager as vis_msg

__all__ = ['visualization']


def crossplot2D(pointdict,
                colorlist=[], linestylelist=[],
                linewidthlist=[],
                markerstylelist=[],
                markersizelist=[],
                xfeature='x', xlabel='x-label',
                yfeature='y', ylabel='y-label',
                xlim=[-10, 10], ylim=[-10, 10],
                fontstyle=None,
                title=None,
                legendon=True,
                qicon=None, qtitle='2D Window - PointSet Cross-plot'):
    """
    2D corss plot

    Args:
        pointdict:          Point dictionary, with each key representing a point group
        colorlist:          List of the colors for each point group
        linestylelist:      List of the line style for each point group
        linewidthlist:      List of the line width for each point group
        markerstylelist:    List of the marker style for each point group
        markersizelist:     List of the marker size for each point group
        xfeature:           x-axis feature. It must be within the keys in each point group
        xlabel:             x-axis label to display
        yfeature:           y-axis feature. It must be within the keys in each point group
        ylabel:             y-axis label to display
        xlim:               x-axi limit to display
        ylim:               y-axis limit to display
        fontstyle:          font style to display
        title:              title to display
        legendon:           Legend to be displayed or not. Default is True
        qicon:              QIcon to be used for the window
        qtitle:             QTitle to be used for the window

    Return:
        None
    """


    # if len(colorlist) < len(pointdict):
    #     print('WARNING in crossplot2D: No color coding')
    #     colorlist = []
    # if len(markerlist) < len(pointdict):
    #     print('WARNING in crossplot2D: No marker coding')
    #     markerlist = []

    vis_font.updatePltFont(fontstyle)
    #
    fig = plt.figure(facecolor='white')
    for idx, name in enumerate(pointdict):
        color = 'Black'
        if idx < len(colorlist):
            color = colorlist[idx]
        linestyle = 'Solid'
        if idx < len(linestylelist):
            linestyle = linestylelist[idx]
        linewidth = 12
        if idx < len(linewidthlist):
            linewidth = linewidthlist[idx]
        markerstyle = '.'
        if idx < len(markerstylelist):
            markerstyle = markerstylelist[idx]
        markersize = '.'
        if idx < len(markersizelist):
            markersize = markersizelist[idx]
        #
        pointdata = pointdict[name]
        if xfeature not in pointdata.keys():
            vis_msg.print('ERROR in crossplot2D: %s not found in %s' %(xfeature, name), type='error')
            sys.exit()
        if yfeature not in pointdata.keys():
            vis_msg.print('ERROR in crossplot2D: %s not found in %s' %(yfeature, name), type='error')
            sys.exit()
        #
        pointnum = basic_mdt.maxDictConstantRow(pointdata)
        x = np.mean(np.reshape(pointdata[xfeature], [pointnum, -1]),
                    axis=1)
        y = np.mean(np.reshape(pointdata[yfeature], [pointnum, -1]),
                    axis=1)
        plt.plot(x, y, linestyle=linestyle, linewidth=linewidth,
                 color=color, marker=markerstyle, markersize=markersize, label=name)
    #
    if legendon:
        plt.legend()
    #
    plt.xlabel(xlabel)
    plt.xlim(xlim)
    plt.ylabel(ylabel)
    plt.ylim(ylim)
    if title is None:
        title = xfeature + ' vs ' + yfeature
    plt.title(title)

    if qicon is not None:
        fig.canvas.set_window_title(qtitle)
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)

    plt.show()


class visualization:
    # Pack all functions as a class
    #
    crossplot2D = crossplot2D