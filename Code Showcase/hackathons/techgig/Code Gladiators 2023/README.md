<div align = "center">

![CG Logo 2023](https://www.techgig.com/files/contest_upload_files/cg-logo-2023.png)
# Code Gladiators 2023

</div>

<div align = "justify">

Code Gladiators is an annual coding competition by TechGig. This directory hosts my `python` based solution for the event held from 27th March - 7th August 2023.
The two problem statements are described below.
  
## Problem 1: Forest Fire (100 Marks)

You are camping in a forest area at night. You are living with the forest officers to experience their challenges and hardships to create a documentary on them. Everything was going well. Suddenly, a fire has broken out in the forest and it is expanding exponentially. There is a lot of chaos and cries of animals. It is going to take alot of time for the backup. Some of the posts in the forest have also caught fire. The officers are trying everything to safeguard the animals but the fire is spreading too fast. Amid such chaos, the petrol tankers of the officers have also caught fire. The fire is unstoppable now and the commanding officer is taking important decisions with his officers.

The officers know the energy levels of all the $N$ animals in the forest at the moment. It is a tough decision for them as they can only save exactly $X$ animals because of the current situation of the transports they have. Since, the animals are pride of the forest, the energy level of the animals are represented with $P$. _All the animals with energy level equal to $P$ or greater than $P$ can board the available transports and they will be moved to a safer place. But since the capacity is for exactly $X$ animals_ it is going to be tough to figure out.

Officer needs your help to **figure out the minimum energy level $P$ such that they can get exactly $X$ animals to transport. If it is not possible to save exactly $X$ animals, then you should respond with $-1$ so that they can think of some other plan.** The officers are busy trying to get control of the fire and are counting on you to figure out the minimum $P$ to save and transport exactly $X$ animals.

### Example & Use Case
Number of Animals, $N = 5$ with Energy Levels as ${1, 3, 2, 4, 5}$, and Current available Capacity $X = 4$, then you should chose $P = 2$, so that exactly $4$ animals with energy levels $(2, 3, 4, 5)$ can be saved as these have energies greater than or equal to $P$.

<div align = "center">

![Example Illustrations](./cg_pb1_ex1.png)

</div>

### Input Format

The **first line** of input consists of two space-separated integers, $N$ (number of animals) and $X$ (available capacity for animals that can be transported). The **second line** of input consists of N space-separated integers, representing the energy of all the animals.

**`CONSTRAINTS`**
  * Number of Animals: $1 \leq N 10^5$ 
  * Number of Animals that can be Saved: $1 \leq X \leq N$
  * Energy Level of Animals: $1 \leq A_i \leq 10^{12}$, where $A_i$ represents the energy level of $i$-th animal.

### Output Format
Print the minimum energy level $P$ such that exactly $X$ animals can be saved or transported. If it is not possible to save exactly X animals, then print `-1`.

### Code & Explanation
Code file is available in [`forest_fire.py`](./forest_fire.py). Approach is simple, for each element, update `x` which gives the current number of animals that can be saved for a given energy level. Based on it, the output is generated.

## Problem 2: The Magic Wand

You are a wizard who possesses a magical wand that can be used to change the values of an array. Your **wand has two powers: `Increase` and `Decrease`**. With each use of the wand, you can either *increase or decrease any element of the array* by `1`.

One day, a group of villagers came to you with a problem. They had an array of positive integers of size $N$ and a set of queries of size $M$. For each query, $Q_i$ (`queries[i]`), they wanted to make all the elements of the array equal to `queries[i]` using your magic wand.

To help the villagers, you decided to use your magic wand to perform the operations. However, each time you perform an operation, the cost of using your wand increases. **The cost of using your wand for an operation on an element is equal to the absolute difference between the value of the element and the desired value after the operation.**

### Example & Use Case

If you want to change an element from 5 to 3, it will cost you 2 (since, $|5 - 3| = 2$). If you want to change an element from 7 to 8, it will cost you 1 (as, $|7 - 8| = 1$). You can perform any number of operations on any element of the array for a given query. However, the cost of using the wand for each operation accumulates, and you want to minimize the total cost of all operations for each query.

### Input Format

The **first line** of the input consists of two space-separated integers $N$ (length of array) and $M$ (length of queries). The **second line** of input consists of $N$ space-separated integers `arr[i]`. The **third line** of input consists of $M$ space-separated integers `queries[i]`.

**`CONSTRAINTS`**
  * Length of Array: $1 \leq N \leq 10^5$
  * Length of Queries: $1 \leq M \leq 10^5$
  * Values of N: $1 \leq a_i \leq 10^9$
  : Values of M: $1 \leq Q_i \leq 10^9$

### Output Format

Print a list of integers of cost of length **`m`**, where `cost[i]` is the minimum cost to make all elements of nums equal to `queries[i]`.

```
# Input Format:
5 3
1 2 3 4 5
5 2 1

# Output Format:
10 7 10
```

### Code & Explanation
Code file is available in [`the_magic_wand.py`](./the_magic_wand.py). The problem is solved using `brute_force()` approach, however the code fails due to **"Time Limit Exceeded"** because of huge array size. The array `A` and `Q` is generated considering maximum constraint (as in problem) using:

```python
import random

if __name__ == "__main__":
  random.seed(7)
  A = [random.randint(1, 10 ** 5) for _ in range(10 ** 6)]
  Q = [random.randint(1, 10 ** 5) for _ in range(10 ** 6)]
```

The code is profiled using [`cProfile`](https://docs.python.org/3/library/profile.html#module-cProfile) and [`pstats`](https://docs.python.org/3/library/profile.html#module-pstats) module, and the results are as below:

```shell
```

## Disclaimer

The code commits are in-between the events, however they are hosted on GitHub (i.e. made public from this repository) after the end of event for fair play and usage. This code is shared for learning purposes, and is not shared on public domain before the end of the event.

</div>
