# -*- encoding: utf-8 -*-

"""
❓ Problem : Smallest Subarray With a Greater Sum 💪 (easy)
📜 Question Description

Given an array of positive integers and a number 'S' find the length
of the smallest contiguous subarray whose sum is greater than or
equal to 'S'. Return 0 if no such subarray exists.

🔗 Explanatory Example - 1
```shell
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
```

🔗 Explanatory Example - 2
```shell
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
```

🔗 Explanatory Example - 3
```shell
Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8'' are [3, 4, 1] or [1, 1, 6].
```

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2022 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""


import time
import timeit
import functools


def layman() -> None:
    """
    A `layman` solution to the problem is one which may not be the
    most efficient one, but this is the one solution that I have used
    initially. If a better solution is found then the same is
    available in the later section of "this" document. I've also used
    the `timeit` module to check the performance of the code/function
    that is used to solve the problem.
    """
    pass


if __name__ == "__main__":
    # run this code from command line as `python filename.py`
    # defined below the `inputs` for the function `layman` or others
    var = "variable"

    # using the `functools.partial` to run the code and also display output
    partial_function = functools.partial(layman, var)

    print(f"{time.ctime()} Checking Code Performance...")
    
    t1 = timeit.Timer(partial_function).timeit(number = 1000) # perform `number` of times
    print(f" > `layman` Run Time: {round(t1, 3)} secs.")
    print(f" > `layman` Solution: {partial_function()}")
