# # -*- encoding: utf-8 -*-

# """
# Problem Name: Two Sum
# Probelm Description: This is a type of `windowing` problem,
#     as available in Grokking Interview Prepartion Series.

# About the LeetCode Editor: The program is executed directly from the
# mentioned `class.function()` using `result = ClassName.function(*args, **kwargs)` thus,
# do not change/modify the initial code (different from other coding platforms). Use the
# `reset` button, if you have misplaced the original code.
# """



# def combos(array : List[int]) -> List[int]:
#     """
#     Given an `array` of `n`-elements, the function lists out all the element
#     combinations from the array. This is different from that available without
#     using any in-built modules (like `itertools`) available in python.
    
#     This part of the code is taken from SO (Jonathan R):
#     https://stackoverflow.com/a/54480126/6623589
    
#     :rtype:  array-like
#     :return: An array of all possible combination(s) from the given input
#              array. The array is unordered.
#     """
    
#     if len(array) == 0:
#         return [[]] # blank array
    
#     cs = []
#     for idx, elem in enumerate(combos(array[1:])):
#         cs += [elem, elem + [array[0]]]

#     return cs

# def get_sub_arr_sum(array : List[int]) -> List[int]:
#     idxs_ = [elem[0] for elem in array]
#     elems = [elem[1] for elem in array]
    
#     return idxs_, sum(elems)

# class Solution:
#     from itertools import combinations
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums = [(idx, value) for idx, value in enumerate(nums)]
#         print(nums, type(itertools.combinations))
#         # combinations = combos(nums)
#         combinations = list(combinations(nums, 2))
#         for combo in combinations:
#             idx, sum_ = get_sub_arr_sum(combo)
#             if sum_ == target:
#                 return idx
        
#         # for combo in combinations:
#         #     idx, sum_ = get_sub_arr_sum(combo)
#         #     if (sum_ == target) and len(idx) == 2:
#         #         return idx

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 