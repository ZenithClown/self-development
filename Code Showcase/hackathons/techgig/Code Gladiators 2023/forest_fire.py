# -*- encoding: utf-8 -*-

"""
The problem tries to find out the optimal value of energy (P) such
that exactly X animals can be saved in a forest fire. Check the
read me file for more information about the problem. The hackathon is
hosted on TechGig/Code Gladiators 2023

@author: Debmalya Pramanik
"""

import os
import sys

counter = lambda li : {k : li.count(k) for k in sorted(set(P), reverse = True)}

def get_min_energy(X : int, P : list) -> int:
    """
    Calculate the Minimum Energy (P) to Save X Animals

    The function takes in the input parameters, and calculates the
    minimum energy required to save the required number of animals in
    the forest fire.

    :type  X: int
    :param X: Number of animals that can be saved in the forest fire
              due to limitation of transport facility.

    :type  P: array-like
    :param P: Energy of all the animals (N) in an array/iterable
              format.
    """

    counter_ = counter(P) # calculate energy wise count in reverse
    
    x = 0
    for k, v in counter_.items():
        x += v # number of animals for each energy level
        
        P = 0
        if x == X:
            # we have found the optimal energy point
            P = k; break
        elif x > X:
            # it is not possible to save `X` animals with a `P` value
            P = -1; break
        else:
            continue
            
    return P

if __name__ == "__main__":
    # input is from STDIN, and output to STDOUT
    N, X = map(int, input().split())
    P = sorted(list(map(int, input().split())))

    print(get_min_energy(X, P)) # STDOUT of Min. Energy
