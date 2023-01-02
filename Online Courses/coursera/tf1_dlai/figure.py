# -*- encoding: utf-8 -*-

"""
A list of utility functions related to figure objects, i.e., using
the `matplotlib` and `seaborn` libraries.
"""

from typing import List

import seaborn as sns
import matplotlib.pyplot as plt

def plot(x : List[int], y : List[int] or List[List[int]], format : str = "-", start : int = 0, end : int = None, **kwargs) -> None:
    """
    A simple function to visualize the time series data plotted in `x` and `y`
    axis, where `x` axis denotes the time, and `y` denotes the value at a
    given timestamp. To simplify, time is denoted as list of integer, where
    each day is denoted as number (i.e., day 1, day 2, etc.). Optionally, the
    plot can be zoomed in by using the `start` and `end` paramters.

    :type  x, y: array-like
    :param x, y: List of integers representing the day number and the value at
                 each given timestamp (i.e., day/month/etc.).
    """

    sns.set_style('whitegrid');
    plt.style.use('default-style');

    if type(y) == tuple:
        for idx, series in enumerate(y):
            plt.plot(x, series[start:end], format, label = kwargs.get("label")[idx])
    else:
        plt.plot(x, y[start:end], format, label = kwargs.get("label"))

    plt.xlabel("Time Stamp")
    plt.ylabel("y-Values")

    plt.legend()
    plt.show()
