#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:43:36 2017

@author: Neo

Calculate the auto-covariance and cross-covariance functions.

"""

import numpy as np


# ------------------------------  FUNCTIONS  -----------------------------
def ccovf(x, y, n=0):
    '''Calculate the sample cross-covariance function CCovF(h).

    Parameters
    ----------
    x, y : arrays
       time series data
    n : int, positive
       the maximum of lag

    Returns
    -------
    CCovF : array
        cross-covariance function CCovF(h) at h =0, 1, ..., n-1.
    '''
    if x.size != y.size:
        print('The lenght of x and y must be equal.')
        return 0

    if not n:
        n = x.size

    rsdx, rsdy = x - np.mean(x), y - np.mean(y)
    N = rsdx.size
    CCovF = np.zeros(n)
    for i in range(n):
        CCovF[i] = np.dot(rsdx[i:], rsdy[:N-i]) / N

    return CCovF


def ccovfa(x, y, n=0):
    '''
    Calculate the sample cross-covariance function CCovF(h)
    at h = -(n-1), -(n-2), ..., 0, 1, ..., n-1.

    For h >= 0, use the function ccovf defined above.
    For h < 0, use the relation
        CCovF(x, y, -h) = CCovF(y, x, h).

    Parameters
    ----------
    x, y : arrays
       time series data
    n : int, positive
       the maximum of lag

    Returns
    -------
    CCovFa : array
        cross-covariance function CCovF(h) at
        h = -(n-1), -(n-2), ..., 0, 1, ..., n-1.
    '''
    if x.size != y.size:
        print('The lenght of x and y must be equal.')
        return 0

    if not n:
        n = x.size

    CCovFp = ccovf(x, y, n)  # for h >= 0 (positive)
    CCovFn = ccovf(y, x, n)  # for h < 0  (negative)

    CCovFa = np.hstack((CCovFn[n-1:0:-1], CCovFp))

    return CCovFa


def acovf(x, n=0):
    '''Calculate the sample auto-covariance function ACovF(h).

    Here we can use the function ccovf defined above.

    Parameters
    ----------
    x : arrays
       time series data
    n : int, positive
       the maximum of lag

    Returns
    -------
    ACovF : array
        autocovariance function ACovF(h) at h = 0, 1, ..., n-1.
    '''
    if not n:
        n = x.size

    return ccovf(x, x, n)


def acorf(x, n=0):
    '''
    Calculate the sample autocorrelation function ACorF(h).

    ACorF(h) = ACovF(h) / ACovF(0)

    Parameters
    ----------
    x : arrays
       time series data
    n : int, positive
       the maximum of lag

    Returns
    -------
    ACorF : array
        autocorrelation function ACorF(h) at h = 0, 1, ..., n-1.
    '''
    if not n:
        n = x.size

    ACovF = acovf(x, n)

    return ACovF / ACovF[0]


def ccorf(x, y, n=0):
    '''
    Calculate the sample cross-correlation function CCorF(h).

    CCorF(h) = CCovF(h) / (acovf_x(0)*acovf_y(0))**0.5

    Parameters
    ----------
    x, y : arrays
       time series data
    n : int, positive
       the maximum of lag

    Returns
    -------
    CCorF : array
        cross-correlation function CCorF(h) at h = 0, 1, ..., n-1.
    '''
    if not n:
        n = x.size

    ACovFx, ACovFy = acovf(x, 1), acovf(y, 1)
    div = np.sqrt(ACovFx[0] * ACovFy[0])

    return ccovf(x, y, n) / div


def ccorfa(x, y, n=0):
    '''
    Calculate the sample cross-correlation function CCorF(h).

    CCorF(h) = CCovF(h) / (acovf_x(0)*acovf_y(0))**0.5

    Parameters
    ----------
    x, y : arrays
       time series data
    n : int, positive
       the maximum of lag

    Returns
    -------
    CCorF : array
        cross-correlation function CCorF(h) at
        h = -(n-1), -(n-2), ..., 0, 1, ..., n-1.
    '''
    if not n:
        n = x.size

    ACovFx, ACovFy = acovf(x, 1), acovf(y, 1)
    div = np.sqrt(ACovFx[0] * ACovFy[0])

    return ccovfa(x, y, n) / div

# ------------------------------  MAIN BODY  -----------------------------
# # A test, using the Example 1.23 on page 31.
# # Add a tail -1 and a head 1
# x = np.array([-1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1])
# N = 10
# y = 5 + x[1:-1] - 0.7 * x[:N]
# # Calculate the autocovariance function of y.
# acf_y = acovf(y)
# if acf_y[4] == -0.04848:
#     print('Bingo!')
# else:
#     print('There must be something wrong, please check the code!')
# print('Done!')
# ------------------------------ END -----------------------------------
