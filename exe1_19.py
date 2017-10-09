#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:25:26 2017

@author: Neo

Exercise 1.19.

"""

import numpy as np
import matplotlib.pyplot as plt
from acf_ccf import acorf


# ------------------------------  MAIN BODY  -----------------------------
# Generate a Gaussioan white nosie.
mu, sigma = 0, 1  # mean and standard deviation
w = np.random.normal(mu, sigma, 50)
# Calculate the auto-correlation function
acf = acorf(w, 20)
# Plot ACF.
plt.plot(acf)
plt.xlim([0, 20])
plt.show()
print('Done!')
# ------------------------------ END -----------------------------------
