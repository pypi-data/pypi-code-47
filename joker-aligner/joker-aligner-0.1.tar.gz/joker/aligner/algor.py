#!/usr/bin/env python3
# coding: utf-8

from __future__ import unicode_literals, print_function

import ctypes
import pkgutil

import numpy as np
from numpy.ctypeslib import ndpointer


def locate_lib():
    ldr = pkgutil.get_loader('joker.aligner.library.align')
    return ldr.get_filename()


class Alignment(object):
    CI_DEFAULT = '-'
    CM_DEFAULT = '.'

    __slots__ = ['matrix', '_istr', '_jstr', 'ci', 'cm']

    def __init__(self, matrix, istr, jstr):
        self.ci = self.CI_DEFAULT
        self.cm = self.CM_DEFAULT
        self.matrix = matrix
        self._istr = istr
        self._jstr = jstr

    def reconf(self, ci=CI_DEFAULT, cm=CM_DEFAULT):
        self.ci = ci
        self.cm = cm
        return self

    @property
    def score(self):
        return self.matrix[-1, -1, 2]

    def get_istr(self):
        return self._istr.replace('\0', self.ci)

    def get_jstr(self):
        return self._jstr.replace('\0', self.ci)

    def get_xstr(self):
        iarr = np.fromstring(self._istr, dtype='uint8')
        jarr = np.fromstring(self._jstr, dtype='uint8')

        # set all remaining positions to cmis
        marr = np.empty(len(self._istr), dtype='uint8')
        marr[:] = ord(self.cm)

        # if same char, use that char
        mask = iarr ^ jarr
        marr[mask == 0] = iarr[mask == 0]
        marr[(iarr & jarr) == 0] = ord(self.ci)
        return marr.tostring().decode()

    def debug(self):
        print(self.get_istr())
        print(self.get_xstr())
        print(self.get_jstr())

    def debug_backtrack(self):
        symbols = ord('-'), ord('|'), ord('\\'), ord('3')
        symbols = np.array(symbols, dtype='uint8')
        idx = self.matrix[:, :, 3]
        darr = symbols[idx]
        for row in darr:
            line = row.tostring().decode('ascii')
            yield line


class Aligner(object):
    index_type = ctypes.c_int64
    score_type = ctypes.c_int64
    short_type = ctypes.c_int16
    score_dtype = 'int64'
    index_dtype = 'int64'
    GLOBAL, OVERLAP, LOCAL = 1, 2, 3

    def __init__(self, rho, sigma, reference, scheme=GLOBAL):
        """
        :param rho: gap opening penalty
        :param sigma: gap extension penalty
        :param reference: see `from_submat` method
        :param scheme: 1 for global, 2 for overlap, 3 for local
        """
        self.rho = rho
        self.sigma = sigma
        self.scheme = scheme
        self.reference = reference

        arrflags = 'C'

        self.lib = ctypes.cdll.LoadLibrary(locate_lib())
        self.build = self.lib.build
        self.build.argtypes = [
            ndpointer(self.score_type, flags=arrflags),
            self.index_type,  # isize
            self.index_type,  # jsize
            self.score_type,  # rho
            self.score_type,  # sigma
            self.short_type,  # local_
        ]

        self.backtrack = self.lib.backtrack
        self.backtrack.rettype = self.index_type
        self.backtrack.argtypes = [
            ndpointer(self.score_type, flags=arrflags),
            self.index_type,  # isize
            self.index_type,  # jsize
            self.index_type,  # istart
            self.index_type,  # jstart
            ndpointer(self.index_type, flags=arrflags),  # iarr index
            ndpointer(self.index_type, flags=arrflags),  # jarr index
            self.short_type,  # global_
        ]

    @classmethod
    def from_submat(cls, istr, jstr, submat, rho=12, sigma=1, scheme=GLOBAL):
        reference = np.zeros(2 ** 16, dtype=submat.dtype)
        iarr = np.fromstring(istr, 'uint8')
        jarr = np.fromstring(jstr, 'uint8')
        ixarr = cls.build_ixarr(iarr, jarr)

        # magic indexing, Step 1: set values
        reference[ixarr] = submat
        return cls(rho, sigma, reference, scheme=scheme)

    def compute(self, istr, jstr, backtrack=False):
        """
        :param istr: (str)
        :param jstr: (str)
        :param backtrack: (bool) do backtrack? True or False
        :return:    (matrix, istr_arr, jstr_arr)
        """
        isize = len(istr) + 1
        jsize = len(jstr) + 1

        # convert strings to 1d arrays
        iarr = np.empty(isize, dtype='uint8')
        jarr = np.empty(jsize, dtype='uint8')

        iarr[1:] = np.fromstring(istr, dtype='uint8')
        jarr[1:] = np.fromstring(jstr, dtype='uint8')

        # indels
        iarr[0] = 0
        jarr[0] = 0

        ixarr = self.build_ixarr(iarr, jarr)
        matrix = np.empty(shape=[isize, jsize, 4], dtype=self.score_dtype)

        # mark scores on matrix
        # magic indexing, Step 2: get values
        matrix[:, :, 2] = self.reference[ixarr]

        # overlap and local
        if self.scheme in (self.OVERLAP, self.LOCAL):
            matrix[:, 0, :3] = 0  # j = 0, of isize x 3
            matrix[0, :, :3] = 0  # i = 0, of jsize x 3
        else:
            # TODO: when sigma == 0
            border = np.arange(max(isize, jsize), dtype='int') * -1 * self.sigma
            border.shape = -1, 1
            matrix[:, 0, :3] = border[:isize]
            matrix[0, :, :3] = border[:jsize]

        matrix[:, 0, 3] = 0
        matrix[0, :, 3] = 1
        matrix[0, 0, 3] = 3

        # dynamic programming -- main step
        self.build(matrix, isize, jsize, self.rho, self.sigma, self.scheme)

        if not backtrack:
            return matrix, None, None

        # caution: isize + jsize, not max(isize, jsize)!
        ipos_arr = np.empty(isize + jsize, dtype=self.index_dtype)
        jpos_arr = np.empty(isize + jsize, dtype=self.index_dtype)

        print('start backtrack')
        # TODO: local / overlap backtrack not from last point
        # backtrack -- another major step
        x = self.backtrack(
            matrix, isize, jsize, isize - 1, jsize - 1, ipos_arr, jpos_arr, self.scheme)

        # print('sizes:', x, iarr.shape, jarr.shape)
        return matrix, iarr[ipos_arr[:x]], jarr[jpos_arr[:x]]

    @classmethod
    def build_ixarr(cls, iarr, jarr):
        """
        Build an array of indexes. Each value represent a pair of letters.
        :param iarr: a 1d array representing a string
        :param jarr: a 1d array representing a string
        :return: a 2d array
        """
        iarr = iarr.astype('uint16') << 8
        jarr = jarr.astype('uint16')
        iarr[0] = 0
        jarr[0] = 0
        iarr.shape = -1, 1
        jarr.shape = 1, -1
        return iarr | jarr

    def __call__(self, istr, jstr, backtrack=False):
        """
        :param istr: (str)
        :param jstr: (str)
        :param backtrack: (bool)
        :return: (Alignment or number)
        If backtrack is true, return an Alignment object;
        else return the final score.
        """
        matrix, iarr, jarr = self.compute(istr, jstr, backtrack=backtrack)
        if not backtrack:
            return matrix[-1, -1, 2]
        return Alignment(
            matrix,
            iarr.tostring()[::-1].decode(),
            jarr.tostring()[::-1].decode(),
        )
