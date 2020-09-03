#!/bin/python3

def solver(n : int) -> int:
	vals = [i for i in range(1, n) if i % 3 == 0 or i % 5 == 0]
	return sum(vals)