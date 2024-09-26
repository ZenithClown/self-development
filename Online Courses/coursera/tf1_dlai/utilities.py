# -*- encoding: utf-8 -*-

"""
A Set of Utility Functions for TensorFlow/Keras Model Development

Developing a model is the easy part, but processing and transforming
the data into a correct dimension and feature scaling is important!
The functions here does just the same, transformations and scaling of
data using the utility functions.
"""

import numpy as np
import tensorflow as tf

def create_xy(series : np.ndarray, window_size : int, batch_size : int, shuffle_buffer : int, **kwargs):
    """
    Process a `np.ndarray` into XY Lables for AI-ML Time Series Analysis
    
    Consider a 1D-Array the data splits and process it into `xy` where `x` is
    the number of features set by the "window" element and `y` is the last
    element for each data split. For detailed methodlogies check each
    steps as dicussed above.
    """
    
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift = kwargs.get("shift", 1), drop_remainder = True)
    dataset = dataset.flat_map(lambda window : window.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer).map(lambda window : (window[:-1], window[-1]))
    
    return dataset.batch(batch_size).prefetch(1)
