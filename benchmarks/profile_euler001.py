# -*- encoding: utf-8 -*-

"""
The file is meant to do a profiling on function(s) for a given
problem. Using the inbuilt `functools` and `timeit` module of python,
to run tests, and let end-user know the performance.

A problem from ProjectEuler/ProjectEuler+ can have multiple level of
optimization possible. In contrast, the `layman` function is defined
which is generally the worst possible approach. Further modification,
and/or optimizations are provided under each solution file.

❓ Problem Number  : 001

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2020 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""

import os
import sys
import time
import timeit
import functools

if __name__ == "__main__":
    ROOT = os.path.join("..") # considering `project-euler` directory
    sys.path.append(ROOT) # allows to import from `euler001.py` files

    from euler001 import layman
    print(f"{time.ctime()} Performing Tests for 001...")
    t = timeit.Timer(functools.partial(layman, 100000)).timeit(number = 1000) # perform `number` of times
    print(f" > `layman` Run Time: {round(t, 3)} secs.")
