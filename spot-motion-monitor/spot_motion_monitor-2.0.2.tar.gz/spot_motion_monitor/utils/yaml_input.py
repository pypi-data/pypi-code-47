# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

__all__ = ["YAML_INPUT"]


YAML_INPUT = \
    '''
    camera:
      roi:
        size: 50
        fps: 50
      full:
        fps: 30
      spotOscillation:
        do: true
        x:
          amplitude: 10
          frequency: 1.0
        y:
          amplitude: 5
          frequency: 2.0
    data:
      buffer:
        pixelScale: 1.0
        size: 512
      fullFrame:
        minimumNumPixels: 10
        sigmaScale: 5.0
      roiFrame:
        thresholdFactor: 0.3
    general:
      autorun: true
      configVersion: "1.5.2"
      site: null
      telemetry:
        cleanup:
          directory: true
          files: true
        directory: null
      timezone: UTC
    plot:
      centroid:
        scatterPlot:
          histograms:
            numBins: 40
        xCentroid:
          autoscaleY: PARTIAL
          maximumY: null
          minimumY: null
        yCentroid:
          autoscaleY: PARTIAL
          maximumY: null
          minimumY: null
      psd:
        waterfall:
          colorMap: viridis
          numBins: 25
        xPSD:
          autoscaleY: true
          maximumY: null
        yPSD:
          autoscaleY: true
          maximumY: null
    '''
