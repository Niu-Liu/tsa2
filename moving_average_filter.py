#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:49:23 2017

@author: Neo

Apply a moving average filter to an array.

"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------  MAIN BODY  -----------------------------
# Generate a Gaussioan white nosie.
N = 500
mu, sigma = 0, 1  # mean and standard deviation
w = np.random.normal(mu, sigma, N)
# Use a moving average filter v[t] = (w[t-1] + w[t] + w[t+1]) / 3.0
# 1) a normal way
v = np.empty(N)
# For head
v[0] = (w[0] + w[1]) / 3.0
# For tail
v[-1] = (w[-2] + w[-1]) / 3.0
# For else
v[1:-1] = (w[:-2] + w[1:-1] + w[2:]) / 3.0
# 2) use np.convolve() function
n = 3
window = np.ones(n) * 1.0 / n
v1 = np.convolve(window, w, mode='same')
# Plot the result.
plt.plot(v1 - v)
plt.xlim([0, N])
plt.legend()
plt.show()
print('Done!')
# ------------------------------ END -----------------------------------
