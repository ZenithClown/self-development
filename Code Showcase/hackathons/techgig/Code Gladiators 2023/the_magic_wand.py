# -*- encoding: utf-8 -*-

import time
import pstats
import random
import cProfile

cum_abs_diff = lambda li, v : sum([abs(i - v) for i in li])

def brute_force(arr : list, queries : list) -> str:
    # main function is created for cProfiling
    return " ".join([str(cum_abs_diff(arr, q)) for q in queries])

if __name__ == "__main__":
    # input is from STDIN, and output to STDOUT
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    # Q = list(map(int, input().split()))

    random.seed(7)
    # N, M = 5, 3
    print(f"{time.ctime()} : Operation `random(seed = 7)` to Create `A` & `Q`.")
    A = [random.randint(1, 10 ** 5) for _ in range(10 ** 6)]
    Q = [random.randint(1, 10 ** 5) for _ in range(10 ** 6)]
    print(f"  {time.ctime()} : Array Initialized. Array Length : <A = {len(A)}, Q = {len(Q)}>")
    
    print(f"{time.ctime()} : Starting cProfile (for `brute_force()` method)...")
    with cProfile.Profile() as profile:
        result_ = brute_force(A, Q) # ? not printing, as take less time
    
    print(f"  {time.ctime()} : Generating Results...")
    print("====================================================\n")
    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
