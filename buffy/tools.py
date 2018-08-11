"""
This file should contain standalone routines to be used throughout the project
"""

import numpy as np

def generate_poly(x, y, lim, deg=3):
    """
    Fit a polynomial to given x and y data
    Then generate data points from between the limit so it can be plotted
    :param x:
    :param y:
    :param lim:
    :return: 20 data points on the polynomial
    """
    dt = (lim[0] - lim[1]) / 20
    poly = np.polyfit(x, y, deg=deg)
    return np.array([
        [i, np.polyval(poly, i)]
        for i in np.arange(*lim, dt)
    ])