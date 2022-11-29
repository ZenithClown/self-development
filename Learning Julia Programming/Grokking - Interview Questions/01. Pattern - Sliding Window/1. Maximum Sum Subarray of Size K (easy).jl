# -*- encoding: utf-8 -*-

"""
❓ Problem : Maximum Sum Subarray of Size K 💪 (easy)
📜 Question Description

Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size'k'.

🔗 Explanatory Example - 1
```shell
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
```

🔗 Explanatory Example - 2
```shell
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
```

🤓 @author: Debmalya Pramanik
🏷️ Copyright (c) 2022 Debmalya Pramanik
📧 dPramanik.official@gmail.com
"""

# let's define the inputs
arr, k = [2, 1, 5, 1, 3, 2], 3

# define control statements
len = length(arr) - k + 1
max_ = 0 # ! TODO : define as `-infinity`

for idx in 1:4 # * we can start at any index, and x ∈ [start, stop]
    subarr = arr[idx : idx + k - 1] # * as we are indexing from `1`
    println(subarr)
    
    if sum(subarr) > max_
        max_ = sum(subarr)
    end
end

print("Max. Sum of Sub Array = ", max_)
