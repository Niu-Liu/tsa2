#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:54:54 2017

@author: neo
"""
import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
# ============  Moving average filter  ===========
def maf(x):
    '''va_t = (xa_t + xa_{t-1} + xa{t-2} + t_{t-3})/4'''
    N = x.size
    v = np.zeros(N)
    v[:3] = x[:3]
    for i in range(3, N):
        v[i] = np.sum( x[i-3: i+1] )/4
    return v
# ============  Generate a Gaussioan white nosie  ============
mu, sigma = 0, 1 # mean and standard deviation
w = np.random.normal(mu, sigma, 100)
# ============  Genereate a signals  ============
t = np.arange(100)
xa = np.zeros(100)
# For model (a)
xa[:2] = t[:2]
# Autoregression xa_t = -0.9*xa_{t-2} + w_t
for i in range(2, 100):
    xa[i] = -0.9 * xa[i-2] + w[i]
# Moving average filter
va = maf(xa)
# For model (b)
xb = np.cos( 2*pi*t/4 )
vb = maf(xb)
# For model (c)
xc = xb + w
vc = maf(xc)
# ============  Plot  ===============
# (a)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(xa, 'b-',  label='$x_t$')
ax.plot(va, 'b--', label='$v_t$')
ax.set_title('Model (a)')
plt.xlim([0, 100])
plt.legend()
plt.savefig('../figures/1_3a.eps', dpi=100)
plt.close()
# (b)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(xb, 'b-',  label='$x_t$')
ax.plot(vb, 'b--', label='$v_t$')
ax.set_title('Model (b)')
plt.xlim([0, 100])
plt.legend()
plt.savefig('../figures/1_3b.eps', dpi=100)
plt.close()
# (c)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(xc, 'b-',  label='$x_t$')
ax.plot(vc, 'b--', label='$v_t$')
ax.set_title('Model (c)')
plt.xlim([0, 100])
plt.legend()
plt.savefig('../figures/1_3c.eps', dpi=100)
plt.close()
# (c)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(xa - xc, 'b-',  label='$x_t$')
ax.plot(va - vc, 'b--', label='$v_t$')
ax.set_title('Model (a) - (c)')
plt.xlim([0, 100])
plt.legend()
plt.savefig('../figures/1_3a_c.eps', dpi=100)
plt.close()
