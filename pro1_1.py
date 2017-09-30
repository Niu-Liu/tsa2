#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:20:44 2017

@author: neo
"""
import matplotlib.pyplot as plt
import numpy as np
# Load data
DAT = np.genfromtxt('../data/eq5exp6.dat')
N = DAT.size // 2
Ear, Exp = DAT[:N], DAT[N:]
fig, ax = plt.subplots(figsize=(14, 4))
x = np.arange(N)
ax.plot(Ear, 'b', label='Earthquake')
ax.plot(Exp, 'r', label='Explosion')
plt.xlim([0, N])
plt.xticks([0, N // 2, N])
plt.legend()
plt.savefig('../figures/1_1.eps', dpi=100)
plt.show()
