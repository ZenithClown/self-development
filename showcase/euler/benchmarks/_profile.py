# -*- encoding: utf-8 -*-

"""
The file is meant to do a profiling on function(s) for a given
problem. Using the inbuilt `functools` and `timeit` module of python,
to run tests, and let end-user know the performance.

A problem from ProjectEuler/ProjectEuler+ can have multiple level of
optimization possible. In contrast, the `layman` function is defined
which is generally the worst possible approach. Further modification,
and/or optimizations are provided under each solution file.

Use the file to test a given function, and print the time taken to
produce output. In addition, the script uses visualization library to
produce image.

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2020 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""

import os
import sys
import time
import timeit
import functools

import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ROOT = os.path.join("..") # considering `project-euler` directory
    LIBS = os.path.join(ROOT, "include") # a better optimized solution

    sys.path.append(ROOT) # allows to import from `euler###.py` files
    sys.path.append(LIBS) # allows to import from `euler###_.py` files

    # global arguments to control the file and output structure
    PROBLEM_NUMBER = "0001" # as on 19.10.2022 there are 802 problems, provision for 9999

    # import the file(s) and function(s) w.r.t. a given problem
    # ? check the question number, and import the same from respective file
    from euler001 import layman
    from euler001_ import sum_of_multiples

    print(f"{time.ctime()} Performing Tests for `{PROBLEM_NUMBER}`...")
    n = 100000 # for which result is to be checked
    
    t1 = timeit.Timer(functools.partial(layman, n)).timeit(number = 1000) # perform `number` of times
    print(f" > `layman` Run Time: {round(t1, 3)} secs.")

    # define a lambda function that will calculate the final result
    total = lambda n : int(sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15))

    t2 = timeit.Timer(functools.partial(total, n)).timeit(number = 1000) # perform `number` of times
    print(f" > `sum_of_multiples` Run Time: {round(t2, 3)} secs.")

    # * plot the figure and save in directory
    sns.set_style('whitegrid');
    plt.style.use('default-style');

    fig, axs = plt.subplots(figsize = (25, 3))
    sns.barplot(x = [t1, t2], y = ["layman", "sum_of_multiples"], ax = axs)

    axs.bar_label(axs.containers[-1], fmt = "%.3f s")
    axs.set_xlabel("time $\longrightarrow$")

    plt.suptitle("Performance Benchmark for #0001")
    plt.tight_layout()
    plt.savefig(os.path.join(".", "0001-9999", f"{PROBLEM_NUMBER}.png"))
