# -*- encoding: utf-8 -*-

"""
❓ Problem : Maximum Sum Subarray of Size K 💪 (easy)
📜 Question Description

Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size'k'.

🔗 Explanatory Example - 1
```shell
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
```

🔗 Explanatory Example - 2
```shell
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
```

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2022 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""


import time
import timeit
import functools
from typing import Iterable

import numpy as np

def layman(arr : Iterable, k : int) -> Iterable:
    """
    A `layman` solution to the problem is one which may not be the
    most efficient one, but this is the one solution that I have used
    initially. If a better solution is found then the same is
    available in the later section of "this" document. I've also used
    the `timeit` module to check the performance of the code/function
    that is used to solve the problem.

    # parameters are self explanatory and/or as described statement.
    """
    
    len_ = len(arr) - k + 1 # iterate the elements, and use slicing
    max_ = [- float("inf"), []] # [<value>, <subarray>]
    for i in range(len_):
        subarr = arr[i : i + k]
        if sum(subarr) > max_[0]:
            max_[0] = sum(subarr)
            max_[1] = subarr

    return max_


if __name__ == "__main__":
    # run this code from command line as `python filename.py`
    # defined below the `inputs` for the function `layman` or others
    # arr, k = [2, 1, 5, 1, 3, 2], 3 # as provided in problem description
    arr, k = np.random.randint(0, 100001, size = 1000), 3

    # using the `functools.partial` to run the code and also display output
    partial_function = functools.partial(layman, arr, k)

    print(f"{time.ctime()} Checking Code Performance...")
    
    t1 = timeit.Timer(partial_function).timeit(number = 1000) # perform `number` of times
    print(f" > `layman` Run Time: {round(t1, 7)} secs.")
    print(f" > `layman` Solution: {partial_function()}")
