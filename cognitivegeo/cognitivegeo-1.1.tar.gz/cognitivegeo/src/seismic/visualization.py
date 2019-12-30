#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     March 2018                                                                      #
#                                                                                           #
#############################################################################################

# Seismic data visualization

from PyQt5 import QtCore
import sys, os
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from vispy import app, scene
from vispy.color import Colormap
#
sys.path.append(os.path.dirname(__file__)[:-8][:-4][:-13])
from cognitivegeo.src.vis.font import font as vis_font
from cognitivegeo.src.vis.colormap import colormap as vis_cmap
from cognitivegeo.src.vis.messager import messager as vis_msg
from cognitivegeo.src.seismic.analysis import analysis as seis_ays


__all__ = ['visualization']


def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)


def first_slice(ax, pref='', surf='', idxlist=None):
    """Go to the previous slice."""
    volume = ax.volume
    ax.index = 0
    ax.images[0].set_array(volume[ax.index])
    if idxlist is None:
        idx = ax.index
    else:
        idx = idxlist[ax.index]
    ax.set_title(pref+str(idx)+surf)


def previous_slice(ax, step=1, pref='', surf='', idxlist=None):
    """Go to the previous slice."""
    volume = ax.volume
    ax.index = (ax.index - step) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])
    if idxlist is None:
        idx = ax.index
    else:
        idx = idxlist[ax.index]
    ax.set_title(pref+str(idx)+surf)


def next_slice(ax, step=1, pref='', surf='', idxlist=None):
    """Go to the next slice."""
    volume = ax.volume
    ax.index = (ax.index + step) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])
    if idxlist is None:
        idx = ax.index
    else:
        idx = idxlist[ax.index]
    ax.set_title(pref+str(idx)+surf)


def last_slice(ax, pref='', surf='', idxlist=None):
    """Go to the previous slice."""
    volume = ax.volume
    ax.index = volume.shape[0]-1
    ax.images[0].set_array(volume[ax.index])
    if idxlist is None:
        idx = ax.index
    else:
        idx = idxlist[ax.index]
    ax.set_title(pref+str(idx)+surf)


def first_trace_x(ax, dim_xy, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the first trace along x direction (lower dimension)."""
    volume = ax.volume
    index_y = int(ax.index / dim_xy[0])
    index_x = 0 # ax.index - index_y * dim_x
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def previous_trace_x(ax, dim_xy, step_x=1, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the previous trace along x direction (lower dimension)."""
    volume = ax.volume
    index_y = int(ax.index / dim_xy[0])
    index_x = (ax.index - index_y * dim_xy[0] - step_x) % dim_xy[0]
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def next_trace_x(ax, dim_xy, step_x=1, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the next trace along x direction (lower dimension)."""
    volume = ax.volume
    index_y = int(ax.index / dim_xy[0])
    index_x = (ax.index - index_y * dim_xy[0] + step_x) % dim_xy[0]
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def last_trace_x(ax, dim_xy, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the last trace along x direction (lower dimension)."""
    volume = ax.volume
    index_y = int(ax.index / dim_xy[0])
    index_x = dim_xy[0] - 1 # ax.index - index_y * dim_x
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def first_trace_y(ax, dim_xy, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the first trace along y direction (higher dimension)."""
    volume = ax.volume
    index_y = 0
    index_x = ax.index % dim_xy[0]
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def previous_trace_y(ax, dim_xy, step_y=1, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the previous trace along y direction (higher dimension)."""
    volume = ax.volume
    index_y = (int(ax.index / dim_xy[0]) - step_y) % dim_xy[1]
    index_x = ax.index % dim_xy[0]
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def next_trace_y(ax, dim_xy, step_y=1, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the next trace along y direction (higher dimension)."""
    volume = ax.volume
    index_y = (int(ax.index / dim_xy[0])+ step_y) % dim_xy[1]
    index_x = ax.index % dim_xy[0]
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def last_trace_y(ax, dim_xy, pref='', surf='', idxlist_x=None, idxlist_y=None):
    """Go to the last trace along y direction (higher dimension)."""
    volume = ax.volume
    index_y = dim_xy[1] - 1
    index_x = ax.index % dim_xy[0]
    ax.index = index_y * dim_xy[0] + index_x
    ax.lines[0].set_ydata(volume[:, ax.index])
    if idxlist_x is not None:
        index_x = idxlist_x[index_x]
    if idxlist_y is not None:
        index_y = idxlist_y[index_y]
    ax.set_title(pref+'('+str(index_y)+', '+str(index_x)+')'+surf)


def plotSeisILSliceFrom2DMat(seis2dmat, inlsls=None, datacol=3,
                             inlcol=0, xlcol=1, zcol=2,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             titlesurf='', colorbaron=False,
                             verbose=True):
    """
    Plot seismic inline slices from 2D matrix (Seis2Dmat)(by matplotlib.imshow)

    Argus:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        inlsls:     inline No. for plotting
                    Plot all inline slicess if not specified
        datacol:    index of data column for plotting in 2D matrix (Indexing from 0)
                    Use the fourth column if not specified (targetcol=3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        verbose:    flag for message display. Default is True

    Return:
        N/A
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisILSliceFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisILSliceFrom2DMat: Not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisILSliceFrom2DMat: Not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisILSliceFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisILSliceFrom2DMat: Not z column found in 2D seismic matrix', type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                 datacol=datacol,
                                                 inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if inlsls is None:
        vis_msg.print('WARNING in plotSeisILSliceFrom2DMat: to plot all inline slices in 2D seismic matrix',
                      type='warning')
        inlsls = inlrange

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in plotSeisILSliceFrom2DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, zrange)

    ninlsls = len(inlsls)
    if verbose:
        print('Plot ' + str(ninlsls) + ' inline slices')
    for i in range(ninlsls):
        inl = inlsls[i]
        idx = np.round((inl - inlstart) / inlstep).astype(np.int32)
        if idx >= 0 and idx < inlnum:
            seisdata = seis3dmat[:, :, idx]
            plt.figure(facecolor='white')
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([zend, zstart])
            plt.title('Inline No.' + str(inlrange[idx]) + titlesurf)
            plt.xlabel('Crossline No.')
            plt.ylabel('Vertical (z) Depth/Time')
            if colorbaron:
                plt.colorbar()
    plt.show()

    return


def plotSeisILSlicePlayerFrom2DMat(seis2dmat, initinlsl=None, datacol=3,
                                   inlcol=0, xlcol=1, zcol=2,
                                   colormap=None, flipcmap=False,
                                   valuemin=-1.0, valuemax=1.0,
                                   titlesurf='', colorbaron=False,
                                   interpolation='bicubic',
                                   playerconfig=None,
                                   fontstyle=None,
                                   qicon=None
                                   ):
    """
    Plot seismic inline slices from 2D matrix (Seis2DMat), as a player (by matplotlib.imshow)

    Args:
        seis2dmat:      2D matrix representing seismic data
                        It contains at least four columns, [IL, XL, Z, Value, ...]
        initinlsl:      initial inline No. for player
                        Plot the first inline slicess if not specified
        datacol:        index of data column for plotting in 2D matrix (Indexing from 0)
                        Use the fourth column if not specified (targetcol=3)
        inlcol:         index of inline column. Default is the first column (0)
        xlcol:          index of crossline column. Default is the second column (1)
        zcol:           index of z column. Default is the third column (2)
        colormap:       colormap name for seismic data visualization, such as 'seismic'
                        Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:       Flip colormap. Default is False
        valuemin:       lower limit for seismic data visualization. Default is -1.0
        valuemax:       upper limit for seismic data visualization. Default is 1.0
        titlesurf:      surfix for the title. Default is blank
        colorbaron:     colorbar display. Default is false
        interpolation:  interpolation type. Default is 'bicubic'
        playerconfig:   Player configuration. Default is None
        fontstyle:      Font style object. Default is None
        qicon:          QIcon for plotting window. Default is None

    Return:
        None
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisILSlicePlayerFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisILSlicePlayerFrom2DMat: Not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisILSlicePlayerFrom2DMat: Not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisILSlicePlayerFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisILSlicePlayerFrom2DMat: Not z column found in 2D seismic matrix',
                      type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                        inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if initinlsl is None:
        vis_msg.print('WARNING in plotSeisILSlicePlayerFrom2DMat: '
                      'to be initialized by the first inline slice in 2D seismic matrix', type='warning')
        initinlsl = inlrange[0]


    if playerconfig is None:
        playerconfig = {}
        playerconfig['First'] = 'A'
        playerconfig['Previous'] = 'S'
        playerconfig['Backward'] = 'Q'
        playerconfig['Pause'] = 'P'
        playerconfig['Forward'] = 'W'
        playerconfig['Next'] = 'D'
        playerconfig['Last'] = 'F'
        playerconfig['Interval'] = 5

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfig['First'].lower():
            first_slice(ax, pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Previous'].lower():
            previous_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Next'].lower():
            next_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Last'].lower():
            last_slice(ax, pref='Inline No. ', surf=titlesurf,
                       idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Backward'].lower():
            while True:
                previous_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                               idxlist=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Forward'].lower():
            while True:
                next_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfig['First'].lower(), playerconfig['Previous'].lower(),
                             playerconfig['Backward'].lower(), playerconfig['Pause'].lower(),
                             playerconfig['Forward'].lower(), playerconfig['Next'].lower(),
                             playerconfig['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(8, 8))
    # ax.set_xticks(np.linspace(0, len(xlrange)-1, 6, dtype=int))
    # ax.set_xticklabels(np.linspace(xlstart, xlend, 6, dtype=int))
    # ax.set_yticks(np.linspace(0, len(zrange) - 1, 6, dtype=int))
    # ax.set_yticklabels(np.linspace(zstart, zend, 6, dtype=int))
    ax.set_xlabel('Crossline No.')
    ax.set_ylabel('Vertical (z) Depth/Time')
    volume = np.transpose(seis3dmat, [2,0,1])
    ax.volume = volume
    ax.index = int((initinlsl-inlstart)/inlstep)
    ax.set_title('Inline No. ' + str(inlrange[ax.index]) + titlesurf)
    cat = ax.imshow(volume[ax.index],
                    aspect='auto', #float(len(xlrange))/float(len(zrange)),
                    extent=[xlstart, xlend, zend, zstart],
                    cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                    interpolation=interpolation,
                    vmin=valuemin, vmax=valuemax)
    if colorbaron:
        fig.colorbar(cat)
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('2D Window - Seismic Inline')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisILSliceFrom3DMat(seis3dmat, inlsls=None, seisinfo=None,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             titlesurf='', colorbaron=False,
                             verbose=True):
    """
    Plot seismic inline slices from 3D matrix (Seis3DMat) (by matplotlib.imshow)

    Args:
        seis3dmat:  3D matrix representing seismic data [Z/XL/IL]
        inlsls:     inline No. for plotting
                    Plot all inline slices if not specified
        seisinfo:   basic information of 3D seismic survey
                    Auto-generated from 3D matrix if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        verbose:    flag for message display. Default is True

    Return:
        None
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisILSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisILSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if inlsls is None:
        vis_msg.print('WARNING in plotSeisILSliceFrom3DMat: to plot all inline slices in 3D seismic matrix',
                      type='warning')
        inlsls = inlrange

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in plotSeisILSliceFrom3DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, zrange)

    ninlsls = len(inlsls)
    if verbose:
        print('Plot ' + str(ninlsls) + ' inline slices')
    for i in range(ninlsls):
        inl = inlsls[i]
        idx = np.round((inl - inlstart) / inlstep).astype(np.int32)
        if idx >= 0 and idx < inlnum:
            seisdata = seis3dmat[:, :, idx]
            plt.figure(facecolor='white')
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([zend, zstart])
            plt.title('Inline No.' + str(inlrange[idx]) + titlesurf)
            plt.xlabel('Crossline No.')
            plt.ylabel('Vertical (z) Depth/Time')
            if colorbaron:
                plt.colorbar()
    plt.show()

    return


def plotSeisILSlicePlayerFrom3DMat(seis3dmat, initinlsl=None, seisinfo=None,
                                   colormap=None, flipcmap=False,
                                   valuemin=-1.0, valuemax=1.0,
                                   titlesurf='', colorbaron=False,
                                   interpolation='bicubic',
                                   playerconfig=None,
                                   fontstyle=None,
                                   qicon=None
                                   ):
    """
    Plot seismic inline slices from 3D matrix, as a player (by matplotlib.imshow)

    Args:
        seis3dmat:  3D matrix representing seismic data
        initinlsl:  initial inline No. for player
                    Plot the first inline slicess if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        interpolation:  interpolation type. Default is 'bicubic'
        playerconfig:   Player configuration. Default is None
        fontstyle:      Font style object. Default is None
        qicon:      QIcon for plotting window. Default is None

    Return:
        None
    """

    # Check input matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisILSlicePlayerFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print("WARNING in plotSeisILSlicePlayerFrom3DMat: SeisInfo automatically generated",
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if initinlsl is None:
        vis_msg.print('WARNING in plotSeisILSlicePlayerFrom2DMat: '
                      'to be initialized by the first inline slice in 2D seismic matrix', type='warning')
        initinlsl = inlrange[0]

    if playerconfig is None:
        playerconfig = {}
        playerconfig['First'] = 'A'
        playerconfig['Previous'] = 'S'
        playerconfig['Backward'] = 'Q'
        playerconfig['Pause'] = 'P'
        playerconfig['Forward'] = 'W'
        playerconfig['Next'] = 'D'
        playerconfig['Last'] = 'F'
        playerconfig['Interval'] = 5

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfig['First'].lower():
            first_slice(ax, pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Previous'].lower():
            previous_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Next'].lower():
            next_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Last'].lower():
            last_slice(ax, pref='Inline No. ', surf=titlesurf,
                       idxlist=inlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Backward'].lower():
            while True:
                previous_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                               idxlist=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Forward'].lower():
            while True:
                next_slice(ax, step=playerconfig['Interval'], pref='Inline No. ', surf=titlesurf,
                           idxlist=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfig['First'].lower(), playerconfig['Previous'].lower(),
                             playerconfig['Backward'].lower(), playerconfig['Pause'].lower(),
                             playerconfig['Forward'].lower(), playerconfig['Next'].lower(),
                             playerconfig['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(8, 8))
    # ax.set_xticks(np.linspace(0, len(xlrange)-1, xlnum, dtype=int))
    # ax.set_xticklabels(np.linspace(xlstart, xlend, xlnum, dtype=int))
    # ax.set_yticks(np.linspace(0, len(zrange) - 1, znum, dtype=int))
    # ax.set_yticklabels(np.linspace(zstart, zend, znum, dtype=int))
    ax.set_xlabel('Crossline No.')
    ax.set_ylabel('Vertical (z) Depth/Time')
    volume = np.transpose(seis3dmat, [2,0,1])
    ax.volume = volume
    ax.index = int((initinlsl-inlstart)/inlstep)
    ax.set_title('Inline No. ' + str(inlrange[ax.index]) + titlesurf)
    cat = ax.imshow(volume[ax.index],
                    # aspect=None,
                    aspect='auto', #float(len(zrange))/float(len(xlrange)),
                    extent=[xlstart, xlend, zend, zstart],
                    cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                    interpolation=interpolation,
                    vmin=valuemin, vmax=valuemax)

    if colorbaron:
        fig.colorbar(cat)
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('2D Window - Seismic Inline')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisXLSliceFrom2DMat(seis2dmat, xlsls=None, datacol=3,
                             inlcol=0, xlcol=1, zcol=2,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             titlesurf='', colorbaron=False,
                             verbose=True):
    """
    Plot seismic crossline slices from 2D matrix (Seis2Dmat) (by matplotlib.imshow)

    Args:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        xlsls:      crossline No. for plotting
                    Plot all crossline slices if not specified
        datacol:    index of data column for plotting in 2D matrix (indexing from 0)
                    Plot the fourth column if not specified (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        verbose:    flag for message display. Default is True

    Return:
        None
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisXLSliceFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisXLSliceFrom2DMat: not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisXLSliceFrom2DMat: not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisXLSliceFrom2DMat: not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisXLSliceFrom2DMat: not z column found in 2D seismic matrix',
                      type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1

    if xlsls is None:
        vis_msg.print('WARNING in plotSeisXLSliceFrom2DMat: to plot all crossline slices in 2D seismic matrix',
                      type='warning')
        xlsls = xlrange

    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in plotSeisXLSliceFrom2DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(inlrange, zrange)

    nxlsls = len(xlsls)
    if verbose:
        print('Plot ' + str(nxlsls) + ' crossline slices')
    for i in range(nxlsls):
        xl = xlsls[i]
        idx = np.round((xl - xlstart) / xlstep).astype(np.int32)
        if idx >= 0 and idx < xlnum:
            seisdata = seis3dmat[:, idx, :]
            plt.figure(facecolor='white')
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([inlstart, inlend])
            plt.ylim([zend, zstart])
            plt.title('Crossline No.' + str(xlrange[idx]) + titlesurf)
            plt.xlabel('Inline No.')
            plt.ylabel('Vertical (z) Depth/Time')
            if colorbaron:
                plt.colorbar()
    plt.show()

    return


def plotSeisXLSlicePlayerFrom2DMat(seis2dmat, initxsl=None, datacol=3,
                                   inlcol=0, xlcol=1, zcol=2,
                                   colormap=None, flipcmap=False,
                                   valuemin=-1.0, valuemax=1.0,
                                   titlesurf='', colorbaron=False,
                                   interpolation='bicubic',
                                   playerconfig=None,
                                   fontstyle=None,
                                   qicon=None
                                   ):
    """
    Plot seismic crossline slices from 2D matrix, as a player (by matplotlib.imshow)

    Args:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        initxsl:    initial crossline No. for player
                    Plot the first crossline slices if not specified
        datacol:    index of data column for plotting in 2D matrix (indexing from 0)
                    Plot the fourth column if not specified (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        interpolation:  interpolation type. Default is 'bicubic'
        playerconfig:   Player configuration. Default is None
        fontstyle:      Font style object. Default is None
        qicon:      QIcon for plotting window. Default is None

    Return:
        None
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisXLSlicePlayerFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisXLSlicePlayerFrom2DMat: not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisXLSlicePlayerFrom2DMat: not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisXLSlicePlayerFrom2DMat: not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisXLSlicePlayerFrom2DMat: not z column found in 2D seismic matrix',
                      type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1

    if initxsl is None:
        vis_msg.print('WARNING in plotSeisXLSlicePlayerFrom2DMat: '
                      'to be initialized by the first crossline slice in the 2D seismic matrix', type='warning')
        initxsl = xlrange[0]

    if playerconfig is None:
        playerconfig = {}
        playerconfig['First'] = 'A'
        playerconfig['Previous'] = 'S'
        playerconfig['Backward'] = 'Q'
        playerconfig['Pause'] = 'P'
        playerconfig['Forward'] = 'W'
        playerconfig['Next'] = 'D'
        playerconfig['Last'] = 'F'
        playerconfig['Interval'] = 5

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfig['First'].lower():
            first_slice(ax, pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Previous'].lower():
            previous_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Next'].lower():
            next_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Last'].lower():
            last_slice(ax, pref='Crossline No. ', surf=titlesurf,
                       idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Backward'].lower():
            while True:
                previous_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                               idxlist=xlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Forward'].lower():
            while True:
                next_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfig['First'].lower(), playerconfig['Previous'].lower(),
                             playerconfig['Backward'].lower(), playerconfig['Pause'].lower(),
                             playerconfig['Forward'].lower(), playerconfig['Next'].lower(),
                             playerconfig['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(8, 8))
    # ax.set_xticks(np.linspace(0, len(inlrange)-1, 6, dtype=int))
    # ax.set_xticklabels(np.linspace(inlstart, inlend, 6, dtype=int))
    # ax.set_yticks(np.linspace(0, len(zrange) - 1, 6, dtype=int))
    # ax.set_yticklabels(np.linspace(zstart, zend, 6, dtype=int))
    ax.set_xlabel('Inline No.')
    ax.set_ylabel('Vertical (z) Depth/Time')
    volume = np.transpose(seis3dmat, [1,0,2])
    ax.volume = volume
    ax.index = int((initxsl-xlstart)/xlstep)
    ax.set_title('Crossline No. ' + str(xlrange[ax.index]) + titlesurf)

    cat = ax.imshow(volume[ax.index],
                    # aspect=None,
                    aspect='auto', #float(len(inlrange))/float(len(zrange)),
                    extent=[inlstart, inlend, zend, zstart],
                    cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                    interpolation=interpolation,
                    vmin=valuemin, vmax=valuemax)
    if colorbaron:
        fig.colorbar(cat)
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('2D Window - Seismic Crossline')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisXLSliceFrom3DMat(seis3dmat, xlsls=None, seisinfo=None,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             titlesurf='', colorbaron=False,
                             verbose=True):
    """
    Plot seismic crossline slices from 3D matrix (Seis3DMat) (by matplotlib.imshow)
    Argus:
        seis3dmat:  3D matrix representing seismic data [Z/XL/IL]
        xlsls:      crossline No. for plotting
                    Plot all crossline slices if not specified
        seisinfo:   basic information of 3D seismic survey
                    Auto-generated from 3D matrix if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        verbose:    flag for message display. Default is True
    Return:
        None
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisXLFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisXLFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1

    if xlsls is None:
        vis_msg.print('WARNING in plotSeisXLSliceFrom3DMat: to plot all crossline slices in 3D seismic matrix',
                      type='warning')
        xlsls = xlrange

    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in plotSeisXLFrom3DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(inlrange, zrange)

    nxlsls = len(xlsls)
    if verbose:
        print('Plot ' + str(nxlsls) + ' crossline slices')
    for i in range(nxlsls):
        xl = xlsls[i]
        idx = np.round((xl-xlstart)/xlstep).astype(np.int32)
        if idx>=0 and idx<xlnum:
            seisdata = seis3dmat[:, idx, :]
            plt.figure(facecolor='white')
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([inlstart, inlend])
            plt.ylim([zend, zstart])
            plt.title('Crossline No.' + str(xlrange[idx]) + titlesurf)
            plt.xlabel('Inline No.')
            plt.ylabel('Vertical (z) Depth/Time')
            if colorbaron:
                plt.colors()
    plt.show()

    return


def plotSeisXLSlicePlayerFrom3DMat(seis3dmat, initxsl=None, seisinfo=None,
                                   colormap=None, flipcmap=False,
                                   valuemin=-1.0, valuemax=1.0,
                                   titlesurf='', colorbaron=False,
                                   interpolation='bicubic',
                                   playerconfig=None,
                                   fontstyle=None,
                                   qicon=None
                                   ):
    """
    Plot seismic crossline slices from 3D matrix, as a player (by matplotlib.imshow)

    Args:
        seis3dmat:  3D matrix representing seismic data
        initxsl:    initial crossline No. for player
                    Plot the first crossline slices if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        interpolation:  interpolation type. Default is 'bicubic'
        playerconfig:   Player configuration. Default is None
        fontstyle:      Font style object. Default is None
        qicon:      QIcon for plotting window. Default is None

    Return:
        N/A
    """

    # Check input matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisXLSlicePlayerFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisXLSlicePlayerFrom3DMat: SeisInfo automatically generated', type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1

    if initxsl is None:
        vis_msg.print('WARNING in plotSeisXLSlicePlayerFrom3DMat: '
                      'to be initialized by the first crossline slice in the 3D seismic matrix', type='warning')
        initxsl = xlrange[0]

    if playerconfig is None:
        playerconfig = {}
        playerconfig['First'] = 'A'
        playerconfig['Previous'] = 'S'
        playerconfig['Backward'] = 'Q'
        playerconfig['Pause'] = 'P'
        playerconfig['Forward'] = 'W'
        playerconfig['Next'] = 'D'
        playerconfig['Last'] = 'F'
        playerconfig['Interval'] = 5

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfig['First'].lower():
            first_slice(ax, pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Previous'].lower():
            previous_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Next'].lower():
            next_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Last'].lower():
            last_slice(ax, pref='Crossline No. ', surf=titlesurf,
                       idxlist=xlrange)
            fig.canvas.draw()
        if event.key == playerconfig['Backward'].lower():
            while True:
                previous_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                               idxlist=xlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Forward'].lower():
            while True:
                next_slice(ax, step=playerconfig['Interval'], pref='Crossline No. ', surf=titlesurf,
                           idxlist=xlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfig['First'].lower(), playerconfig['Previous'].lower(),
                             playerconfig['Backward'].lower(), playerconfig['Pause'].lower(),
                             playerconfig['Forward'].lower(), playerconfig['Next'].lower(),
                             playerconfig['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(8, 8))
    # ax.set_xticks(np.linspace(0, len(inlrange)-1, 6, dtype=int))
    # ax.set_xticklabels(np.linspace(inlstart, inlend, 6, dtype=int))
    # ax.set_yticks(np.linspace(0, len(zrange) - 1, 6, dtype=int))
    # ax.set_yticklabels(np.linspace(zstart, zend, 6, dtype=int))
    ax.set_xlabel('Inline No.')
    ax.set_ylabel('Vertical (z) Depth/Time')
    volume = np.transpose(seis3dmat, [1,0,2])
    ax.volume = volume
    ax.index = int((initxsl-xlstart)/xlstep)
    ax.set_title('Crossline No. ' + str(xlrange[ax.index]) + titlesurf)

    cat = ax.imshow(volume[ax.index],
                    # aspect=None,
                    aspect='auto', #float(len(inlrange))/float(len(zrange)),
                    extent=[inlstart, inlend, zend, zstart],
                    cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                    interpolation=interpolation,
                    vmin=valuemin, vmax=valuemax)
    if colorbaron:
        fig.colorbar(cat)
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('2D Window - Seismic Crossline')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisZSliceFrom2DMat(seis2dmat, zsls=None, datacol=3,
                            inlcol=0, xlcol=1, zcol=2,
                            colormap=None, flipcmap=False,
                            valuemin=-1.0, valuemax=1.0,
                            titlesurf='', colorbaron=False,
                            verbose=True):
    """
    Plot seismic z slices from 2D matrix (by matplotlib.imshow)

    Args:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        zsls:       depth/time No. for plotting
                    Plot all z slices if not specified
        datacol:    index of data column for plotting in 2D matrix (indexing from 0)
                    Plot the fourth column if not specified (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        verbose:    flag for message display. Default is True

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisZSliceFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisZSliceFrom2DMat: Not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisZSliceFrom2DMat: Not inline column found in 2D seismic matrix', 'error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisZSliceFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisZSliceFrom2DMat: Not z column found in 2D seismic matrix', type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zstep = seisinfo['ZStep']
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = -1

    if zsls is None:
        vis_msg.print('WARNING in plotSeisZSliceFrom2DMat: to plot all a slices in 2D seismic matrix', type='warning')
        zsls = zrange

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in plotSeisZSliceFrom2DMat: 1D array of z slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, inlrange)

    nzsls = len(zsls)
    if verbose:
        print('Plot ' + str(nzsls) + ' z slices')
    for i in range(nzsls):
        z = zsls[i]
        idx = np.round((z - zstart) / zstep).astype(np.int32)
        if idx >= 0 and idx < znum:
            seisdata = seis3dmat[idx, :, :]
            seisdata = seisdata.transpose()
            plt.figure(facecolor='white')
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([inlstart, inlend])
            plt.title('Depth/Time at ' + str(zrange[idx]) + titlesurf)
            plt.xlabel('Crossline No.')
            plt.ylabel('Inline No.')
            if colorbaron:
                plt.colorbar()
    plt.show()

    return


def plotSeisZSlicePlayerFrom2DMat(seis2dmat, initzsl=None, datacol=3,
                                  inlcol=0, xlcol=1, zcol=2,
                                  colormap=None, flipcmap=False,
                                  valuemin=-1.0, valuemax=1.0,
                                  titlesurf='', colorbaron=False,
                                  interpolation='bicubic',
                                  playerconfig=None,
                                  fontstyle=None,
                                  qicon=None
                                  ):
    """
    Plot seismic z slices from 2D matrix, as a player (by matplotlib.imshow)

    Args:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        initzsl:    initial depth/time No. for the player
                    Plot first z slices if not specified
        datacol:    index of data column for plotting in 2D matrix (indexing from 0)
                    Plot the fourth column if not specified (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        interpolation:  interpolation type. Default is 'bicubic'
        playerconfig:   Player configuration. Default is None
        fontstyle:      Font style object. Default is None
        qicon:      QIcon for plotting window. Default is None

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisZSlicePlayerFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisZSlicePlayerFrom2DMat: Not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisZSlicePlayerFrom2DMat: Not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisZSlicePlayerFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisZSlicePlayerFrom2DMat: Not z column found in 2D seismic matrix',
                      type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zstep = seisinfo['ZStep']
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = -1

    if initzsl is None:
        vis_msg.print('WARNING in plotSeisZSlicePlayerFrom2DMat: to be initizlied with the first slice',
                      type='warning')
        initzsl = zrange[0]

    if playerconfig is None:
        playerconfig = {}
        playerconfig['First'] = 'A'
        playerconfig['Previous'] = 'S'
        playerconfig['Backward'] = 'Q'
        playerconfig['Pause'] = 'P'
        playerconfig['Forward'] = 'W'
        playerconfig['Next'] = 'D'
        playerconfig['Last'] = 'F'
        playerconfig['Interval'] = 5

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfig['First'].lower():
            first_slice(ax, pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Previous'].lower():
            previous_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Next'].lower():
            next_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Last'].lower():
            last_slice(ax, pref='Depth/Time at ', surf=titlesurf,
                       idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Backward'].lower():
            while True:
                previous_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                               idxlist=zrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Forward'].lower():
            while True:
                next_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfig['First'].lower(), playerconfig['Previous'].lower(),
                             playerconfig['Backward'].lower(), playerconfig['Pause'].lower(),
                             playerconfig['Forward'].lower(), playerconfig['Next'].lower(),
                             playerconfig['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(8, 8))
    # ax.set_xticks(np.linspace(0, len(xlrange)-1, 6, dtype=int))
    # ax.set_xticklabels(np.linspace(xlstart, xlend, 6, dtype=int))
    # ax.set_yticks(np.linspace(0, len(inlrange) - 1, 6, dtype=int))
    # ax.set_yticklabels(np.linspace(inlend, inlstart, 6, dtype=int))
    ax.set_xlabel('Crossline No.')
    ax.set_ylabel('Inline No.')
    volume = np.transpose(seis3dmat, [0, 2, 1])
    volume = np.flip(volume, axis=1)
    ax.volume = volume
    ax.index = int((initzsl - zstart) / zstep)
    ax.set_title('Depth/Time at ' + str(zrange[ax.index]) + titlesurf)
    cat = ax.imshow(volume[ax.index],
                    aspect='auto', #float(len(xlrange))/float(len(inlrange)),
                    extent=[xlstart, xlend, inlstart, inlend],
                    cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                    interpolation=interpolation,
                    vmin=valuemin, vmax=valuemax)
    if colorbaron:
        fig.colorbar(cat)
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('2D Window - Seismic Time/depth')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisZTracePlayerFrom2DMat(seis2dmat, initinltc=None, initxltc=None,
                                  datacol=3, inlcol=0, xlcol=1, zcol=2,
                                  valuemin=-1.0, valuemax=1.0,
                                  color='blue', marker=None, linewidth=12, linestyle='solid',
                                  titlesurf='',
                                  playerconfiginl=None, playerconfigxl=None,
                                  fontstyle=None,
                                  qicon=None
                                  ):
    """
    Plot seismic waveform from 2D matrix, as a player (by matplotlib.imshow)

    Args:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        initinlno:  initial inline No. for player
                    Plot the first inline if not specified
        initxlno:   initial crossline No. for player
                    Plot the first crossline if not specified
        datacol:    index of data column for plotting in 2D matrix (Indexing from 0)
                    Use the fourth column if not specified (targetcol=3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        qicon:      QIcon for plotting window. Default is None

    Return:
        N/A
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in plotSeisZTracePlayerFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in plotSeisZTracePlayerFrom2DMat: Not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in plotSeisZTracePlayerFrom2DMat: Not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in plotSeisZTracePlayerFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in plotSeisZTracePlayerFrom2DMat: Not z column found in 2D seismic matrix', type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                             inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                 datacol=datacol,
                                                 inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if initinltc is None:
        vis_msg.print('WARNING in plotSeisZTracePlayerFrom2DMat: '
                      'to be initialized by the first inline trace in 2D seismic matrix', type='warning')
        initinltc = inlrange[0]
    if initxltc is None:
        vis_msg.print('WARNING in plotSeisZTracePlayerFrom2DMat: '
                      'to be initialized by the first crossline trace in 2D seismic matrix', type='warning')
        initxltc = xlrange[0]

    if playerconfiginl is None:
        playerconfiginl = {}
        playerconfiginl['First'] = 'A'
        playerconfiginl['Previous'] = 'S'
        playerconfiginl['Backward'] = 'Q'
        playerconfiginl['Pause'] = 'P'
        playerconfiginl['Forward'] = 'W'
        playerconfiginl['Next'] = 'D'
        playerconfiginl['Last'] = 'F'
        playerconfiginl['Interval'] = 5
    if playerconfigxl is None:
        playerconfigxl = {}
        playerconfigxl['First'] = chr(ord(playerconfiginl['First']) + 1)
        playerconfigxl['Previous'] = chr(ord(playerconfiginl['Previous']) + 1)
        playerconfigxl['Backward'] = chr(ord(playerconfiginl['Backward']) + 1)
        playerconfigxl['Pause'] = chr(ord(playerconfiginl['Pause']) + 1)
        playerconfigxl['Forward'] = chr(ord(playerconfiginl['Forward']) + 1)
        playerconfigxl['Next'] = chr(ord(playerconfiginl['Next']) + 1)
        playerconfigxl['Last'] = chr(ord(playerconfiginl['Last']) + 1)
        playerconfigxl['Interval'] = playerconfiginl['Interval']

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfiginl['First'].lower():
            first_trace_y(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                          idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Previous'].lower():
            previous_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Next'].lower():
            next_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Last'].lower():
            last_trace_y(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Backward'].lower():
            while True:
                previous_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ',
                                 surf='',
                                 idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfiginl['Forward'].lower():
            while True:
                next_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfiginl['Pause'].lower():
            plt.pause(0)
        #
        if event.key == playerconfigxl['First'].lower():
            first_trace_x(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                          idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Previous'].lower():
            previous_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Next'].lower():
            next_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Last'].lower():
            last_trace_x(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Backward'].lower():
            while True:
                previous_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ',
                                 surf='',
                                 idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfigxl['Forward'].lower():
            while True:
                next_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfigxl['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfiginl['First'].lower(), playerconfiginl['Previous'].lower(),
                             playerconfiginl['Backward'].lower(), playerconfiginl['Pause'].lower(),
                             playerconfiginl['Forward'].lower(), playerconfiginl['Next'].lower(),
                             playerconfiginl['Last'].lower(),
                             playerconfigxl['First'].lower(), playerconfigxl['Previous'].lower(),
                             playerconfigxl['Backward'].lower(), playerconfigxl['Pause'].lower(),
                             playerconfigxl['Forward'].lower(), playerconfigxl['Next'].lower(),
                             playerconfigxl['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(10, 5))
    ax.set_xlabel('Vertical (z) Depth/Time')
    ax.set_xlim(zrange[-1], zrange[0])
    ax.set_ylim(valuemin, valuemax)
    volume = np.reshape(np.transpose(seis3dmat, [0, 2, 1]), [-1, inlnum*xlnum])
    ax.volume = volume
    inlidx = int((initinltc-inlstart)/inlstep)
    xlidx = int((initxltc-xlstart)/xlstep)
    ax.index = inlidx * xlnum + xlidx
    ax.set_title(titlesurf + '(' + str(inlrange[inlidx]) + ', ' + str(xlrange[xlidx]) + ')')
    #
    ax.plot(zrange, volume[:, ax.index],
            color=color, marker=marker, linewidth=linewidth, linestyle=linestyle)
    ax.invert_xaxis()
    #
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('1D Window - Seismic Waveform')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisZSliceFrom3DMat(seis3dmat, zsls=None, seisinfo=None,
                            colormap=None, flipcmap=False,
                            valuemin=-1.0, valuemax=1.0,
                            titlesurf='', colorbaron=False,
                            verbose=True):
    """
    Plot seismic z slices from 3D matrix (by matplotlib.imshow)

    Args:
        seis3dmat:  3D matrix representing seismic data [Z/XL/IL]
        zsls:       depth/time No. for plotting
                    Plot all z slices if not specified
        seisinfo:   basic information of 3D seismic survey
                    Auto-generated from 3D matrix if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        titlesurf:  surfix for the title. Default is blank
        colorbaron: colorbar display. Default is false
        verbose:    flag for message display. Default is True

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisZSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisZSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zstep = seisinfo['ZStep']
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = -1

    if zsls is None:
        vis_msg.print('WARNING in plotSeisZSliceFrom3DMat: to plot all z sections in 3D seismic matrix',
                      type='warning')
        zsls = zrange

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in plotSeisZSliceFrom3DMat: 1D array of z slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, inlrange)

    nzsls = len(zsls)
    if verbose:
        print('Plot ' + str(nzsls) + ' z slices')
    for i in range(nzsls):
        z = zsls[i]
        idx = np.round((z - zstart) / zstep).astype(np.int32)
        if idx >= 0 and idx < znum:
            seisdata = seis3dmat[idx, :, :]
            seisdata = seisdata.transpose()
            plt.figure(facecolor='white')
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([inlstart, inlend])
            plt.title('Depth/Time at ' + str(zrange[idx]) + titlesurf)
            plt.xlabel('Crossline No.')
            plt.ylabel('Inline No.')
            if colorbaron:
                plt.colorbar()
    plt.show()

    return


def plotSeisZSlicePlayerFrom3DMat(seis3dmat, initzsl=None, seisinfo=None,
                                  colormap=None, flipcmap=False,
                                  valuemin=-1.0, valuemax=1.0,
                                  titlesurf='', colorbaron=False,
                                  interpolation='bicubic',
                                  playerconfig=None,
                                  fontstyle=None,
                                  qicon=None
                                  ):
    """
    Plot seismic z slices from 3D matrix, as a player (by matplotlib.imshow)

    Args:
        seis3dmat:      3D matrix representing seismic data
        colormap:       colormap name for seismic data visualization, such as 'seismic'
                        Use the default colormap by vis_cmap.makeColorMap if not specified
        valuemin:       lower limit for seismic data visualization. Default is -1.0
        valuemax:       upper limit for seismic data visualization. Default is 1.0
        titlesurf:      surfix for the title. Default is blank
        colorbaron:     colorbar display. Default is false
        interpolation:  interpolation type. Default is 'bicubic'
        playerconfig:   Player configuration. Default is None
        fontstyle:      Font style object. Default is None
        qicon:          QIcon for plotting window. Default is None

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisZSlicePlayerFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisZSlicePlayerFrom3DMat: SeisInfo automatically generated', type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zstep = seisinfo['ZStep']
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = -1

    if initzsl is None:
        vis_msg.print('WARNING in plotSeisZSlicePlayerFrom2DMat: to be initizlied with the first slice',
                      type='warning')
        initzsl = zrange[0]

    if playerconfig is None:
        playerconfig = {}
        playerconfig['First'] = 'A'
        playerconfig['Previous'] = 'S'
        playerconfig['Backward'] = 'Q'
        playerconfig['Pause'] = 'P'
        playerconfig['Forward'] = 'W'
        playerconfig['Next'] = 'D'
        playerconfig['Last'] = 'F'
        playerconfig['Interval'] = 5

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfig['First'].lower():
            first_slice(ax, pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Previous'].lower():
            previous_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Next'].lower():
            next_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Last'].lower():
            last_slice(ax, pref='Depth/Time at ', surf=titlesurf,
                       idxlist=zrange)
            fig.canvas.draw()
        if event.key == playerconfig['Backward'].lower():
            while True:
                previous_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                               idxlist=zrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Forward'].lower():
            while True:
                next_slice(ax, step=playerconfig['Interval'], pref='Depth/Time at ', surf=titlesurf,
                           idxlist=zrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfig['Pause'].lower():
            plt.pause(0)


    remove_keymap_conflicts({playerconfig['First'].lower(), playerconfig['Previous'].lower(),
                             playerconfig['Backward'].lower(), playerconfig['Pause'].lower(),
                             playerconfig['Forward'].lower(), playerconfig['Next'].lower(),
                             playerconfig['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(8, 8))
    # ax.set_xticks(np.linspace(0, len(xlrange)-1, 6, dtype=int))
    # ax.set_xticklabels(np.linspace(xlstart, xlend, xlnum, dtype=int))
    # ax.set_yticks(np.linspace(0, len(inlrange) - 1, 6, dtype=int))
    # ax.set_yticklabels(np.linspace(inlend, inlstart, inlnum, dtype=int))
    ax.set_xlabel('Crossline No.')
    ax.set_ylabel('Inline No.')
    volume = np.transpose(seis3dmat, [0, 2, 1])
    volume = np.flip(volume, axis=1)
    ax.volume = volume
    ax.index = int((initzsl - zstart) / zstep)
    ax.set_title('Depth/Time at ' + str(zrange[ax.index]) + titlesurf)
    cat = ax.imshow(volume[ax.index],
                    aspect='auto', #float(len(xlrange))/float(len(inlrange)),
                    extent=[xlstart, xlend, inlstart, inlend],
                    cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                    interpolation=interpolation,
                    vmin=valuemin, vmax=valuemax)
    if colorbaron:
        fig.colorbar(cat)
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('2D Window - Seismic Time/depth')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisZTracePlayerFrom3DMat(seis3dmat, initinltc=None, initxltc=None,
                                  seisinfo=None,
                                  valuemin=-1.0, valuemax=1.0,
                                  color='blue', markerstyle=None, markersize=12,
                                  linewidth=12, linestyle='solid',
                                  titlesurf='',
                                  playerconfiginl=None, playerconfigxl=None,
                                  fontstyle=None,
                                  qicon=None
                                  ):
    """
    Plot seismic waveform from 3D matrix, as a player (by matplotlib.imshow)

    Args:
        seis3dmat:          2D matrix representing seismic data
        initial:            inline No. for player
                            Plot the first inline if not specified
        initxltc:           initial crossline No. for player
                            Plot the first crossline if not specified
        valuemin:           lower limit for seismic data visualization. Default is -1.0
        valuemax:           upper limit for seismic data visualization. Default is 1.0
        titlesurf:          surfix for the title. Default is blank
        playerconfiginl:    Player configuration for inline direction. Default is None
        playerconfigxl:     Player configuration for xline direction. Default is None
        fontstyle:          Font style object. Default is None
        qicon:              QIcon for plotting window. Default is None

    Return:
        N/A
    """

    # Check input matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisZTracePlayerFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisZTracePlayerFrom3DMat: SeisInfo automatically generated', type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if initinltc is None:
        vis_msg.print('WARNING in plotSeisZTracePlayerFrom2DMat: '
                      'to be initialized by the first inline trace in 2D seismic matrix', type='warning')
        initinltc = inlrange[0]
    if initxltc is None:
        vis_msg.print('WARNING in plotSeisZTracePlayerFrom2DMat: '
                      'to be initialized by the first crossline trace in 2D seismic matrix', type='warning')
        initxltc = xlrange[0]

    if playerconfiginl is None:
        playerconfiginl = {}
        playerconfiginl['First'] = 'A'
        playerconfiginl['Previous'] = 'S'
        playerconfiginl['Backward'] = 'Q'
        playerconfiginl['Pause'] = 'P'
        playerconfiginl['Forward'] = 'W'
        playerconfiginl['Next'] = 'D'
        playerconfiginl['Last'] = 'F'
        playerconfiginl['Interval'] = 5
    if playerconfigxl is None:
        playerconfigxl = {}
        for _k in playerconfiginl.keys():
            if _k != 'Interval':
                playerconfigxl[_k] = chr(ord(playerconfiginl[_k]) + 1)
            else:
                playerconfigxl[_k] = playerconfiginl[_k]

    def process_key(event):
        fig = event.canvas.figure
        ax = fig.axes[0]
        if event.key == playerconfiginl['First'].lower():
            first_trace_y(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                          idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Previous'].lower():
            previous_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Next'].lower():
            next_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Last'].lower():
            last_trace_y(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfiginl['Backward'].lower():
            while True:
                previous_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ',
                                 surf='',
                                 idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfiginl['Forward'].lower():
            while True:
                next_trace_y(ax, [xlnum, inlnum], step_y=playerconfiginl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfiginl['Pause'].lower():
            plt.pause(0)
        #
        if event.key == playerconfigxl['First'].lower():
            first_trace_x(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                          idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Previous'].lower():
            previous_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Next'].lower():
            next_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Last'].lower():
            last_trace_x(ax, [xlnum, inlnum], pref=titlesurf + ' at ', surf='',
                         idxlist_x=xlrange, idxlist_y=inlrange)
            fig.canvas.draw()
        if event.key == playerconfigxl['Backward'].lower():
            while True:
                previous_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ',
                                 surf='',
                                 idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfigxl['Forward'].lower():
            while True:
                next_trace_x(ax, [xlnum, inlnum], step_x=playerconfigxl['Interval'], pref=titlesurf + ' at ', surf='',
                             idxlist_x=xlrange, idxlist_y=inlrange)
                fig.canvas.draw()
                plt.pause(0.2)
        if event.key == playerconfigxl['Pause'].lower():
            plt.pause(0)

    remove_keymap_conflicts({playerconfiginl['First'].lower(), playerconfiginl['Previous'].lower(),
                             playerconfiginl['Backward'].lower(), playerconfiginl['Pause'].lower(),
                             playerconfiginl['Forward'].lower(), playerconfiginl['Next'].lower(),
                             playerconfiginl['Last'].lower(),
                             playerconfigxl['First'].lower(), playerconfigxl['Previous'].lower(),
                             playerconfigxl['Backward'].lower(), playerconfigxl['Pause'].lower(),
                             playerconfigxl['Forward'].lower(), playerconfigxl['Next'].lower(),
                             playerconfigxl['Last'].lower()})

    #
    vis_font.updatePltFont(fontstyle)
    #
    fig, ax = plt.subplots(facecolor='white', figsize=(10, 5))
    ax.set_xlabel('Vertical (z) Depth/Time')
    ax.set_xlim(zrange[-1], zrange[0])
    ax.set_ylim(valuemin, valuemax)
    volume = np.reshape(np.transpose(seis3dmat, [0, 2, 1]), [-1, inlnum*xlnum])
    ax.volume = volume
    inlidx = int((initinltc-inlstart)/inlstep)
    xlidx = int((initxltc-xlstart)/xlstep)
    ax.index = inlidx * xlnum + xlidx
    ax.set_title(titlesurf + '(' + str(inlrange[inlidx]) + ', ' + str(xlrange[xlidx]) + ')')
    #
    ax.plot(zrange, volume[:, ax.index],
            color=color, marker=markerstyle, markersize=markersize,
            linewidth=linewidth, linestyle=linestyle)
    ax.invert_xaxis()
    #
    fig.canvas.mpl_connect('key_press_event', process_key)
    if qicon is not None:
        fig.canvas.set_window_title('1D Window - Seismic Waveform')
        #
        # Commented by HD on June 7, 2018 to avoid crash
        # plt.get_current_fig_manager().window.setWindowIcon(qicon)
    plt.show()

    return


def plotSeisILXLZSliceFrom3DMat(seis3dmat, inlsls=None, xlsls=None, zsls=None,
                                seisinfo=None,
                                colormap=None, flipcmap=False, interpolation='bicubic', zscale=1.0,
                                valuemin=-1.0, valuemax=1.0, surveyboxon=True,
                                viewerconfig=None,
                                verbose=True):
    """
    Plot seismic inline, crossline, and z slices from 3D matrix (by vispy.Image)

    Args:
        seis3dmat:      3D matrix representing seismic data [Z/XL/IL]
        inlsls:         inline No. for plotting
                        The middle inline slice if not specified
        xlsls:          crossline No. for plotting
                        The middle crossline slice if not specified
        zsls:           z No. for plotting
                        The middle z slice if not specified
        seisinfo:       basic information of 3D seismic survey
                        Auto-generated from 3D matrix if not specified
        colormap:       colormap name for seismic data visualization, such as 'seismic'
                        Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:       Flip colormap. Default is False
        interpolation:  interpolation type. Default is 'bicubic'
        valuemin:       lower limit for seismic data visualization. Default is -1.0
        valuemax:       upper limit for seismic data visualization. Default is 1.0
        zscale:         ratio of z vs. horizontal
        viewerconfig:   viewer configuration. Default is None.
        surveyboxon:    Survey box on or not. Default is True
        verbose:        flag for message display. Default is True

    Return:
        N/A
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisILXLZSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisILXLZSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    if viewerconfig is None:
        viewerconfig = {}
        viewerconfig['All'] = 'A'
        viewerconfig['Inline'] = 'I'
        viewerconfig['Crossline'] = 'X'
        viewerconfig['Z'] = 'Z'

    def process_key(event):
        if event.key == viewerconfig['All'].lower():
            cam = scene.TurntableCamera(elevation=30, azimuth=135)
            view.camera = cam
        if event.key == viewerconfig['Inline'].lower() :
            cam = scene.TurntableCamera(elevation=0, azimuth=0)
            view.camera = cam
        if event.key == viewerconfig['Crossline'].lower():
            cam = scene.TurntableCamera(elevation=0, azimuth=90)
            view.camera = cam
        if event.key == viewerconfig['Z'].lower():
            cam = scene.TurntableCamera(elevation=90, azimuth=0)
            view.camera = cam

    remove_keymap_conflicts({viewerconfig['All'].lower(), viewerconfig['Inline'].lower(),
                             viewerconfig['Crossline'].lower(), viewerconfig['Z'].lower()})

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange'] * zscale
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart'] * zscale
    zend = seisinfo['ZEnd'] * zscale
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1
    zstep = seisinfo['ZStep'] * zscale
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = 1

    if inlsls is None:
        vis_msg.print('WARNING in plotSeisILXLZSliceFrom3DMat: to plot the middle inline slice in 3D seismic matrix',
                      type='warning')
        inlsls = inlrange[int(inlnum/2):int(inlnum/2)+1]

    if xlsls is None:
        vis_msg.print('WARNING in plotSeisILXLZSliceFrom3DMat: to plot the middle crossline slice in 3D seismic matrix',
                      type='warning')
        xlsls = xlrange[int(xlnum/2):int(xlnum/2)+1]

    if zsls is None:
        vis_msg.print('WARNING in plotSeisILXLZSliceFrom3DMat: to plot the middle z slice in 3D seismic matrix',
                      type='warning')
        zsls = zrange[int(znum/2):int(znum/2)+1]

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in plotSeisILXLZSliceFrom3DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in plotSeisILXLZSliceFrom3DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in plotSeisILXLZSliceFrom3DMat: 1D array of z slices expected', type='error')
        sys.exit()

    # Create a canvas with a 3D viewport
    canvas = scene.SceneCanvas(keys='interactive', title='vispy', bgcolor=[0.5, 0.5, 0.5])
    view = canvas.central_widget.add_view()

    # add box
    if surveyboxon:
        for p in ([xlstart, inlstart, zend, xlend, inlstart, zend],
                  [xlstart, inlstart, zend, xlstart, inlend, zend],
                  [xlstart, inlstart, zend, xlstart, inlstart, zstart],
                  [xlstart, inlend, zstart, xlend, inlend, zstart],
                  [xlend, inlstart, zstart, xlend, inlend, zstart],
                  [xlend, inlend, zend, xlend, inlend, zstart],
                  [xlend, inlstart, zend, xlend, inlend, zend],
                  [xlstart, inlend, zend, xlend, inlend, zend],
                  [xlstart, inlend, zend, xlstart, inlend, zstart],
                  [xlstart, inlstart, zstart, xlstart, inlend, zstart],
                  [xlend, inlstart, zend, xlend, inlstart, zstart],
                  [xlstart, inlstart, zstart, xlend, inlstart, zstart]):
            line = scene.visuals.Line(pos=np.array([[p[0], p[1], p[2]],
                                                    [p[3], p[4], p[5]]]),
                                      color='black',
                                      parent=view.scene)

    cmp = vis_cmap.makeColorMap(colormap, flipcmap)
    cmp = Colormap(cmp.colors)

    if interpolation is None or interpolation =='None' or interpolation == 'none':
        interpolation = 'nearest'

    # Create inline slice visual
    ninlsls = len(inlsls)
    if verbose:
        print('Plot ' + str(ninlsls) + ' inline slices')
    for i in range(ninlsls):
        inl = inlsls[i]
        idx = np.round((inl - inlstart) / inlstep).astype(np.int32)
        if idx >= 0 and idx < inlnum:
            seisdata = seis3dmat[:, :, idx]
            #
            slice_inl = scene.visuals.Image(seisdata, parent=view.scene, grid=(zscale*znum, xlnum),
                                            cmap=cmp, clim=(valuemin, valuemax),
                                            interpolation=interpolation)
            tr_inl = scene.transforms.MatrixTransform()
            tr_inl.scale((1, zscale))
            tr_inl.rotate(-90, (1, 0, 0))
            # tr_inl.rotate(90, (0, 0, 1))
            tr_inl.translate((xlstart, inl, zstart))
            slice_inl.transform = tr_inl

    # Create crossline slice visual
    nxlsls = len(xlsls)
    if verbose:
        print('Plot ' + str(nxlsls) + ' crossline slices')
    for i in range(nxlsls):
        xl = xlsls[i]
        idx = np.round((xl - xlstart) / xlstep).astype(np.int32)
        if idx >= 0 and idx < xlnum:
            seisdata = seis3dmat[:, idx, :]
            #
            slice_xl = scene.visuals.Image(seisdata, parent=view.scene,
                                           cmap=cmp, clim=(valuemin, valuemax),
                                           interpolation=interpolation)
            tr_xl = scene.transforms.MatrixTransform()
            tr_xl.scale((1, zscale))
            tr_xl.rotate(-90, (1, 0, 0))
            tr_xl.rotate(90, (0, 0, 1))
            tr_xl.translate((xl, inlstart, zstart))
            slice_xl.transform = tr_xl

    # Create z slice visual
    nzsls = len(zsls)
    if verbose:
        print('Plot ' + str(nzsls) + ' z slices')
    for i in range(nzsls):
        z = zsls[i]
        idx = np.round((z - zstart) / zstep).astype(np.int32)
        if idx >= 0 and idx < znum:
            seisdata = seis3dmat[idx, :, :]
            #
            slice_z = scene.visuals.Image(seisdata, parent=view.scene,
                                          cmap=cmp, clim=(valuemin, valuemax),
                                          interpolation=interpolation)
            tr_z = scene.transforms.MatrixTransform()
            tr_z.rotate(90, (0, 0, 1))
            tr_z.rotate(180, (0, 1, 0))
            tr_z.translate((xlstart, inlstart, z))
            slice_z.transform = tr_z

    # Add a 3D axis to keep us oriented
    axis = scene.visuals.XYZAxis(parent=view.scene)

    # Use a 3D camera
    # Manual bounds; Mesh visual does not provide bounds yet
    # Note how you can set bounds before assigning the camera to the viewbox
    cam = scene.TurntableCamera(elevation=30, azimuth=135)
    cam.set_range((xlstart, xlend), (inlstart, inlend), (zend, zstart))
    view.camera = cam

    canvas.events.key_press.connect(process_key)

    canvas.show()
    if sys.flags.interactive == 0:
        app.run()

    return


def plotSeisILXLZSlicePlayerFrom3DMat(seis3dmat, initinlsl=None, initxlsl=None, initzsl=None,
                                      seisinfo=None,
                                      colormap=None, flipcmap=False, interpolation='bicubic', zscale=1.0,
                                      valuemin=-1.0, valuemax=1.0, surveyboxon=True,
                                      viewerconfig=None,
                                      playerconfiginl=None, playerconfigxl=None, playerconfigz=None,
                                      qicon=None
                                      ):
    """
    Plot seismic inline, crossline, and z slices from 3D matrix (by vispy.Image)

    Args:
        seis3dmat:          3D matrix representing seismic data [Z/XL/IL]
        initinlsl:          initial inline No. for plotting
                            The middle inline slice if not specified
        initxlsl:           initial crossline No. for plotting
                            The middle crossline slice if not specified
        initzsl:            z No. for plotting
                            The middle z slice if not specified
        seisinfo:           basic information of 3D seismic survey
                            Auto-generated from 3D matrix if not specified
        colormap:           colormap name for seismic data visualization, such as 'seismic'
                            Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:           Flip colormap. Default is False
        valuemin:           lower limit for seismic data visualization. Default is -1.0
        valuemax:           upper limit for seismic data visualization. Default is 1.0
        interpolation:      interpolation type. Default is 'bicubic'
        zscale:             ratio of z vs. horizontal
        viewerconfig:       viewer configuration. Default is None.
        surveyboxon:        Survey box on or not. Default is True
        playerconfiginl:    player configuration along inline. Default is None
        playerconfigxl:     player configuration along xline. Default is None
        playerconfigz:      player configuration along z. Default is None
        verbose:            flag for message display. Default is True

    Return:
        N/A
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in plotSeisILXLZSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in plotSeisILXLZSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    if viewerconfig is None:
        viewerconfig = {}
        viewerconfig['Home'] = 'U'
        viewerconfig['Inline'] = 'I'
        viewerconfig['Crossline'] = 'X'
        viewerconfig['Z'] = 'Z'

    if playerconfiginl is None:
        playerconfiginl = {}
        playerconfiginl['First'] = 'A'
        playerconfiginl['Previous'] = 'S'
        playerconfiginl['Next'] = 'D'
        playerconfiginl['Last'] = 'F'
        playerconfiginl['Backward'] = 'Q'
        playerconfiginl['Forward'] = 'W'
        playerconfiginl['Pause'] = 'P'
        playerconfiginl['Interval'] = 5

    if playerconfigxl is None:
        playerconfigxl = {}
        playerconfigxl['First'] = 'G'
        playerconfigxl['Previous'] = 'H'
        playerconfigxl['Next'] = 'J'
        playerconfigxl['Last'] = 'K'
        playerconfigxl['Backward'] = 'E'
        playerconfigxl['Forward'] = 'R'
        playerconfigxl['Pause'] = 'P'
        playerconfigxl['Interval'] = 5

    if playerconfigz is None:
        playerconfigz = {}
        playerconfigz['First'] = 'C'
        playerconfigz['Previous'] = 'V'
        playerconfigz['Next'] = 'B'
        playerconfigz['Last'] = 'N'
        playerconfigz['Backward'] = 'T'
        playerconfigz['Forward'] = 'Y'
        playerconfigz['Pause'] = 'P'
        playerconfigz['Interval'] = 5

    remove_keymap_conflicts({viewerconfig['Home'].lower(), viewerconfig['Inline'].lower(),
                             viewerconfig['Crossline'].lower(), viewerconfig['Z'].lower()})
    remove_keymap_conflicts({playerconfiginl['First'].lower(), playerconfiginl['Previous'].lower(),
                             playerconfiginl['Next'].lower(), playerconfiginl['Last'].lower(),
                             playerconfiginl['Backward'].lower(), playerconfiginl['Forward'].lower(),
                             playerconfiginl['Pause'].lower()})
    remove_keymap_conflicts({playerconfigxl['First'].lower(), playerconfigxl['Previous'].lower(),
                             playerconfigxl['Next'].lower(), playerconfigxl['Last'].lower(),
                             playerconfigxl['Backward'].lower(), playerconfigxl['Forward'].lower(),
                             playerconfigxl['Pause'].lower()})
    remove_keymap_conflicts({playerconfigz['First'].lower(), playerconfigz['Previous'].lower(),
                             playerconfigz['Next'].lower(), playerconfigz['Last'].lower(),
                             playerconfigz['Backward'].lower(), playerconfigz['Forward'].lower(),
                             playerconfigz['Pause'].lower()})

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange'] * zscale
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart'] * zscale
    zend = seisinfo['ZEnd'] * zscale
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1
    zstep = seisinfo['ZStep'] * zscale
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = 1

    if initzsl is not None:
        initzsl = initzsl * zscale


    class current_slice:
        def __init__(self):
            self.inl = 0
            self.xl = 0
            self.z = 0

    # Create a canvas with a 3D viewport
    canvas = scene.SceneCanvas(keys='interactive', title='3D seismic', bgcolor=[0.5, 0.5, 0.5],
                               size=(1000, 800), app='pyqt5')
    view = canvas.central_widget.add_view()

    # add box
    if surveyboxon:
        for p in ([xlstart - 0.5 * xlstep, inlstart - 0.5 * inlstep, zend + 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlstart - 0.5 * inlstep, zend + 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlstart - 0.5 * inlstep, zend + 0.5 * zstep, xlstart - 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zend + 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlstart - 0.5 * inlstep, zend + 0.5 * zstep, xlstart - 0.5 * xlstep,
                   inlstart - 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlend + 0.5 * inlstep, zstart - 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlend + 0.5 * xlstep, inlstart - 0.5 * inlstep, zstart - 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlend + 0.5 * xlstep, inlend + 0.5 * inlstep, zend + 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlend + 0.5 * xlstep, inlstart - 0.5 * inlstep, zend + 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zend + 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlend + 0.5 * inlstep, zend + 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zend + 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlend + 0.5 * inlstep, zend + 0.5 * zstep, xlstart - 0.5 * xlstep,
                   inlend + 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlstart - 0.5 * inlstep, zstart - 0.5 * zstep,
                   xlstart - 0.5 * xlstep, inlend + 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlend + 0.5 * xlstep, inlstart - 0.5 * inlstep, zend + 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlstart - 0.5 * inlstep, zstart - 0.5 * zstep],
                  [xlstart - 0.5 * xlstep, inlstart - 0.5 * inlstep, zstart - 0.5 * zstep, xlend + 0.5 * xlstep,
                   inlstart - 0.5 * inlstep, zstart - 0.5 * zstep]):
            scene.visuals.Line(pos=np.array([[p[0], p[1], p[2]], [p[3], p[4], p[5]]]),
                               color='black',
                               parent=view.scene)

    cmp = vis_cmap.makeColorMap(colormap, flipcmap)
    cmp = Colormap(cmp.colors)

    if interpolation is None or interpolation =='None' or interpolation == 'none':
        interpolation = 'nearest'

    current_slices = current_slice()
    current_slices.inl = None
    current_slices.xl = None
    current_slices.z = None

    # Create inline slice visual
    current_inl = initinlsl
    if current_inl is not None:
        idx = np.round((current_inl - inlstart) / inlstep).astype(np.int32)
        if idx >= 0 and idx < inlnum and znum > 1 and xlnum > 1:
            seisdata = seis3dmat[:, :, idx]
            #
            slice_inl = scene.visuals.Image(seisdata, parent=view.scene,
                                            cmap=cmp, clim=(valuemin, valuemax),
                                            interpolation=interpolation)
            tr_inl = scene.transforms.MatrixTransform()
            tr_inl.scale((abs(xlstep), abs(zstep)))
            tr_inl.rotate(-90, (1, 0, 0))
            tr_inl.translate((xlstart, current_inl, zstart))
            tr_inl.translate((-0.5*xlstep, 0, -0.5*zstep))
            slice_inl.transform = tr_inl
            #
            current_slices.inl = inlstart + idx * inlstep

    # Create crossline slice visual
    current_xl = initxlsl
    if current_xl is not None:
        idx = np.round((current_xl - xlstart) / xlstep).astype(np.int32)
        if idx >= 0 and idx < xlnum and znum > 1 and inlnum > 1:
            seisdata = seis3dmat[:, idx, :]
            #
            slice_xl = scene.visuals.Image(seisdata, parent=view.scene,
                                           cmap=cmp, clim=(valuemin, valuemax),
                                           interpolation=interpolation)
            tr_xl = scene.transforms.MatrixTransform()
            tr_xl.scale((abs(inlstep), abs(zstep)))
            tr_xl.rotate(-90, (1, 0, 0))
            tr_xl.rotate(90, (0, 0, 1))
            tr_xl.translate((current_xl, inlstart, zstart))
            tr_xl.translate((0, -0.5*inlstep, -0.5*zstep))
            slice_xl.transform = tr_xl
            #
            current_slices.xl = xlstart + idx * xlstep

    # Create z slice visual
    current_z = initzsl
    if current_z is not None:
        idx = np.round((current_z - zstart) / zstep).astype(np.int32)
        if idx >= 0 and idx < znum and inlnum > 1 and xlnum > 1:
            seisdata = seis3dmat[idx, :, :]
            #
            slice_z = scene.visuals.Image(seisdata, parent=view.scene,
                                          cmap=cmp, clim=(valuemin, valuemax),
                                          interpolation=interpolation)
            tr_z = scene.transforms.MatrixTransform()
            tr_z.scale((abs(inlstep), abs(xlstep)))
            tr_z.rotate(90, (0, 0, 1))
            tr_z.rotate(180, (0, 1, 0))
            tr_z.translate((xlstart, inlstart, current_z))
            tr_z.translate((-0.5*xlstep, -0.5*inlstep, 0))
            slice_z.transform = tr_z
            #
            current_slices.z = zstart + idx * zstep


    # Add a 3D axis to keep us oriented
    _x0 = 0.5 * (xlstart + xlend) # xlstart
    _y0 = 0.5 * (inlstart + inlend) #inlend + inlend - inlstart
    _z0 = 0.5 * (zstart + zend) #zend + zend - zstart
    _len = np.max(np.abs(np.array([xlstep, inlstep, zstep])))
    xyzaxis = scene.visuals.XYZAxis(parent=view.scene,
                                    pos=np.array([[_x0, _y0, _z0], [_x0 + _len, _y0, _z0],
                                                  [_x0, _y0, _z0], [_x0, _y0 + _len, _z0],
                                                  [_x0, _y0, _z0], [_x0, _y0, _z0 - _len]]))

    # Use a 3D camera
    # Manual bounds; Mesh visual does not provide bounds yet
    # Note how you can set bounds before assigning the camera to the viewbox
    cam = scene.TurntableCamera(elevation=30, azimuth=135)
    cam.set_range((xlstart, xlend), (inlstart, inlend), (zend, zstart))
    view.camera = cam

    # add text
    # inline - crossline - z info
    text_inlxlz = scene.visuals.Text('( , , )', parent=canvas.scene, color='black')
    text_inlxlz.text = '( '
    if current_slices.inl is not None:
        text_inlxlz.text = text_inlxlz.text + str(current_slices.inl)
    text_inlxlz.text = text_inlxlz.text + ', '
    if current_slices.xl is not None:
        text_inlxlz.text = text_inlxlz.text + str(current_slices.xl)
    text_inlxlz.text = text_inlxlz.text + ', '
    if current_slices.z is not None:
        text_inlxlz.text = text_inlxlz.text + str(int(current_slices.z/zscale))
    text_inlxlz.text = text_inlxlz.text + ' )'
    text_inlxlz.font_size = 5
    text_inlxlz.pos = (view.canvas.size[0]-100, view.canvas.size[1]-20)

    if qicon is not None:
        canvas.title = '3D Window - Seismic'

    def press_key(event):
        # viewer
        if event.key == viewerconfig['Home'].lower():
            cam = scene.TurntableCamera(elevation=30, azimuth=135)
            cam.set_range((xlstart, xlend), (inlstart, inlend), (zend, zstart))
            view.camera = cam
        if event.key == viewerconfig['Inline'].lower():
            cam = scene.TurntableCamera(elevation=0, azimuth=0)
            cam.set_range((xlstart, xlend), (inlstart, inlend), (zend, zstart))
            view.camera = cam
        if event.key == viewerconfig['Crossline'].lower():
            cam = scene.TurntableCamera(elevation=0, azimuth=90)
            cam.set_range((xlstart, xlend), (inlstart, inlend), (zend, zstart))
            view.camera = cam
        if event.key == viewerconfig['Z'].lower():
            cam = scene.TurntableCamera(elevation=90, azimuth=0)
            cam.set_range((xlstart, xlend), (inlstart, inlend), (zend, zstart))
            view.camera = cam
        # player - inline
        if event.key == playerconfiginl['First'].lower():
            current_inl = current_slices.inl
            if current_inl is not None and znum > 1 and xlnum > 1:
                idx = ((current_inl - inlstart) / inlstep).astype(np.int32)
                tr_inl.translate((0, -current_inl, 0))
                slice_inl.set_data(seis3dmat[:, :, 0])
                tr_inl.translate((0, inlstart, 0))
                current_slices.inl = inlstart
        if event.key == playerconfiginl['Previous'].lower():
            current_inl = current_slices.inl
            if current_inl is not None and znum > 1 and xlnum > 1:
                idx = ((current_inl - inlstart) / inlstep).astype(np.int32)
                tr_inl.translate((0, -current_inl, 0))
                idx = (idx - playerconfiginl['Interval']) % inlnum
                slice_inl.set_data(seis3dmat[:, :, idx])
                tr_inl.translate((0, inlrange[idx], 0))
                current_slices.inl = inlrange[idx]
        if event.key == playerconfiginl['Next'].lower():
            current_inl = current_slices.inl
            if current_inl is not None and znum > 1 and xlnum > 1:
                idx = ((current_inl - inlstart) / inlstep).astype(np.int32)
                tr_inl.translate((0, -current_inl, 0))
                idx = (idx + playerconfiginl['Interval']) % inlnum
                slice_inl.set_data(seis3dmat[:, :, idx])
                tr_inl.translate((0, inlrange[idx], 0))
                current_slices.inl = inlrange[idx]
        if event.key == playerconfiginl['Last'].lower():
            current_inl = current_slices.inl
            if current_inl is not None and znum > 1 and xlnum > 1:
                idx = ((current_inl - inlstart) / inlstep).astype(np.int32)
                tr_inl.translate((0, -current_inl, 0))
                slice_inl.set_data(seis3dmat[:, :, -1])
                tr_inl.translate((0, inlend, 0))
                current_slices.inl = inlend
        if event.key == playerconfiginl['Backward'].lower():
            print(playerconfiginl['Backward'].lower() + ' not implemented yet !')
            # while True:
            #     current_inl = current_slices.inl
            #     if current_inl is not None and znum > 1 and xlnum > 1:
            #         idx = ((current_inl - inlstart) / inlstep).astype(np.int32)
            #         tr_inl.translate((0, -current_inl, 0))
            #         tr_inl.translate((0, -idx*d_inl, 0))
            #         idx = (idx - playerconfiginl['Interval']) % inlnum
            #         slice_inl.set_data(seis3dmat[:, :, idx])
            #         tr_inl.translate((0, inlrange[idx], 0))
            #         tr_inl.translate((0, idx*d_inl, 0))
            #         current_slices.inl = inlrange[idx]
            #         canvas.app.sleep(0.2)
        if event.key == playerconfiginl['Forward'].lower():
            print(playerconfiginl['Forward'].lower() + ' not implemented yet !')
            # while True:
            #     current_inl = current_slices.inl
            #     if current_inl is not None and znum > 1 and xlnum > 1:
            #         idx = ((current_inl - inlstart) / inlstep).astype(np.int32)
            #         tr_inl.translate((0, -current_inl, 0))
            #         tr_inl.translate((0, -idx*d_inl, 0))
            #         idx = (idx + playerconfiginl['Interval']) % inlnum
            #         slice_inl.set_data(seis3dmat[:, :, idx])
            #         tr_inl.translate((0, inlrange[idx], 0))
            #         tr_inl.translate((0, idx*d_inl, 0))
            #         current_slices.inl = inlrange[idx]
            #         canvas.app.sleep(0.2)
        if event.key == playerconfiginl['Pause'].lower():
            print(playerconfiginl['Pause'].lower() + ' not implemented yet !')
            # current_inl = current_slices.inl
            # if current_inl is not None and znum > 1 and xlnum > 1:
            #     canvas.freeze()
        # player - crossline
        if event.key == playerconfigxl['First'].lower():
            current_xl = current_slices.xl
            if current_xl is not None and znum > 1 and inlnum > 1:
                idx = ((current_xl - xlstart) / xlstep).astype(np.int32)
                tr_xl.translate((-current_xl, 0, 0))
                slice_xl.set_data(seis3dmat[:, 0, :])
                tr_xl.translate((xlstart, 0, 0))
                current_slices.xl = xlstart
        if event.key == playerconfigxl['Previous'].lower():
            current_xl = current_slices.xl
            if current_xl is not None and znum > 1 and inlnum > 1:
                idx = ((current_xl - xlstart) / xlstep).astype(np.int32)
                tr_xl.translate((-current_xl, 0, 0))
                idx = (idx - playerconfigxl['Interval']) % xlnum
                slice_xl.set_data(seis3dmat[:, idx, :])
                tr_xl.translate((xlrange[idx], 0, 0))
                current_slices.xl = xlrange[idx]
        if event.key == playerconfigxl['Next'].lower():
            current_xl = current_slices.xl
            if current_xl is not None and znum > 1 and inlnum > 1:
                idx = ((current_xl - xlstart) / xlstep).astype(np.int32)
                tr_xl.translate((-current_xl, 0, 0))
                idx = (idx + playerconfigxl['Interval']) % xlnum
                slice_xl.set_data(seis3dmat[:, idx, :])
                tr_xl.translate((xlrange[idx], 0, 0))
                current_slices.xl = xlrange[idx]
        if event.key == playerconfigxl['Last'].lower():
            current_xl = current_slices.xl
            if current_xl is not None and znum > 1 and inlnum > 1:
                idx = ((current_xl - xlstart) / xlstep).astype(np.int32)
                tr_xl.translate((-current_xl, 0, 0))
                slice_xl.set_data(seis3dmat[:, -1, :])
                tr_xl.translate((xlend, 0, 0))
                current_slices.xl = xlend
        if event.key == playerconfigxl['Backward'].lower():
            print(playerconfigxl['Backward'].lower() + ' not implemented yet !')
            # while True:
            #     current_xl = current_slices.xl
            #     if current_xl is not None and znum > 1 and inlnum > 1:
            #         idx = ((current_xl - xlstart) / xlstep).astype(np.int32)
            #         tr_xl.translate((-current_xl, 0, 0))
            #         tr_xl.translate((-idx * d_xl, 0, 0))
            #         idx = (idx - playerconfigxl['Interval']) % xlnum
            #         slice_xl.set_data(seis3dmat[:, idx, :])
            #         tr_xl.translate((xlrange[idx], 0, 0))
            #         tr_xl.translate((idx * d_xl, 0, 0))
            #         current_slices.xl = xlrange[idx]
            #         canvas.app.sleep(0.2)
        if event.key == playerconfigxl['Forward'].lower():
            print(playerconfigxl['Forward'].lower() + ' not implemented yet !')
            # while True:
            #     current_xl = current_slices.xl
            #     if current_xl is not None and znum > 1 and inlnum > 1:
            #         idx = ((current_xl - xlstart) / xlstep).astype(np.int32)
            #         tr_xl.translate((-current_xl, 0, 0))
            #         tr_xl.translate((-idx * d_xl, 0, 0))
            #         idx = (idx + playerconfigxl['Interval']) % xlnum
            #         slice_xl.set_data(seis3dmat[:, idx, :])
            #         tr_xl.translate((xlrange[idx], 0, 0))
            #         tr_xl.translate((idx * d_xl, 0, 0))
            #         current_slices.xl = xlrange[idx]
            #         canvas.app.sleep(0.2)
        if event.key == playerconfigxl['Pause'].lower():
            print(playerconfigxl['Pause'].lower() + ' not implemented yet !')
            # current_xl = current_slices.xl
            # if current_xl is not None and znum > 1 and inlnum > 1:
            #     canvas.freeze()
        # player - z
        if event.key == playerconfigz['First'].lower():
            current_z = current_slices.z
            if current_z is not None and inlnum > 1 and xlnum > 1:
                idx = ((current_z - zstart) / zstep).astype(np.int32)
                tr_z.translate((0, 0, -current_z))
                slice_z.set_data(seis3dmat[0, :, :])
                tr_z.translate((0, 0, zstart))
                current_slices.z = zstart
        if event.key == playerconfigz['Previous'].lower():
            current_z = current_slices.z
            if current_z is not None and inlnum > 1 and xlnum > 1:
                idx = ((current_z - zstart) / zstep).astype(np.int32)
                tr_z.translate((0, 0, -current_z))
                idx = (idx - playerconfigz['Interval']) % znum
                slice_z.set_data(seis3dmat[idx, :, :])
                tr_z.translate((0, 0, zrange[idx]))
                current_slices.z = zrange[idx]
        if event.key == playerconfigz['Next'].lower():
            current_z = current_slices.z
            if current_z is not None and inlnum > 1 and xlnum > 1:
                idx = ((current_z - zstart) / zstep).astype(np.int32)
                tr_z.translate((0, 0, -current_z))
                idx = (idx + playerconfigz['Interval']) % znum
                slice_z.set_data(seis3dmat[idx, :, :])
                tr_z.translate((0, 0, zrange[idx]))
                current_slices.z = zrange[idx]
        if event.key == playerconfigz['Last'].lower():
            current_z = current_slices.z
            if current_z is not None and inlnum > 1 and xlnum > 1:
                idx = ((current_z - zstart) / zstep).astype(np.int32)
                tr_z.translate((0, 0, -current_z))
                slice_z.set_data(seis3dmat[-1, :, :])
                tr_z.translate((0, 0, zend))
                current_slices.z = zend
        if event.key == playerconfigz['Backward'].lower():
            print(playerconfigz['Backward'].lower() + ' not implemented yet !')
            # while True:
            #     current_z = current_slices.z
            #     if current_z is not None and inlnum > 1 and xlnum > 1:
            #         idx = ((current_z - zstart) / zstep).astype(np.int32)
            #         tr_z.translate((0, 0, -current_z))
            #         tr_z.translate((0, 0, -idx * d_z))
            #         idx = (idx - playerconfigz['Interval']) % znum
            #         slice_z.set_data(seis3dmat[idx, :, :])
            #         tr_z.translate((0, 0, zrange[idx]))
            #         tr_z.translate((0, 0, idx * d_z))
            #         current_slices.z = zrange[idx]
            #         canvas.app.sleep(0.2)
        if event.key == playerconfigz['Forward'].lower():
            print(playerconfigz['Forward'].lower() + ' not implemented yet !')
            # while True:
            #     current_z = current_slices.z
            #     if current_z is not None and inlnum > 1 and xlnum > 1:
            #         idx = ((current_z - zstart) / zstep).astype(np.int32)
            #         tr_z.translate((0, 0, -current_z))
            #         tr_z.translate((0, 0, -idx * d_z))
            #         idx = (idx + playerconfigz['Interval']) % znum
            #         slice_z.set_data(seis3dmat[idx, :, :])
            #         tr_z.translate((0, 0, zrange[idx]))
            #         tr_z.translate((0, 0, idx * d_z))
            #         current_slices.z = zrange[idx]
            #         canvas.app.sleep(0.2)
        if event.key == playerconfigz['Pause'].lower():
            print(playerconfigz['Pause'].lower() + ' not implemented yet !')
            # current_z = current_slices.z
            # if current_z is not None and inlnum > 1 and xlnum > 1:
            #     canvas.freeze()
        #
        text_inlxlz.text = '( '
        if current_slices.inl is not None:
            text_inlxlz.text = text_inlxlz.text + str(current_slices.inl)
        text_inlxlz.text = text_inlxlz.text + ', '
        if current_slices.xl is not None:
            text_inlxlz.text = text_inlxlz.text + str(current_slices.xl)
        text_inlxlz.text = text_inlxlz.text + ', '
        if current_slices.z is not None:
            text_inlxlz.text = text_inlxlz.text + str(int(current_slices.z / zscale))
        text_inlxlz.text = text_inlxlz.text + ' )'

    def double_click_mouse(event):
        print('double click to be implemted')
        # p2 = event.pos
        # norm = np.mean(view.camera._viewbox.size)
        # if view.camera._event_value is None or len(view.camera._event_value) == 2:
        #     ev_val = view.camera.center
        # else:
        #     ev_val = view.camera._event_value
        # dist = p2 / norm * view.camera._scale_factor
        # print(view.camera._viewbox.size)
        # print(norm)
        # print(ev_val)
        # dist[1] *= -1
        # dx, dy, dz = view.camera._dist_to_trans(dist)
        # print([dx, dy, dz])
        # ff = view.camera._flip_factors
        # up, forward, right = view.camera._get_dim_vectors()
        # dx, dy, dz = right * dx + forward * dy + up * dz
        # dx, dy, dz = ff[0] * dx, ff[1] * dy, ff[2] * dz
        # print([dx, dy, dz])
        # c = ev_val
        # sc_half = view.camera._scale_factor / 2
        # point = c[0] + dx - sc_half, c[1] + dy - sc_half, c[2] + dz - sc_half
        # print(p2)
        # print(type(p2))
        # print(point)
        #
        # print(view.camera.center)
        # tr = view.camera.transforms()
        # print(tr.imap(view.camera.center))
        # print(event.pos)
        # vis = canvas.visual_at(event.pos)
        # tr = view.camera.node_transform(vis)
        # pos = tr.map(event.pos)
        # print(pos)
        # tr = canvas.scene.transform
        # pos = tr.imap(np.array([486, 112, 1, 1]))
        # print(pos)

    def resize_canvas(event):
        text_inlxlz.pos = (view.canvas.size[0] - 100, view.canvas.size[1] - 20)


    canvas.events.key_press.connect(press_key)
    canvas.events.mouse_double_click.connect(double_click_mouse)
    canvas.events.resize.connect(resize_canvas)


    canvas.show()

    if qicon is None and sys.flags.interactive == 0:
        app.run()


    return canvas


def saveSeisILSliceFrom2DMat(seis2dmat, imagename='',
                             inlsls=None, datacol=3,
                             inlcol=0, xlcol=1, zcol=2,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             verbose=True, qpgsdlg=None):
    """
    Save seismic inline slices as image files (by matplotlib.pcolormesh)

    Args:
        seis2dmat:  seismic data in 2D matrix of at least four columns [IL, XL, Z, Value]
        imagename:  prefix of image name. Default is ''
                    'IL_XXX.jpg' is added with XXX representing inline slice No.
        inlsls:     list of inline slices in array [xl1, xl2, ...]
                    Save all inline slices if not specified
        datacol:    index of data column (indexing from from 0)
                    Default is the fourth column (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        verbose:    flag for message display. Default is True
        qpgsdlg:    QProgressDialog for displaying progress. Default is None

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in saveSeisILSliceFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in saveSeisILSliceFrom2DMat: Not data column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in saveSeisILSliceFrom2DMat: Not inline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in saveSeisILSliceFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in saveSeisILSliceFrom2DMat: Not z column found in 2D seismic matrix',
                      type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if inlsls is None:
        vis_msg.print('WARNING in saveSeisILSliceFrom2DMat: to save all inline slices in 2D seismic matrix',
                      type='warning')
        inlsls = inlrange

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in saveSeisILSliceFrom2DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, zrange)

    ninlsls = len(inlsls)
    if verbose:
        print('Save ' + str(ninlsls) + ' inline slices')

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(ninlsls)

    for i in range(ninlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        inl = inlsls[i]
        idx = np.round((inl - inlstart) / inlstep).astype(np.int32)
        if idx >= 0 and idx < inlnum:
            seisdata = seis3dmat[:, :, idx]
            plt.figure(i + 1, facecolor='white', frameon=False)
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([zend, zstart])
            plt.xticks([])
            plt.yticks([])

            plt.Axes(plt.gcf(), [0.0, 0.0, 1.0, 1.0])
            imagepath = imagename + "IL_" + str(inlrange[idx]) + ".png"
            plt.savefig(imagepath, dpi=300, bbox_inches='tight', pad_inches=0)

    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(ninlsls)

    return


def saveSeisILSliceFrom3DMat(seis3dmat, imagename='',
                             inlsls=None, seisinfo=None,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             verbose=True, qpgsdlg=None):
    """
    Save seismic inline slices as image files (by matplotlib.pcolormesh)

    Args:
        seis3dmat:  3D matrix representing seismic data [Z/XL/IL]
        imagename:  prefix of image name. Default is ''
                    'IL_XXX.jpg' is added with XXX representing inline slice No.
        inlsls:     list of inline slices in array [inl1, inl2, ...]
                    Save all inline slices if not specified
        seisinfo:   basic information of 3D seismic survey
                    Auto-generated from 3D matrix if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        verbose:    flag for message display. Default is True

    Return:
        N/A
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in saveSeisILSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in saveSeisILSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    inlstart = seisinfo['ILStart']
    inlstep = seisinfo['ILStep']
    inlnum = seisinfo['ILNum']
    if inlnum == 1:
        inlstep = 1

    if inlsls is None:
        vis_msg.print('WARNING in saveSeisILSliceFrom3DMat: to save all inline slices in 3D seismic matrix',
                      type='warning')
        inlsls = inlrange

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in saveSeisILSliceFrom3DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, zrange)

    ninlsls = len(inlsls)
    if verbose:
        print('Save ' + str(ninlsls) + ' inline slices')

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(ninlsls)

    for i in range(ninlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        inl = inlsls[i]
        idx = np.round((inl - inlstart) / inlstep).astype(np.int32)
        if idx >= 0 and idx < inlnum:
            seisdata = seis3dmat[:, :, idx]
            plt.figure(i + 1, facecolor='white', frameon=False)
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([zend, zstart])
            plt.xticks([])
            plt.yticks([])
            plt.Axes(plt.gcf(), [0.0, 0.0, 1.0, 1.0])
            imagepath = imagename + 'IL_' + str(inlrange[idx]) + '.png'
            plt.savefig(imagepath, dpi=300, bbox_inches='tight', pad_inches=0)

    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(ninlsls)

    return


def saveSeisXLSliceFrom2DMat(seis2dmat, imagename='',
                             xlsls=None, datacol=3,
                             inlcol=0, xlcol=1, zcol=2,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             verbose=True, qpgsdlg=None):
    """
    Save seismic crossine slices as image files (by matplotlib.pcolormesh)

    Args:
        seis2dmat:  seismic data in 2D matrix of at least four columns [IL, XL, Z, Value]
        imagename:  prefix of image name. Default is ''
                    'XL_XXX.jpg' is added with XXX representing crossline slice No.
        xlsls:      list of crossline slices in array [xl1, xl2, ...]
                    Save all crossline slices if not specified
        datacol:    index of data column (indexing from 0)
                    Default is the fourth column (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        verbose:    flag for message display. Default is True
        qpgsdlg:    QProgressDialog for displaying progress. Default is None

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in saveSeisXLSliceFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in saveSeisXLSliceFrom2DMat: Not data column found in 2D seismic matrix', type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in saveSeisXLSliceFrom2DMat: Not inline column found in 2D seismic matrix', type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in saveSeisXLSliceFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in saveSeisXLSliceFrom2DMat: Not z column found in 2D seismic matrix', type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1

    if xlsls is None:
        vis_msg.print('WARNING in saveSeisXLSliceFrom2DMat: to save all crossline slices in 2D seismic matrix',
                      type='warning')
        xlsls = xlrange

    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in saveSeisXLSliceFrom2DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(inlrange, zrange)

    nxlsls = len(xlsls)

    if verbose:
        print('Save ' + str(nxlsls) + ' crossline slices')

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nxlsls)

    for i in range(nxlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        xl = xlsls[i]
        idx = np.round((xl - xlstart) / xlstep).astype(np.int32)
        if idx >= 0 and idx < xlnum:
            seisdata = seis3dmat[:, idx, :]
            plt.figure(facecolor='white', frameon=False)
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([inlstart, inlend])
            plt.ylim([zend, zstart])
            plt.xticks([])
            plt.yticks([])
            plt.Axes(plt.gcf(), [0.0, 0.0, 1.0, 1.0])
            imagepath = imagename + 'XL_' + str(xlrange[idx]) + '.png'
            plt.savefig(imagepath, dpi=300, bbox_inches='tight', pad_inches=0)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nxlsls)

    return


def saveSeisXLSliceFrom3DMat(seis3dmat, imagename='',
                             xlsls=None, seisinfo=None,
                             colormap=None, flipcmap=False,
                             valuemin=-1.0, valuemax=1.0,
                             verbose=True, qpgsdlg=None):
    """
    Save seismic crossline slices as image files (by matplotlib.pcolormesh)

    Args:
        seis3dmat:  3D matrix representing seismic data [Z/XL/IL]
        imagename:  prefix of image name. Default is ''
                    'XL_XXX.jpg' is added with XXX representing crossline slice No.
        xlsls:      list of crossline slices in array [xl1, xl2, ...]
                    Save all crossline slices if not specified
        seisinfo:   basic information of 3D seismic survey
                    Auto-generated from 3D matrix if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        verbose:    flag for message display. Default is True

    Return:
        N/A
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in saveSeisXLSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in saveSeisXLSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    zstart = seisinfo['ZStart']
    zend = seisinfo['ZEnd']
    xlstart = seisinfo['XLStart']
    xlstep = seisinfo['XLStep']
    xlnum = seisinfo['XLNum']
    if xlnum == 1:
        xlstep = 1

    if xlsls is None:
        vis_msg.print('WARNING in saveSeisXLSliceFrom3DMat: to save all crossline slices in 3D seismic matrix',
                      type='warning')
        xlsls = xlrange

    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in saveSeisXLSliceFrom3DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(inlrange, zrange)

    nxlsls = len(xlsls)
    if verbose:
        print('Save ' + str(nxlsls) + ' crossline slices')

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nxlsls)

    for i in range(nxlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        xl = xlsls[i]
        idx = np.round((xl - xlstart) / xlstep).astype(np.int32)
        if idx >= 0 and idx < xlnum:
            seisdata = seis3dmat[:, idx, :]
            plt.figure(i + 1, facecolor='white', frameon=False)
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([inlstart, inlend])
            plt.ylim([zend, zstart])
            plt.xticks([])
            plt.yticks([])
            plt.Axes(plt.gcf(), [0.0, 0.0, 1.0, 1.0])
            imagepath = imagename + 'XL_' + str(xlrange[idx]) + '.png'
            plt.savefig(imagepath, dpi=300, bbox_inches='tight', pad_inches=0)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nxlsls)

    return


def saveSeisZSliceFrom2DMat(seis2dmat, imagename='',
                            zsls=None, datacol=3,
                            inlcol=0, xlcol=1, zcol=2,
                            colormap=None, flipcmap=False,
                            valuemin=-1.0, valuemax=1.0,
                            verbose=True, qpgsdlg=None):
    """
    Save seismic z slices as image files (by matplotlib.pcolormesh)

    Args:
        seis2dmat:  2D matrix representing seismic data
                    It contains at least four columns, [IL, XL, Z, Value, ...]
        imagename:  prefix of image name. Default is ''
                    'Z_XXX.jpg' is added with XXX representing z slice No.
        zsls:       list of z slices in array [xl1, xl2, ...]
                    Save all z slices if not specified
        datacol:    index of data column (indexing from 0)
                    Default the fourth column (3)
        inlcol:     index of inline column. Default is the first column (0)
        xlcol:      index of crossline column. Default is the second column (1)
        zcol:       index of z column. Default is the third column (2)
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for seismic data visualization. Default is -1.0
        valuemax:   upper limit for seismic data visualization. Default is 1.0
        verbose:    flag for message display. Default is True
        qpgsdlg:    QProgressDialog for displaying progress. Default is None

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input matrix
    if np.ndim(seis2dmat) != 2:
        vis_msg.print('ERROR in saveSeisZSliceFrom2DMat: 2D seismic matrix expected', type='error')
        sys.exit()
    if datacol < 0 or len(seis2dmat[0, :]) <= datacol:
        vis_msg.print('ERROR in saveSeisZSliceFrom2DMat: Not data column found in 2D seismic matrix', type='error')
        sys.exit()
    if inlcol < 0 or len(seis2dmat[0, :]) <= inlcol:
        vis_msg.print('ERROR in saveSeisZSliceFrom2DMat: Not inline column found in 2D seismic matrix', type='error')
        sys.exit()
    if xlcol < 0 or len(seis2dmat[0, :]) <= xlcol:
        vis_msg.print('ERROR in saveSeisZSliceFrom2DMat: Not crossline column found in 2D seismic matrix',
                      type='error')
        sys.exit()
    if zcol < 0 or len(seis2dmat[0, :]) <= zcol:
        vis_msg.print('ERROR in saveSeisZSliceFrom2DMat: Not z column found in 2D seismic matrix', type='error')
        sys.exit()

    seisinfo = seis_ays.getSeisInfoFrom2DMat(seis2dmat,
                                            inlcol=inlcol, xlcol=xlcol, zcol=zcol)
    seis3dmat = seis_ays.convertSeis2DMatTo3DMat(seis2dmat,
                                                datacol=datacol,
                                                inlcol=inlcol, xlcol=xlcol, zcol=zcol)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zstep = seisinfo['ZStep']
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = -1

    if zsls is None:
        vis_msg.print('WARNING in saveSeisZSliceFrom2DMat: to save all a slices in 2D seismic matrix', type='warning')
        zsls = zrange

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in saveSeisZSliceFrom2DMat: 1D array of z slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, inlrange)

    nzsls = len(zsls)
    if verbose:
        print('Save ' + str(nzsls) + ' z slices')

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nzsls)

    for i in range(nzsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        z = zsls[i]
        idx = np.round((z - zstart) / zstep).astype(np.int32)
        if idx >= 0 and idx < znum:
            seisdata = seis3dmat[idx, :, :]
            seisdata = seisdata.transpose()
            plt.figure(i + 1, facecolor='white', frameon=False)
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([inlstart, inlend])
            plt.xticks([])
            plt.yticks([])
            plt.Axes(plt.gcf(), [0.0, 0.0, 1.0, 1.0])
            imagepath = imagename + 'Z_' + str(zrange[idx]) + '.png'
            plt.savefig(imagepath, dpi=300, bbox_inches='tight', pad_inches=0)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nzsls)

    return


def saveSeisZSliceFrom3DMat(seis3dmat, imagename='',
                            zsls=None, seisinfo=None,
                            colormap=None, flipcmap=False,
                            valuemin=-1.0, valuemax=1.0,
                            verbose=True, qpgsdlg=None):
    """
    Save seismic z slices as image files (by matplotlib.pcolormesh)

    Args:
        seis3dmat:  3D matrix representing seismic data [Z/XL/IL]
        imagename:  prefix of image name. Default is ''
                    'XL_XXX.jpg' is added with XXX representing z slice No.
        zsls:       list of z slices in array [xl1, xl2, ...]
                    Save all z slices if not specified
        seisinfo:   basic information of 3D seismic survey
                    Auto-generated from 3D matrix if not specified
        colormap:   colormap name for seismic data visualization, such as 'seismic'
                    Use the default colormap by vis_cmap.makeColorMap if not specified
        flipcmap:   Flip colormap. Default is False
        valuemin:   lower limit for data visualization. Default is -1.0
        valuemax:   upper limit for data visualization. Default is 1.0
        verbose:    flag for message display. Default is True

    Return:
        N/A

    Note:
        Negative z is used in the vertical direction
    """

    # Check input 3D seismic matrix
    if np.ndim(seis3dmat) != 3:
        vis_msg.print('ERROR in saveSeisZSliceFrom3DMat: 3D seismic matrix expected', type='error')
        sys.exit()

    if seisinfo is None:
        vis_msg.print('WARNING in saveSeisZSliceFrom3DMat: Survey info auto-generated from 3D seismic matrix',
                      type='warning')
        seisinfo = seis_ays.createSeisInfoFrom3DMat(seis3dmat)

    inlrange = seisinfo['ILRange']
    xlrange = seisinfo['XLRange']
    zrange = seisinfo['ZRange']
    inlstart = seisinfo['ILStart']
    inlend = seisinfo['ILEnd']
    xlstart = seisinfo['XLStart']
    xlend = seisinfo['XLEnd']
    zstart = seisinfo['ZStart']
    zstep = seisinfo['ZStep']
    znum = seisinfo['ZNum']
    if znum == 1:
        zstep = -1

    if zsls is None:
        vis_msg.print('WARNING in saveSeisZSliceFrom3DMat: to save all z slices in 3D seismic matrix',
                      type='warning')
        zsls = zrange

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in saveSeisZSliceFrom3DMat: 1D array of z slices expected', type='error')
        sys.exit()

    x, y = np.meshgrid(xlrange, inlrange)

    nzsls = len(zsls)
    if verbose:
        print('Save ' + str(nzsls) + ' z slices')

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nzsls)

    for i in range(nzsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        z = zsls[i]
        idx = np.round((z - zstart) / zstep).astype(np.int32)
        if idx >= 0 and idx < znum:
            seisdata = seis3dmat[idx, :, :]
            seisdata = seisdata.transpose()
            plt.figure(i + 1, facecolor='white', frameon=False)
            plt.pcolormesh(x, y, seisdata,
                           cmap=vis_cmap.makeColorMap(colormap, flipcmap),
                           shading='gouraud',
                           vmin=valuemin, vmax=valuemax)
            plt.xlim([xlstart, xlend])
            plt.ylim([inlstart, inlend])
            plt.xticks([])
            plt.yticks([])
            plt.Axes(plt.gcf(), [0.0, 0.0, 1.0, 1.0])
            imagepath = imagename + 'Z_' + str(zrange[idx]) + '.png'
            plt.savefig(imagepath, dpi=300, bbox_inches='tight', pad_inches=0)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nzsls)

    return


def loadSeisILSliceTo2DMat(imagename, inlsls, ispref=True,
                           xlstart=0, xlend=99, xlnum=100,
                           zstart=0, zend=-99, znum=100,
                           verbose=True, qpgsdlg=None):
    """
    Load seismic inline slices from image files to 2D seismic matrix (by matplotlib.imread)

    Args:
        imagename:  name of image files.
        ispref:     image name is given as pref
                    'IL_XXX.jpg' is added with XXX representing inline slice No.
        inlsls:     list of inline slices in array [inl1, inl2, ...]
        xlstart:    first crossline No. for creating 2D seismic matrix. Default is 0
        xlend:      last crossline No. for creating 2D seismic matrix. Default is 99
        xlnum:      number of crossline slices for creating 2D seismic matrix. Default is 100
        zstart:     top z slice for creating 2D seismic matrix. Default is 0
        zend:       bottom z slice for creating 2D seismic matrix. Default is -99
        znum:       number of z slices for creating 3D seismic matrix. Default is 100
        verbose:    flag for message display. Default is True
        qpgsdlg:    QProgressDialog for displaying progress. Default is None

    Return:
        seis2dmat: 2D seismic matrix of four columns [IL, XL, Z, Value]

    Note:
        Negative z is used in the vertical direction
    """

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in loadSeisILSliceTo2DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    # crossline
    xlstart = np.round(xlstart).astype(np.int32)
    xlnum = np.round(xlnum).astype(np.int32)
    if xlnum > 1:
        xlstep = np.round((xlend-xlstart)/(xlnum-1)).astype(np.int32)
        if xlstep == 0:
            xlstep = 1
        xlend = xlstart + (xlnum-1) * xlstep
    else:
        xlnum = 1
        xlend = xlstart
    xlrange = np.linspace(xlstart, xlend, xlnum).astype(np.int32)
    # z
    zstart = np.round(zstart).astype(np.int32)
    znum = np.round(znum).astype(np.int32)
    if znum > 1:
        zstep = np.round((zend - zstart) / (znum - 1)).astype(np.int32)
        if zstep == 0:
            zstep = -1
        zend = zstart + (znum - 1) * zstep
    else:
        znum = 1
        zend = zstart
    zrange = np.linspace(zstart, zend, znum).astype(np.int32)

    ninlsls = len(inlsls)
    if verbose:
        print('Load ' + str(ninlsls) + ' inline images to 2D seismic matrix')

    inl3dmat = np.zeros([znum, xlnum, ninlsls], np.int32)
    xl3dmat = np.zeros([znum, xlnum, ninlsls], np.int32)
    z3dmat = np.zeros([znum, xlnum, ninlsls], np.int32)
    seis3dmat = np.zeros([znum, xlnum, ninlsls], np.float32)

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(ninlsls)

    for i in range(ninlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        inl = inlsls[i]
        if ispref:
            imagepath = imagename + 'IL_' + str(inl) + '.jpg'
        else:
            imagepath = imagename[i]
        #
        data = plt.imread(imagepath).astype(float)
        #
        image_data = 0.2989 * data[:, :, 0] + 0.5870 * data[:, :, 1] + 0.1140 * data[:, :, 2]
        if np.max(data[:, :, 0]) * np.max(data[:, :, 1]) * np.max(data[:, :, 2]) != 0:
            image_data = image_data * 3.0 / (np.max(data[:, :, 0]) + np.max(data[:, :, 1]) + np.max(data[:, :, 2]))
        if np.shape(data)[2] > 3:
            image_data = image_data + 1.0 - data[:, :, 3]
        #
        image_x = np.linspace(xlstart, xlend, np.shape(image_data)[1])
        image_y = np.linspace(zend, zstart, np.shape(image_data)[0])
        f_interp = interpolate.interp2d(image_x, image_y, image_data)

        inl3dmat[:, :, i] = inl
        xl3dmat[:, :, i], z3dmat[:, :, i] = np.meshgrid(xlrange, zrange)
        seis3dmat[:, :, i] = f_interp(xlrange, zrange)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(ninlsls)

    inl3dmat = inl3dmat.transpose()
    inl3dmat = np.reshape(inl3dmat, [1, znum * xlnum * ninlsls])
    inl3dmat = inl3dmat.transpose()
    xl3dmat = xl3dmat.transpose()
    xl3dmat = np.reshape(xl3dmat, [1, znum * xlnum * ninlsls])
    xl3dmat = xl3dmat.transpose()
    z3dmat = z3dmat.transpose()
    z3dmat = np.reshape(z3dmat, [1, znum * xlnum * ninlsls])
    z3dmat = z3dmat.transpose()
    seis3dmat = seis3dmat.transpose()
    seis3dmat = np.reshape(seis3dmat, [1, znum * xlnum * ninlsls])
    seis3dmat = seis3dmat.transpose()

    seis2dmat = np.concatenate((inl3dmat, xl3dmat, z3dmat, seis3dmat), axis=1)

    return seis2dmat


def loadSeisILSliceTo3DMat(imagename, inlsls, ispref=True, xlnum=100, znum=100,
                           verbose=True, qpgsdlg=None):
    """
    Load seismic inline slices from image files to 3D seismic matrix (by matplotlib.imread)

    Args:
        imagename:  name of image files.
        ispref:     image name is given as pref
                    'IL_XXX.jpg' is added with XXX representing inline slice No.
        inlsls:     list of inline slices in array [inl1, inl2, ...]
        xlnum:      number of crossline slices for creating 3D seismic matrix. Default is 100
        znum:       number of z slices for creating 3D seismic matrix. Default is 100
        verbose:    flag for message display. Default is True

    Return:
        seis3dmat: 3D seismic matrix [Z/XL/IL]

    Note:
        Negative z is used in the vertical direction
    """

    if np.ndim(inlsls) != 1:
        vis_msg.print('ERROR in loadSeisILSliceTo3DMat: 1D array of inline slices expected', type='error')
        sys.exit()

    xlrange = np.linspace(0.0, 1.0, xlnum)
    zrange = np.linspace(0.0, -1.0, znum)

    ninlsls = len(inlsls)
    if verbose:
        print('Load ' + str(ninlsls) + ' inline images to 3D seismic matrix')

    seis3dmat = np.zeros([znum, xlnum, ninlsls], np.float32)

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(ninlsls)

    for i in range(ninlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        inl = inlsls[i]
        if ispref:
            imagepath = imagename + 'IL_' + str(inl) + '.jpg'
        else:
            imagepath = imagename[i]
        #
        data = plt.imread(imagepath).astype(float)
        #
        image_data = 0.2989 * data[:, :, 0] + 0.5870 * data[:, :, 1] + 0.1140 * data[:, :, 2]
        if np.max(data[:, :, 0]) * np.max(data[:, :, 1]) * np.max(data[:, :, 2]) != 0:
            image_data = image_data * 3.0 / (np.max(data[:, :, 0]) + np.max(data[:, :, 1]) + np.max(data[:, :, 2]))
        if np.shape(data)[2] > 3:
            image_data = image_data + 1.0 - data[:, :, 3]
        #
        image_x = np.linspace(0.0, 1.0, np.shape(image_data)[1])
        image_y = np.linspace(-1.0, 0.0, np.shape(image_data)[0])
        f_interp = interpolate.interp2d(image_x, image_y, image_data)

        seis3dmat[:, :, i] = f_interp(xlrange, zrange)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(ninlsls)

    return seis3dmat


def loadSeisXLSliceTo2DMat(imagename, xlsls, ispref=True,
                           inlstart=0, inlend=99, inlnum=100,
                           zstart=0, zend=-99, znum=100,
                           verbose=True, qpgsdlg=None):
    """
    Load seismic crossline slices from image files to 2D seismic matrix (by matplotlib.imread)

    Args:
        imagename:  name of image files.
        ispref:     image name is given as pref
                    'XL_XXX.jpg' is added with XXX representing crossline slice No.
        xlsls:      list of crossline slices in array [xl1, xl2, ...]
        inlstart:   first inline No. for creating 2D seismic matrix. Default is 0
        inlend:     end inline No. for creating 2D seismic matrix. Default is 99
        inlnum:     number of inline slices for creating 2D seismic matrix. Default is 100
        zstart:     top z slice No. for creating 2D seismic matrix. Default is 0
        zend:       bottom z slice No. for creating 2D seismic matrix. Default is -99
        znum:       number of z slices for creating 2D seismic matrix. Default is 100
        verbose:    flag for message display. Default is True
        qpgsdlg:    QProgressDialog for displaying progress. Default is None

    Return:
         seis2dmat: 2D seismic matrix of four columns [IL, XL, Z, Value]

    Note:
        Negative z is used in the vertical direction
    """
    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in loadSeisXLSliceTo2DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    # inline
    inlstart = np.round(inlstart).astype(np.int32)
    inlnum = np.round(inlnum).astype(np.int32)
    if inlnum > 1:
        inlstep = np.round((inlend-inlstart)/(inlnum-1)).astype(np.int32)
        if inlstep == 0:
            inlstep = 1
        inlend = inlstart + (inlnum-1) * inlstep
    else:
        inlnum = 1
        inlend = inlstart
    inlrange = np.linspace(inlstart, inlend, inlnum).astype(np.int32)
    # z
    zstart = np.round(zstart).astype(np.int32)
    znum = np.round(znum).astype(np.int32)
    if znum > 1:
        zstep = np.round((zend - zstart) / (znum - 1)).astype(np.int32)
        if zstep == 0:
            zstep = -1
        zend = zstart + (znum - 1) * zstep
    else:
        znum = 1
        zend = zstart
    zrange = np.linspace(zstart, zend, znum).astype(np.int32)

    nxlsls = len(xlsls)
    if verbose:
        print('Load ' + str(nxlsls) + ' crossline images to 2D seismic matrix')

    inl3dmat = np.zeros([znum, nxlsls, inlnum], np.int32)
    xl3dmat = np.zeros([znum, nxlsls, inlnum], np.int32)
    z3dmat = np.zeros([znum, nxlsls, inlnum], np.int32)
    seis3dmat = np.zeros([znum, nxlsls, inlnum], np.float32)

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nxlsls)

    for i in range(nxlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        xl = xlsls[i]
        if ispref:
            imagepath = imagename + 'XL_' + str(xl) + '.jpg'
        else:
            imagepath = imagename[i]
        #
        data = plt.imread(imagepath).astype(float)
        #
        image_data = 0.2989 * data[:, :, 0] + 0.5870 * data[:, :, 1] + 0.1140 * data[:, :, 2]
        if np.max(data[:, :, 0]) * np.max(data[:, :, 1]) * np.max(data[:, :, 2]) != 0:
            image_data = image_data * 3.0 / (np.max(data[:, :, 0]) + np.max(data[:, :, 1]) + np.max(data[:, :, 2]))
        if np.shape(data)[2] > 3:
            image_data = image_data + 1.0 - data[:, :, 3]
        #
        image_x = np.linspace(inlstart, inlend, np.shape(image_data)[1])
        image_y = np.linspace(zend, zstart, np.shape(image_data)[0])
        f_interp = interpolate.interp2d(image_x, image_y, image_data)

        inl3dmat[:, i, :], z3dmat[:, i, :] = np.meshgrid(inlrange, zrange)
        xl3dmat[:, i, :] = xl
        seis3dmat[:, i, :] = f_interp(inlrange, zrange)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nxlsls)

    inl3dmat = inl3dmat.transpose()
    inl3dmat = np.reshape(inl3dmat, [1, znum * nxlsls * inlnum])
    inl3dmat = inl3dmat.transpose()
    xl3dmat = xl3dmat.transpose()
    xl3dmat = np.reshape(xl3dmat, [1, znum * nxlsls * inlnum])
    xl3dmat = xl3dmat.transpose()
    z3dmat = z3dmat.transpose()
    z3dmat = np.reshape(z3dmat, [1, znum * nxlsls * inlnum])
    z3dmat = z3dmat.transpose()
    seis3dmat = seis3dmat.transpose()
    seis3dmat = np.reshape(seis3dmat, [1, znum * nxlsls * inlnum])
    seis3dmat = seis3dmat.transpose()

    seis2dmat = np.concatenate((inl3dmat, xl3dmat, z3dmat, seis3dmat), axis=1)

    return seis2dmat


def loadSeisXLSliceTo3DMat(imagename, xlsls, ispref=True, inlnum=100, znum=100,
                           verbose=True, qpgsdlg=None):
    """
    Load seismic crossline slices from image files to 3D seismic matrix (by matplotlib.imread)

    Args:
        imagename:  name of image files.
        ispref:     image name is given as pref
                    'XL_XXX.jpg' is added with XXX representing crossline slice No.
        xlsls:      list of crossline slices in array [xl1, xl2, ...]
        inlnum:     number of inline slices for creating 3D seismic matrix. Default is 100
        znum:       number of z slices for creating 3D seismic matrix. Default is 100
        verbose:    flag for message display. Default is True

    Return:
        seis3dmat: 3D seismic matrix [Z/XL/IL]

    Note:
        Negative z is used in the vertical direction
    """

    if np.ndim(xlsls) != 1:
        vis_msg.print('ERROR in loadSeisXLSliceTo3DMat: 1D array of crossline slices expected', type='error')
        sys.exit()

    inlrange = np.linspace(0.0, 1.0, inlnum)
    zrange = np.linspace(0.0, -1.0, znum)

    nxlsls = len(xlsls)
    if verbose:
        print('Load ' + str(nxlsls) + ' crossline images to 3D seismic matrix')

    seis3dmat = np.zeros([znum, nxlsls, inlnum], np.float32)

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nxlsls)

    for i in range(nxlsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        xl = xlsls[i]
        if ispref:
            imagepath = imagename + 'XL_' + str(xl) + '.jpg'
        else:
            imagepath = imagename[i]
        #
        data = plt.imread(imagepath).astype(float)
        #
        image_data = 0.2989 * data[:, :, 0] + 0.5870 * data[:, :, 1] + 0.1140 * data[:, :, 2]
        if np.max(data[:, :, 0]) * np.max(data[:, :, 1]) * np.max(data[:, :, 2]) != 0:
            image_data = image_data * 3.0 / (np.max(data[:, :, 0]) + np.max(data[:, :, 1]) + np.max(data[:, :, 2]))
        if np.shape(data)[2] > 3:
            image_data = image_data + 1.0 - data[:, :, 3]
        #
        image_x = np.linspace(0.0, 1.0, np.shape(image_data)[1])
        image_y = np.linspace(-1.0, 0.0, np.shape(image_data)[0])
        f_interp = interpolate.interp2d(image_x, image_y, image_data)

        seis3dmat[:, i, :] = f_interp(inlrange, zrange)
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nxlsls)

    return seis3dmat


def loadSeisZSliceTo2DMat(imagename, zsls, ispref=True,
                          inlstart=0, inlend=99, inlnum=100,
                          xlstart=0, xlend=99, xlnum=100,
                          verbose=True, qpgsdlg=None):
    """
    Load seismic z slices from image files to 2D seismic matrix (by matplotlib.imread)

    Args:
        imagename:  name of image files.
        ispref:     image name is given as pref
                        'Z_XXX.jpg' is added with XXX representing z slice No.
        zsls:       list of z slices in array [xl1, xl2, ...]
        inlstart:   first inline No. for creating 2D seismic matrix. Default is 0
        inlend:     end inline No. for creating 2D seismic matrix. Default is 99
        inlnum:     number of inline slices for creating 2D seismic matrix. Default is 100
        xlstart:    first crossline slice No. for creating 2D seismic matrix. Default is 0
        xlend:      end crossline slice No. for creating 2D seismic matrix. Default is -99
        xlnum:      number of crossline slices for creating 2D seismic matrix. Default is 100
        verbose:    flag for message display. Default is True
        qpgsdlg:    QProgressDialog for displaying progress. Default is None

    Return:
        seis2dmat: 2D seismic matrix of four columns [IL, XL, Z, Value]

    Note:
        Negative z is used in the vertical direction
    """

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in loadSeisZSliceTo2DMat: 1D array of z slices expected', type='error')
        sys.exit()

    # inline
    inlstart = np.round(inlstart).astype(np.int32)
    inlnum = np.round(inlnum).astype(np.int32)
    if inlnum > 1:
        inlstep = np.round((inlend-inlstart)/(inlnum-1)).astype(np.int32)
        if inlstep == 0:
            inlstep = 1
        inlend = inlstart + (inlnum-1) * inlstep
    else:
        inlnum = 1
        inlend = inlstart
    inlrange = np.linspace(inlstart, inlend, inlnum).astype(np.int32)
    # crossline
    xlstart = np.round(xlstart).astype(np.int32)
    xlnum = np.round(xlnum).astype(np.int32)
    if xlnum > 1:
        xlstep = np.round((xlend - xlstart) / (xlnum - 1)).astype(np.int32)
        if xlstep == 0:
            xlstep = 1
        xlend = xlstart + (xlnum - 1) * xlstep
    else:
        xlnum = 1
        xlend = xlstart
    xlrange = np.linspace(xlstart, xlend, xlnum).astype(np.int32)

    nzsls = len(zsls)
    if verbose:
        print('Load ' + str(nzsls) + ' z images to 2D seismic matrix')

    inl3dmat = np.zeros([nzsls, xlnum, inlnum], np.int32)
    xl3dmat = np.zeros([nzsls, xlnum, inlnum], np.int32)
    z3dmat = np.zeros([nzsls, xlnum, inlnum], np.int32)
    seis3dmat = np.zeros([nzsls, xlnum, inlnum], np.float32)

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nzsls)

    for i in range(nzsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        z = zsls[i]
        if ispref:
            imagepath = imagename + 'Z_' + str(z) + '.jpg'
        else:
            imagepath = imagename[i]
        #
        data = plt.imread(imagepath).astype(float)
        #
        image_data = 0.2989 * data[:, :, 0] + 0.5870 * data[:, :, 1] + 0.1140 * data[:, :, 2]
        if np.max(data[:, :, 0]) * np.max(data[:, :, 1]) * np.max(data[:, :, 2]) != 0:
            image_data = image_data * 3.0 / (np.max(data[:, :, 0]) + np.max(data[:, :, 1]) + np.max(data[:, :, 2]))
        if np.shape(data)[2] > 3:
            image_data = image_data + 1.0 - data[:, :, 3]
        #
        image_x = np.linspace(xlend, xlstart, np.shape(image_data)[1])
        image_y = np.linspace(inlstart, inlend, np.shape(image_data)[0])
        f_interp = interpolate.interp2d(image_x, image_y, image_data)

        temp1, temp2 = np.meshgrid(xlrange, inlrange)
        xl3dmat[i, :, :] = temp1.transpose()
        inl3dmat[i, :, :] = temp2.transpose()
        z3dmat[i, :, :] = z
        temp1 = np.fliplr(np.flipud(f_interp(xlrange, inlrange)))
        seis3dmat[i, :, :] = temp1.transpose()
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nzsls)

    inl3dmat = inl3dmat.transpose()
    inl3dmat = np.reshape(inl3dmat, [1, nzsls * xlnum * inlnum])
    inl3dmat = inl3dmat.transpose()
    xl3dmat = xl3dmat.transpose()
    xl3dmat = np.reshape(xl3dmat, [1, nzsls * xlnum * inlnum])
    xl3dmat = xl3dmat.transpose()
    z3dmat = z3dmat.transpose()
    z3dmat = np.reshape(z3dmat, [1, nzsls * xlnum * inlnum])
    z3dmat = z3dmat.transpose()
    seis3dmat = seis3dmat.transpose()
    seis3dmat = np.reshape(seis3dmat, [1, nzsls * xlnum * inlnum])
    seis3dmat = seis3dmat.transpose()

    seis2dmat = np.concatenate((inl3dmat, xl3dmat, z3dmat, seis3dmat), axis=1)

    return seis2dmat


def loadSeisZSliceTo3DMat(imagename, zsls, ispref=True, inlnum=100, xlnum=100,
                          verbose=True, qpgsdlg=None):
    """
    Load seismic z slices from image files to 3D seismic matrix (by matplotlib.imread)

    Args:
        imagename:  name of image files.
        ispref:     image name is given as pref
                    'Z_XXX.jpg' is added with XXX representing z slice No.
        zlsls:      list of inline slices in array [inl1, inl2, ...]
        inllnum:    number of inline slices for creating 3D seismic matrix. Default is 100
        xlnum:      number of crossline slices for creating 3D seismic matrix. Default is 100
        verbose:    flag for message display. Default is True

    Return:
        seis3dmat: 3D seismic matrix [Z/XL/IL]

    Note:
        Negative z is used in the vertical direction
    """

    if np.ndim(zsls) != 1:
        vis_msg.print('ERROR in loadSeisZSliceTo3DMat: 1D array of z slices expected', type='error')
        sys.exit()

    xlrange = np.linspace(0.0, 1.0, xlnum)
    inlrange = np.linspace(0.0, 1.0, inlnum)

    nzsls = len(zsls)
    if verbose:
        print('Load ' + str(nzsls) + ' z images to 3D seismic matrix')

    seis3dmat = np.zeros([nzsls, xlnum, inlnum], np.float32)

    if qpgsdlg is not None:
        qpgsdlg.setMaximum(nzsls)

    for i in range(nzsls):
        #
        if qpgsdlg is not None:
            QtCore.QCoreApplication.instance().processEvents()
            qpgsdlg.setValue(i)
        #
        z = zsls[i]
        if ispref:
            imagepath = imagename + 'Z_' + str(z) + '.jpg'
        else:
            imagepath = imagename[i]
        #
        data = plt.imread(imagepath).astype(float)
        #
        image_data = 0.2989 * data[:, :, 0] + 0.5870 * data[:, :, 1] + 0.1140 * data[:, :, 2]
        if np.max(data[:, :, 0]) * np.max(data[:, :, 1]) * np.max(data[:, :, 2]) != 0:
            image_data = image_data * 3.0 / (np.max(data[:, :, 0]) + np.max(data[:, :, 1]) + np.max(data[:, :, 2]))
        if np.shape(data)[2] > 3:
            image_data = image_data + 1.0 - data[:, :, 3]
        #
        image_x = np.linspace(0.0, 1.0, np.shape(image_data)[1])
        image_y = np.linspace(0.0, 1.0, np.shape(image_data)[0])
        f_interp = interpolate.interp2d(image_x, image_y, image_data)

        temp1 = np.flipud(f_interp(xlrange, inlrange))
        seis3dmat[i, :, :] = temp1.transpose()
    #
    if qpgsdlg is not None:
        qpgsdlg.setValue(nzsls)

    return seis3dmat


class visualization:
    # pack all functions as a class
    #
    plotSeisILSliceFrom2DMat = plotSeisILSliceFrom2DMat
    plotSeisILSliceFrom3DMat = plotSeisILSliceFrom3DMat
    plotSeisXLSliceFrom2DMat = plotSeisXLSliceFrom2DMat
    plotSeisXLSliceFrom3DMat = plotSeisXLSliceFrom3DMat
    plotSeisZSliceFrom2DMat = plotSeisZSliceFrom2DMat
    plotSeisZSliceFrom3DMat = plotSeisZSliceFrom3DMat
    plotSeisILXLZSliceFrom3DMat = plotSeisILXLZSliceFrom3DMat
    #
    plotSeisILSlicePlayerFrom2DMat = plotSeisILSlicePlayerFrom2DMat
    plotSeisILSlicePlayerFrom3DMat = plotSeisILSlicePlayerFrom3DMat
    plotSeisXLSlicePlayerFrom2DMat = plotSeisXLSlicePlayerFrom2DMat
    plotSeisXLSlicePlayerFrom3DMat = plotSeisXLSlicePlayerFrom3DMat
    plotSeisZSlicePlayerFrom2DMat = plotSeisZSlicePlayerFrom2DMat
    plotSeisZSlicePlayerFrom3DMat = plotSeisZSlicePlayerFrom3DMat
    plotSeisZTracePlayerFrom2DMat = plotSeisZTracePlayerFrom2DMat
    plotSeisZTracePlayerFrom3DMat = plotSeisZTracePlayerFrom3DMat
    plotSeisILXLZSlicePlayerFrom3DMat = plotSeisILXLZSlicePlayerFrom3DMat
    #
    saveSeisILSliceFrom2DMat = saveSeisILSliceFrom2DMat
    saveSeisILSliceFrom3DMat = saveSeisILSliceFrom3DMat
    saveSeisXLSliceFrom2DMat = saveSeisXLSliceFrom2DMat
    saveSeisXLSliceFrom3DMat = saveSeisXLSliceFrom3DMat
    saveSeisZSliceFrom2DMat = saveSeisZSliceFrom2DMat
    saveSeisZSliceFrom3DMat = saveSeisZSliceFrom3DMat
    #
    loadSeisILSliceTo2DMat = loadSeisILSliceTo2DMat
    loadSeisILSliceTo3DMat = loadSeisILSliceTo3DMat
    loadSeisXLSliceTo2DMat = loadSeisXLSliceTo2DMat
    loadSeisXLSliceTo3DMat = loadSeisXLSliceTo3DMat
    loadSeisZSliceTo2DMat = loadSeisZSliceTo2DMat
    loadSeisZSliceTo3DMat = loadSeisZSliceTo3DMat
