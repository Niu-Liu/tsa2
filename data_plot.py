#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:20:08 2017

@author: neo
"""

import matplotlib.pyplot as plt
import numpy as np
# =========== Example 1.1 ==================
# Load data
# DAT = np.genfromtxt('../data/jj.dat')
# x = np.arange(DAT.size) * 0.25
# plt.plot(x, DAT)
# plt.show()
# =========== Example 1.7 ==================
# Load data
DAT = np.genfromtxt('../data/eq5exp6.dat')
N = DAT.size // 2
Ear, Exp = DAT[:N], DAT[N:]
fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
ax0.plot(Ear)
ax0.set_title('Earthquake')
ax1.plot(Exp)
ax1.set_title('Explosion')
plt.xlim([0, N])
plt.xticks([0, N // 2, N])
plt.show()
