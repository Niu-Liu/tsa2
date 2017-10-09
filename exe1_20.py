#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:33:02 2017

@author: Neo

Exercise 1.20.


"""

import numpy as np
import matplotlib.pyplot as plt
from acf_ccf import acorf


# ------------------------------  MAIN BODY  -----------------------------
# Generate a Gaussioan white nosie.
N = 500
mu, sigma = 0, 1  # mean and standard deviation
w = np.random.normal(mu, sigma, N)
# Use a moving average filter v[t] = (w[t-1] + w[t] + w[t+1]) / 3.0
v = np.empty(N)
# For head
v[0] = (w[0] + w[1]) / 3.0
# For tail
v[-1] = (w[-2] + w[-1]) / 3.0
# For else
v[1:-1] = (w[:-2] + w[1:-1] + w[2:]) / 3.0
# Calculate the auto-correlation function
acf = acorf(v, 20)
# Plot ACF.
plt.plot(acf)
plt.xlim([0, 5])
plt.show()
print('Done!')
# ------------------------------ END -----------------------------------
