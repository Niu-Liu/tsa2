#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:50:00 2017

@author: Neo

Re-produce the result of Example 1.25.

"""

import numpy as np
import matplotlib.pyplot as plt
from acf_ccf import acorf, ccorfa


# ------------------------------  MAIN BODY  -----------------------------
# Load data
soi = np.genfromtxt('../data/soi.dat')
rec = np.genfromtxt('../data/recruit.dat')
# Calculate ACF
acfs = acorf(soi, 50)
acfr = acorf(rec, 50)
# Calculate CCF
ccf = ccorfa(soi, rec, 50)
# Plot ACF and CCF
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
# ACF of SOI
ax0.plot(acfs)
ax0.hlines(y=0, xmin=0, xmax=50, linewidth=0.5)
ax0.set_ylabel('ACF of SOI')
ax0.set_xlim([0, 50])
# ax0.set_xticks(np.arange(0, 51, 5))
# ACF of Recruitment
ax1.plot(acfr)
ax1.hlines(y=0, xmin=0, xmax=50, linewidth=0.5)
ax1.set_ylabel('ACF of Rer')
ax1.set_xlim([0, 50])
# ax1.set_xticks(np.arange(0, 51, 5))
# CCF
ax2.plot(np.arange(-49, 50), ccf)
ax2.hlines(y=0, xmin=-50, xmax=50, linewidth=0.5)
ax2.set_ylabel('CCF')
ax2.set_xlabel('LAG')
ax2.set_xlim([-50, 50])
ax2.set_ylim([-0.6, 1.0])
# ax2.set_xticks(np.arange(-50, 51, 5))
plt.show()
print('Done!')
# ------------------------------ END -----------------------------------
