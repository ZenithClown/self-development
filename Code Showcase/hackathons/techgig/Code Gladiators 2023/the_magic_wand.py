# -*- encoding: utf-8 -*-

cum_abs_diff = lambda li, v : sum([abs(i - v) for i in li])

if __name__ == "__main__":
    # input is from STDIN, and output to STDOUT
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    print(" ".join([str(cum_abs_diff(A, q)) for q in Q]))
