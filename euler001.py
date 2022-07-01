# -*- encoding: utf-8 -*-

"""
❓ Problem Number  : 001
❔ Question Link   : https://projecteuler.net/problem=1
❔ HackerRank Link : https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

📜 Question Description/Title: Multiples of 3 or 5

🔗 Project Euler : https://projecteuler.net/about
🔗 Hacker Rank   : https://www.hackerrank.com/contests/projecteuler/challenges

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2020 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""

layman = lambda n = 100 : sum([i for i in range(1, n) if (i % 3 == 0) or (i % 5 == 0)])

if __name__ == "__main__":
    n = int(input("Enter a Number: ").strip())

    # print layman solution
    # this is not an optimized solution
    print(layman(n))
