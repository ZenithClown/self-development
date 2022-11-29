## Solution

<p align = "justify">A brute force solution to the problem is to iterate a given array of elements $(x_1, x_2, ..., x_n)$ from starting index to $n - k$ index (where <code>n</code> is the number of elements and <code>k</code> is the sub-array size) and find the sum of each elements. Each of the window ( $W$ ) is of size $k$ elements, and find the individual sub-array size. Finally find the maximum value of each elements. The diagram below displays the <a href = "https://github.com/ZenithClown/self-development/blob/master/Learning%20Python%20Programming/Grokking%20-%20Interview%20Questions/01.%20Pattern%20-%20Sliding%20Window/1.%20Maximum%20Sum%20Subarray%20of%20Size%20K%20(easy).py#L36">layman solution</a> approach considered for solving the problem.</p>

![Layman Solution](https://gitlab.com/ZenithClown/grokking-assets/-/raw/main/Maximum%20Sum%20Subarray%20of%20Size%20K.drawio.svg)

### Simple Algorithm to Find the Maximum

<p align = "justify">There are many libraries and inbuilt functions like <code>max()</code> for finding the maximum value from a given array/lists. However, the most basic algorithm can be stated as:</p>

```shell
1. Start at index = 0
2. let `max = - infinity`
3. for elements till `n-k`:
   a. let value = sum(array[index : index + k])
   b. if value > max:
      max = value
   c. index ++
4. echo max # print to console
```
