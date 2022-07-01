# -*- encoding: utf-8 -*-

"""
The function provides a more optimized solution for the problem stated
in Q001. Check documentation for more information.

The function is also benchmarked using `timeit` module, to understand
the performance. TODO update documentation and/or template.
"""

import math

def sum_of_multiples(n : int, x : int) -> int:
    """
    Calculates the sum of all the multiples of `x` for numbers below
    `n`, and returns the result.

    :type  n: int
    :param n: Final number below which multiple is required, i.e.
              check for numbers in `range(n)`.

    :type  x: int
    :param x: Multiples of `x` is required to be checked for `[0, n)`
    """

    n = n - 1 # exclusive of `n`
    p = math.floor(n / x) # can check till this range

    return x * ((p * (p + 1)) / 2)
