# -*- encoding: utf-8 -*-

"""
Provides a List of Utility Functions for Visualizations

The code uses the `seaborn` and `matplotlib` libraries to showcase
different visualizations which are required in many projects.

@author: Debmalya Pramanik
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def corr_heatmap(df : pd.DataFrame, annot : bool = True, **kwargs):
    """
    Calculates Correlation of all Variables using `pd.corr()` and
    returns a heatmap using `seaborn` after performing/modifying the
    contents of the heatmap for better understanding.

    :type  df: object
    :param df: Original dataframe on which correlation heatmap is to
               be performed. The function uses the in-built pandas
               method.

    :type  annot: bool
    :param annot: Annotate heatmap labels. Defaults to True. When set
                  to True, then other keyword arguments can be used
                  to control the nature of the map.
    """

    copy = kwargs.get("copy", True) # perform deep copy operation on df
    tau_ = kwargs.get("annot_threshold", 0.65) # performs `applymap` operation

    if copy:
        df = df.copy() # deepcopy

    corr = df.corr() # calculate correlation

    if annot:
        # return an annotated heatmap
        # TODO include other parameter controls
        labels = corr.applymap(lambda x : str(round(x, 2)) if (x <= - tau_ or x >= tau_) else '')
    else:
        labels = None # defaults of `sns.heatmap`

    return sns.heatmap(corr, annot = labels, fmt = '')
