#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:33:11 2017

@author: Neo

Re-produce the result of Example 1.24

"""

from acf_ccf import acorf
import numpy as np
import matplotlib.pyplot as plt


# ------------------------------  FUNCTIONS  -----------------------------


# ------------------------------  MAIN BODY  -----------------------------
# Load data
DAT = np.genfromtxt('../data/speech.dat')
N = DAT.size
# Calculate ACF
acf = acorf(DAT)
# Plot ACF
plt.figure(figsize=(10, 6))
plt.plot(acf)
plt.xlabel('LAG')
plt.ylabel('ACF')
plt.xlim([0, 250])
plt.xticks(np.arange(0, 251, 50))
plt.show()
print('Done!')
# ------------------------------ END -----------------------------------
