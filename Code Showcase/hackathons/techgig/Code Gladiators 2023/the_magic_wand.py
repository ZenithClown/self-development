# -*- encoding: utf-8 -*-

counter = lambda li : {k : li.count(k) for k in set(A)}
# cum_abs_diff = lambda li, v : sum([abs(i - v) for i in li])
cum_abs_diff = lambda di, v : sum([abs(key - v) * value for key, value in di.items()])

if __name__ == "__main__":
    # input is from STDIN, and output to STDOUT
    N, M = map(int, input().split())
    A = (list(map(int, input().split())))
    Q = list(map(int, input().split()))

    # create a counter dictionary from A
    A = counter(A)

    print(" ".join([str(cum_abs_diff(A, q)) for q in Q]))
