# -*- encoding: utf-8 -*-

"""
A list of utility function to generate a synthetic curve for analysis
and statistical/machine learning applications.
"""

import numpy as np
from typing import List

trend = lambda time, slope = 0 : slope * time # generate a st. ln. slope


# an arbitary pattern is generated using the `seasonal_pattern()`
seasonal_pattern = lambda season_time : np.where(season_time < 0.4, np.cos(season_time * 2 * np.pi), 1 / np.exp(3 * season_time))


# the seasonal data is generated by using the `seasonal_pattern()` and a same pattern repeated each 365 days
def seasonality(time : List[int], period : int, amplitude : int = 0, phase : int = 0) -> np.ndarray:
    season_time = ((time + phase) % period) / period
    return amplitude * seasonal_pattern(season_time)


# add noise to the data to simulate real world behaviour
def noise(time : List[int], level : int = 1, seed : int = None) -> np.ndarray:
    random = np.random.RandomState(seed)
    return random.randn(time.shape[0]) * level
