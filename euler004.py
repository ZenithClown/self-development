# -*- encoding: utf-8 -*-

"""
❓ Problem Number  : 004
❔ Question Link   : https://projecteuler.net/problem=4
❔ HackerRank Link : https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

📜 Question Description/Title: Largest Palindrome Product of n-Digits

🔗 Project Euler : https://projecteuler.net/about
🔗 Hacker Rank   : https://www.hackerrank.com/contests/projecteuler/challenges

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2020 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""

from itertools import combinations

check = lambda num : str(num) == str(num)[::-1]
layman = lambda n : [int(i * j) for i, j in combinations(range(1, 10 ** n), 2) if check(i * j)]

if __name__ == "__main__":
    n = int(input("N: ").strip())

    # get all products which are palindrome
    products = layman(n)
    print(max(products))
