#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import * # noqa: F403 # pylint: disable=unused-import

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, value in enumerate(nums):
            remaining = target - nums[idx]

            if remaining in seen:
                return [idx, seen[remaining]]

            seen[value] = idx
# @lc code=end

