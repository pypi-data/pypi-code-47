import numpy as np
from scipy.stats import chi2

from .functions import phasor_covariance


def tihaar2D(R0, R1, R2=0, Rirf1=1, Rirf2=1, Nb=0, pvalue=1, L=None, mask=None):
    '''
    R0: number of photons
    R1: phasor harmonic n
    R2: phasor harmonic 2n
    pvalue: pvalue threshold
    L: levels
    '''
    threshold = chi2.isf(pvalue, df=2)

    if mask is None:
        mask = np.zeros_like(R0, dtype=bool)

    if L is None:
        L = int(np.log2(np.min(R1.shape)))

    N = np.zeros((L + 1,) + R0.shape)
    cov = np.zeros((L,) + R0.shape + (2, 2))
    wavelet_h = np.zeros((L,) + R0.shape, dtype=complex)
    wavelet_v = np.zeros((L,) + R0.shape, dtype=complex)
    wavelet_d = np.zeros((L,) + R0.shape, dtype=complex)
    masksum = np.zeros((L + 1,) + R0.shape, dtype=bool)
    maskprod = np.zeros((L + 1,) + R0.shape, dtype=bool)

    N[0] = R0
    masksum[0] = ~mask
    maskprod[0] = ~mask
    for iL in range(L):
        shift = -2 ** iL
        R10 = circshift(R1, shift, 0)
        R01 = circshift(R1, 0, shift)
        R11 = circshift(R1, shift, shift)
        wavelet_h[iL] = R1 + R10 - R01 - R11
        wavelet_v[iL] = R1 - R10 + R01 - R11
        wavelet_d[iL] = R1 - R10 - R01 + R11
        cov[iL] = phasor_covariance(N[iL][..., None, None], R1, R2=R2)  # , Nb=Nb, mask=masksum[iL])

        masksum[iL + 1] = sumall(masksum[iL], shift)
        maskprod[iL + 1] = prodall(maskprod[iL], shift)
        N[iL + 1] = sumall(N[iL], shift)
        R1 = sumall(N[iL] * R1, shift)
        R2 = sumall(N[iL] * R2, shift)
        R1[masksum[iL + 1]] /= N[iL + 1][masksum[iL + 1]]
        R2[masksum[iL + 1]] /= N[iL + 1][masksum[iL + 1]]

    for iL in range(L):
        C = sumall(cov[iL], shift)
        cond = np.logical_and(np.linalg.det(C) > 0, maskprod[iL + 1])
        C[cond] = np.linalg.inv(C[cond])
        wavelet_h[iL][np.logical_and(cond, quadraticForm(C, wavelet_h[iL]) < threshold)] = 0
        wavelet_v[iL][np.logical_and(cond, quadraticForm(C, wavelet_v[iL]) < threshold)] = 0
        wavelet_d[iL][np.logical_and(cond, quadraticForm(C, wavelet_d[iL]) < threshold)] = 0

    for iL in reversed(range(L)):
        shift = 2 ** iL

        R1 = (R1 + 1 / N[iL + 1] * (
                + (circshift(N[iL], 0, -shift) + circshift(N[iL], -shift, -shift)) * wavelet_h[iL]
                + (circshift(N[iL], -shift, 0) + circshift(N[iL], -shift, -shift)) * wavelet_v[iL]
                + (circshift(N[iL], 0, -shift) + circshift(N[iL], -shift, 0)) * wavelet_d[iL]) / 2
              + circshift(R1 + 1 / N[iL + 1] * (
                        - (circshift(N[iL], 0, 0) + circshift(N[iL], -shift, 0)) * wavelet_h[iL]
                        + (circshift(N[iL], -shift, 0) + circshift(N[iL], -shift, -shift)) * wavelet_v[iL]
                        - (circshift(N[iL], 0, 0) + circshift(N[iL], -shift, -shift)) * wavelet_d[iL]) / 2, 0, shift)
              + circshift(R1 + 1 / N[iL + 1] * (
                        + (circshift(N[iL], 0, -shift) + circshift(N[iL], -shift, -shift)) * wavelet_h[iL]
                        - (circshift(N[iL], 0, 0) + circshift(N[iL], 0, -shift)) * wavelet_v[iL]
                        - (circshift(N[iL], 0, 0) + circshift(N[iL], -shift, -shift)) * wavelet_d[iL]) / 2, shift, 0)
              + circshift(R1 + 1 / N[iL + 1] * (
                        - (circshift(N[iL], 0, 0) + circshift(N[iL], -shift, 0)) * wavelet_h[iL]
                        - (circshift(N[iL], 0, 0) + circshift(N[iL], 0, -shift)) * wavelet_v[iL]
                        + (circshift(N[iL], 0, -shift) + circshift(N[iL], -shift, 0)) * wavelet_d[iL]) / 2, shift,
                          shift)) / 4
    return np.ma.masked_array(R1, mask=mask, fill_value=np.nan)


def circshift(a, *shifts):
    out = a
    for ax, shift in enumerate(shifts):
        out = np.roll(out, shift, axis=ax)
    return out


def sumall(a, shift):
    return a + circshift(a, 0, shift) + circshift(a, shift, 0) + circshift(a, shift, shift)


def prodall(a, shift):
    return a * circshift(a, 0, shift) * circshift(a, shift, 0) * circshift(a, shift, shift)


def quadraticForm(A, x):
    return A[..., 0, 0] * x.real ** 2 + A[..., 1, 1] * x.imag ** 2 + 2 * A[..., 0, 1] * x.real * x.imag
