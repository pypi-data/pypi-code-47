# vi: sw=4 ts=4 sts=4 expandtab

import ophyd
from ophyd import Component as Cpt
from ophyd.areadetector import CamBase
from ophyd.areadetector.plugins import (ColorConvPlugin, HDF5Plugin,
                                        ImagePlugin, JPEGPlugin, NetCDFPlugin, OverlayPlugin, ProcessPlugin, ROIPlugin,
                                        StatsPlugin, TIFFPlugin, TransformPlugin, NexusPlugin)

class PCDSDet(ophyd.AreaDetector):
    '''
    Detector class containing all (*) common PCDS AreaDetector plugins

    (*) Currently excludes all PVAccess plugins:
        IMAGE1:Pva
        IMAGE2:Pva:
        THUMBNAIL:Pva
    '''
    cam = Cpt(CamBase, '')
    image1 = Cpt(ImagePlugin, 'IMAGE1:')
    image1_roi = Cpt(ROIPlugin, 'IMAGE1:ROI:')
    image1_cc = Cpt(ColorConvPlugin, 'IMAGE1:CC:')
    image1_proc = Cpt(ProcessPlugin, 'IMAGE1:Proc:')
    image1_over = Cpt(OverlayPlugin, 'IMAGE1:Over:')
    image2 = Cpt(ImagePlugin, 'IMAGE2:')
    image2_roi = Cpt(ROIPlugin, 'IMAGE2:ROI:')
    image2_cc = Cpt(ColorConvPlugin, 'IMAGE2:CC:')
    image2_proc = Cpt(ProcessPlugin, 'IMAGE2:Proc:')
    image2_over = Cpt(OverlayPlugin, 'IMAGE2:Over:')
    thumbnail = Cpt(ImagePlugin, 'THUMBNAIL:')
    thumbnail_roi = Cpt(ROIPlugin, 'THUMBNAIL:ROI:')
    thumbnail_cc = Cpt(ColorConvPlugin, 'THUMBNAIL:CC:')
    thumbnail_proc = Cpt(ProcessPlugin, 'THUMBNAIL:Proc:')
    thumbnail_over = Cpt(OverlayPlugin, 'THUMBNAIL:Over:')
    cc1 = Cpt(ColorConvPlugin, 'CC1:')
    cc2 = Cpt(ColorConvPlugin, 'CC2:')
    hdf51 = Cpt(HDF5Plugin, 'HDF51:')
    jpeg1 = Cpt(JPEGPlugin, 'JPEG1:')
    netcdf1 = Cpt(NetCDFPlugin, 'NetCDF1:')
    nexus1 = Cpt('Nexus1:', 'NetCDF1:')
    over1 = Cpt(OverlayPlugin, 'Over1:')
    proc1 = Cpt(ProcessPlugin, 'Proc1:')
    roi1 = Cpt(ROIPlugin, 'ROI1:')
    roi2 = Cpt(ROIPlugin, 'ROI2:')
    roi3 = Cpt(ROIPlugin, 'ROI3:')
    roi4 = Cpt(ROIPlugin, 'ROI4:')
    stats1 = Cpt(StatsPlugin, 'Stats1:')
    stats2 = Cpt(StatsPlugin, 'Stats2:')
    stats3 = Cpt(StatsPlugin, 'Stats3:')
    stats4 = Cpt(StatsPlugin, 'Stats4:')
    stats5 = Cpt(StatsPlugin, 'Stats5:')
    tiff1 = Cpt(TIFFPlugin, 'TIFF1:')
    trans1 = Cpt(TransformPlugin, 'Trans1:')


det = PCDSDet('CXI:SC3:INLINE:', name='det')
