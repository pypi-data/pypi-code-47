#############################################################################################
#                                                                                           #
# Author:   GeoPy Team                                                                      #
# Email:    geopy.info@gmail.com                                                            #
# Date:     January 2019                                                                    #
#                                                                                           #
#############################################################################################

# pre-stack seismic data processing functions

from PyQt5 import QtCore
import sys, os
import numpy as np
#
sys.path.append(os.path.dirname(__file__)[:-4][:-4][:-13])
from cognitivegeo.src.vis.messager import messager as vis_msg


__all__ = ['analysis']

# Shot information is packed as a dictionary contains the following keys,
#   'ZNum' ----- number of z samples
#   'ZStart' ----- first z
#   'ZStep' ----- z step
#   'ZEnd' ------ last z
#   'ZRange' ----- all z as a 1D array
#   'XLNum' ----- number of xlines
#   'XLStart' ----- first xlines
#   'XLStep' ----- xline step
#   'XLEnd' ------ last xline
#   'XLRange' ----- all xlines as a 1D array
#   'ILNum' ----- number of inlines
#   'ILStart' ----- first inlines
#   'ILStep' ----- inline step
#   'ILEnd' ------ last inline
#   'ILRange' ----- all inlines as a 1D array
#   'TraeFlag' ----- 2D array of the missing-trace flag. 1 for missing trace


def checkPsSeis(psseis):
    """
    Check if a pre-stack seismic dictionary good to use

    Args:
        psseis: A pre-stack seismic dictionary, with each key representing a shot dictionary.
                A shot dictionary contains the following keys,
                    'ShotData' ----- Shot data as a 3D array [Z/XL/IL]
                    'ShotInfo' ----- Shot information as a dictionary defined above
    Return:
    """

    if len(psseis.keys()) < 1:
        return False
    #
    for shot in psseis.keys():
        if 'ShotData' not in psseis[shot].keys() or 'ShotInfo' not in psseis[shot].keys():
            return False
        if 'ZNum' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ZStart' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ZEnd' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ZStep' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ZRange' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'XLNum' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'XLStart' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'XLEnd' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'XLStep' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'XLRange' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ILNum' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ILStart' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ILEnd' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ILStep' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'ILRange' not in psseis[shot]['ShotInfo'].keys():
            return False
        if 'TraceFlag' not in psseis[shot]['ShotInfo'].keys():
            return False
    #
    return True


def createShotInfoFromShotData(shotdata, zstart=0, zstep=-1, xlstart=0, xlstep=1, inlstart=0, inlstep=1):
    """
    Create a ShotInfo dictionary from shot data, with given parameters.

    Args:
        shotdata:   3D array of the shot data [Z/XL/IL]
        zstart:     First z. Default is 0
        zstep:      Step along z (negative). Default is -1
        xlstart:    First xline. Default is 0
        xlstep:     Step of xline. Default is 1
        inlstart:   First inline. Default is 0
        inlstep:    Step of inline. Default is 1

    Return:
         A shot information dictionary as defined above
    """

    info = makeShotInfo()
    if np.ndim(shotdata) < 3:
        vis_msg.print('ERROR in createShotInfo: shot data in 3D matrix', type='error')
        sys.exit()
    #
    info['ZNum'], info['XLNum'], info['ILNum'] = np.shape(shotdata)
    info['ZStart'] = zstart
    info['ZStep'] = zstep
    info['ZEnd'] = zstart + (info['ZNum'] - 1) * zstep
    info['ZRange'] = np.linspace(info['ZStart'], info['ZEnd'], info['ZNum'])
    info['XLStart'] = xlstart
    info['XLStep'] = xlstep
    info['XLEnd'] = xlstart + (info['XLNum'] - 1) * xlstep
    info['XLRange'] = np.linspace(info['XLStart'], info['XLEnd'], info['XLNum'])
    info['ILStart'] = inlstart
    info['ILStep'] = inlstep
    info['ILEnd'] = inlstart + (info['ILNum'] - 1) * inlstep
    info['ILRange'] = np.linspace(info['ILStart'], info['ILEnd'], info['ILNum'])
    info['TraceFlag'] = np.zeros([info['XLNum'], info['ILNum']])
    # check trace flag
    for i in range(info['ILNum']):
        for j in range(info['XLNum']):
            if np.min(shotdata[:, j, i]) >= np.max(shotdata[:, j, i]):
                info['TraceFlag'][j, i] = 1
    #
    return info


def makeShotInfo(inlstart=0, inlstep=1, inlnum=1,
                 xlstart=0, xlstep=1, xlnum=1,
                 zstart=0, zstep=-1, znum=1):
    """
    Make a new shot information dictionary

    Args:
        inlstart:   first inline. Default is 0
        inlstep:    inline step. Default is 1
        inlnum:     inline number. Default is 1
        xlstart:    first xline. Default is 0
        xlstep:     xline step. Default is 1
        xlnum:      xline number. Default is 1
        zstart:     first z. Default is 0
        zstep:      z step. Default is -1
        znum:       z number. Default is 1

    Return:
        Seismic inforamtion dictionary as defined above
    """

    shotinfo = {}
    shotinfo['ILStart'] = inlstart
    shotinfo['ILEnd'] = inlstart + (inlnum - 1) * inlstep
    shotinfo['ILStep'] = inlstep
    shotinfo['ILNum'] = inlnum
    shotinfo['ILRange'] = np.linspace(0, inlnum - 1, 1) * inlstep + inlstart
    shotinfo['XLStart'] = xlstart
    shotinfo['XLEnd'] = xlstart + (xlnum - 1) * xlstep
    shotinfo['XLStep'] = xlstep
    shotinfo['XLNum'] = xlnum
    shotinfo['XLRange'] = np.linspace(0, inlnum - 1, 1) * xlstep + xlstart
    shotinfo['ZStart'] = zstart
    shotinfo['ZEnd'] = zstart + (znum - 1) * zstep
    shotinfo['ZStep'] = zstep
    shotinfo['ZNum'] = znum
    shotinfo['ZRange'] = np.linspace(0, inlnum - 1, 1) * zstep + zstart
    shotinfo['TraceFlag'] = np.zeros([shotinfo['XLNum'], shotinfo['ILNum']])

    return shotinfo


class analysis:
    checkPsSeis = checkPsSeis
    #
    createShotInfoFromShotData = createShotInfoFromShotData
    #
    makeShotInfo = makeShotInfo