"""
This file should contain standalone routines to be used throughout the project
"""

import numpy as np

def generate_poly(x, y, lim):
    poly = np.polyfit(x, y, deg=3)
    return np.array([
        [i, np.polyval(poly, i)]
        for i in np.arange(*lim, 0.02)
    ])