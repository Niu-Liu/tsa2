#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:45:31 2017

@author: Neo

A sample to generate a time series when given a model.
In this sample, x[t] = -0.9 * x[t-2] + w[t]
where w[t] is white noise with variance 1.
"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------  FUNCTIONS  -----------------------------
def ts_gen(max, w):
    # i, a, b, c = 0, 0, 0, 0
    i, a, b = 0, 0, 0
    while i < max:
        # c = -0.9 * a + w[i]
        a, b = b, -0.9 * a + w[i]
        yield b
        # a, b, c = b, c, a
        i = i + 1


# ------------------------------  MAIN BODY  -----------------------------
# ============  Generate a Gaussioan white nosie  ===========
mu, sigma = 0, 1  # mean and standard deviation
w = np.random.normal(mu, sigma, 100)
# ============  Genereate a signals  ============
# 1) use xrange for iteration
t = np.arange(100)
xa = np.zeros(100)
# For model (a)
xa[:2] = w[:2]
for i in range(2, 100):
    xa[i] = -0.9 * xa[i - 2] + w[i]
# 2) use a generator and iterator.
x = np.array([xi for xi in ts_gen(100, w)])
# ============  Plot the differences  ============
plt.plot(x - xa)
plt.show()
print('Done!')
# ------------------------------ END -----------------------------------
