#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
import sys
import numpy as np
from scipy import interpolate
import pandas as pd
import os
import subprocess
from io import StringIO


class Twiss:
    def __init__(self, path):
        super(Twiss, self).__init__()
        self.path = path
        try:
            subprocess.run(['elegant', 'twiss.ele'])
            self.twi = 'twiss.twi'
        except Exception as exp:
            print(exp)
        self.df_mag = self.read_structure()
        self.df = self.read_twiss()
        sys.exit()

    def read_structure(self):
        try:
            out = subprocess.Popen(['sdds2stream', self.path + 'results/beamline.mag', '-col=ElementName,s,Profile', '-pipe=out'],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = out.communicate()
            output = stdout.decode('utf-8').splitlines()
            data = StringIO("\n".join(output))
            df_mag = pd.read_csv(data, names=['ElementName', 's', 'Profile'], delim_whitespace=True)
            return df_mag
        except Exception as exp:
            print(exp)
            return None

    def read_twiss(self):
        try:
            out = subprocess.Popen(['sdds2stream', self.path + 'results/' + self.twi,
                                    '-col=ElementName,s,betax,betay,alphax,alphay,etax,etay,pCentral0,xAperture,yAperture',
                                    '-pipe=out'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = out.communicate()
            output = stdout.decode('utf-8').splitlines()
            data = StringIO("\n".join(output))
            df = pd.read_csv(data, names=['ElementName', 's', 'betax', 'betay', 'alphax', 'alphay', 'etax', 'etay', 'p',
                                          'xAperture', 'yAperture'], delim_whitespace=True)
            return df
        except Exception as exp:
            print(exp)
            return None

    def _sddspar(self, par):
        out = subprocess.Popen(['sdds2stream',  self.path + 'results/' + self.twi, '-par=' + par],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        return float(stdout)

    def bet_freq(self):
        return self._sddspar('nux'), self._sddspar('nuy')

    def chrom(self):
        return self._sddspar('dnux/dp'), self._sddspar('dnuy/dp')

    def acc_view(self):
        out = subprocess.Popen(['sdds2stream', self.path + 'results/xyz.sdds', '-col=ElementName,s,X,Y,Z,theta,phi,psi',
                                '-pipe=out'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        output = stdout.decode('utf-8').splitlines()
        data = StringIO("\n".join(output))
        df_xyz = pd.read_csv(data, names=['ElementName', 's', 'X', 'Y', 'Z', 'theta', 'phi', 'psi'],
                             delim_whitespace=True)
        theta = interpolate.interp1d(df_xyz.s.values, df_xyz.theta.values, fill_value=(0, 0), bounds_error=False)
        x0 = interpolate.interp1d(df_xyz.s.values, df_xyz.X.values, fill_value=(0, 0), bounds_error=False)
        z0 = interpolate.interp1d(df_xyz.s.values, df_xyz.Z.values, fill_value=(0, 0), bounds_error=False)

        df_mag = self.read_structure()
        s = df_mag.s.values
        nx = np.cos(theta(s))
        nz = -np.sin(theta(s))
        element_width = 0.5  # m
        df_mag['X'] = x0(s) + element_width * df_mag['Profile'] * nx
        df_mag['Z'] = z0(s) + element_width * df_mag['Profile'] * nz

        return df_mag


if __name__ == "__main__":
    app = QApplication(['Twiss'])
    w = Twiss()
    sys.exit(app.exec_())
