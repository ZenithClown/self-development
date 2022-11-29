# -*- encoding: utf-8 -*-

"""
❓ Problem : ##### 💪 (difficulty)
📜 Question Description

🔗 Explanatory Example - #
```shell

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
