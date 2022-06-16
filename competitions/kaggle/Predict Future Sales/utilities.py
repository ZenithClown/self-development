# -*- encoding: utf-8 -*-

"""
A list of utility functions used for Kaggle Competion:
Predicting Future Sales.

@author  : Debmalya Pramanik
@contact : dPramanik.official@gmail.com
"""

import pandas as pd

def read_file(filepath : str) -> pd.DataFrame:
    """
    Read a CSV File from the given `filepath` and Return Data

    The function is specifically developed to read `sales_train` data,
    format date column and append item categories and items to it.
    """

    data = pd.read_csv(filepath) # parse dates with `pd.to_datetime`
    data["date"] = pd.to_datetime(data["date"], format = "%d.%m.%Y")

    return data.copy() # deepcopy
