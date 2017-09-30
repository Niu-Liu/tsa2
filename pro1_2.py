#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:31:44 2017

@author: neo
"""
import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
# ============  Generate a Gaussioan white nosie  ============
mu, sigma = 0, 1 # mean and standard deviation
w = np.random.normal(mu, sigma, 200)
# ============  Genereate a signals  ============
t = np.arange(101, 201, 1)
s1 = np.zeros(100)
# For model (a)
sa_2 = 10 * np.exp( -(t-100)/20 ) * np.cos( 2*pi*t/4 )
sa = np.hstack( (s1, sa_2) )
xa = sa + w
# For model (b)
sb_2 = 10 * np.exp( -(t-100)/200 ) * np.cos( 2*pi*t/4 )
sb = np.hstack( (s1, sb_2) )
xb = sb + w
# ============  Plot  ===============
fig, ax = plt.subplots(figsize=(14, 4))
# ax.plot(xa, 'b', label='Model a')
# ax.plot(xb, 'r', label='Model b')
# plt.xlim([0, 200])
# plt.legend()
# plt.savefig('../figures/1_2.eps', dpi=100)
# plt.show()
# # For test
# t = np.arange(100)
# y1 = np.exp( -t/20 )
# y2 = np.exp( -t/200 )
# ax.plot(y1, 'b', label = 'exp{-t/20}')
# ax.plot(y2, 'r', label = 'exp{-t/200}')
# plt.xlim([0, 100])
# plt.show()
