# -*- encoding: utf-8 -*-

"""
Provides a List of Utility Functions for pandas DataFrame

The utility functions is provided to modify a pandas dataframe, and
perform certain operations that might make the dataframe perform
faster and/or improve performance.

@author: Debmalya Pramanik
"""

import gc # garbage collection handling module
import warnings # warn user when something is wrong
import numpy as np # pandas is built over np-dtypes
import pandas as pd # pandas module for dataframes
from typing import Iterable # let user know of data types
from tqdm import tqdm as TQ # display a nice progress bar


def reduce_mem_usage(df : pd.DataFrame, subset : Iterable[str], copy : bool = True, verbose : bool = True, **kwargs) -> pd.DataFrame:
    """
    Iterate through a pandas dataframe (against all columns/features) and modify the data
    types to reduce the memory usage. The original code is presented by Bartosz Mikulski
    (https://www.mikulskibartosz.name/how-to-reduce-memory-usage-in-pandas/), and I've
    modified the code with some arguments.

    :type  df: object
    :param df: Original pandas dataframe, which is to be modified to reduce memory usage.
               For each given column, the algoritm finds the maximum and minimum value, and
               then set the data type to a minimum required time.

    :type  subset: array-like
    :param subset: Perform modification of data types on ONLY the given selected columns,
                   and ignore all other columns.

    :type  copy: bool
    :param copy: Dataframes are mutable, and when multiple variables points to a same object,
                 they point to the same memory pointer. Thus, updating/modifying any one
                 variable results in changing both the object. When set to `True`, the code
                 uses the inbuilt `.copy(deepcopy = True)` function to create a copy.
                 Defaults to True.

    :type  verbose: bool
    :param verbose: Let end user know about some basic details, and operations that are being
                    performed on the dataframe. Defaults to True.

    Keyword Arguments
    -----------------
        * *num_cast* (`bool`): Cast number columns/features, i.e. integer and/or float, to its
          respective lower required version. Defaults to True.

        * *obj_cast* (`bool`): Cast object columns/features, to 'categorical' type. This does not
          include a `datetime` column. Defaults to True.

    Returns
    -------
        :rtype:  object
        :return: A replica of the original dataframe, where each column/feature's data types is
                 casted to a lower required version.
    """

    initial_memory = df.memory_usage().sum() / 1024 ** 2 # in mega byte
    gc.collect() # https://docs.python.org/3/library/gc.html#gc.collect
    print(f"Initial Memory: {initial_memory:.2f} MB")

    if copy:
        df = df.copy() # deep copy

    # assign keyword arguments with default values
    # num_cast = kwargs.get("num_cast", True) # TODO: number casting
    obj_cast = kwargs.get("obj_cast", True)

    cols = subset or df.columns.tolist() # set of columns
    for col in TQ(cols, desc = "Reducing Memory Usage"):
        col_type = str(df[col].dtype) # get the current columns data type

        if col_type not in ["object", "category"] and "datetime" not in col_type:
            # this section will only perform operations on number data types
            # no operations are to be performed on datetime columns
            c_min = df[col].min() # get the column's min value
            c_max = df[col].max() # get the column's max value
            
            # integer casting
            if "int" in col_type.lower():
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
                else:
                    warnings.warn(f"`{col_type}` for {col} operation is not yet addressed. ")
            
            # float casting
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

        if "datetime" not in col_type and obj_cast:
            df[col] = df[col].astype('category')

    gc.collect()
    final_memory = df.memory_usage().sum() / 1024 ** 2 # in mega byte
    print(f"Final Memory (after optimization): {final_memory:.2f} MB")
    print(f"  > Decreased by {((initial_memory - final_memory) / initial_memory) * 100:.2f}%")

    return df
