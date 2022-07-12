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
    LIBS = os.path.join(ROOT, "include")
    sys.path.append(ROOT) # allows to import from `euler###.py` files
    sys.path.append(LIBS) # allows to import from `euler###_.py` files

    from euler001 import layman
    from euler001_ import sum_of_multiples
    print(f"{time.ctime()} Performing Tests for 001...")
    n = 100000 # for which result is to be checked
    
    t1 = timeit.Timer(functools.partial(layman, n)).timeit(number = 1000) # perform `number` of times
    print(f" > `layman` Run Time: {round(t1, 3)} secs.")

    # define a lambda function that will calculate the final result
    total = lambda n : int(sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15))

    t2 = timeit.Timer(functools.partial(total, n)).timeit(number = 1000) # perform `number` of times
    print(f" > `sum_of_multiples` Run Time: {round(t2, 3)} secs.")
