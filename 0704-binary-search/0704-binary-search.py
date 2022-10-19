class Solution:
    def binary(self, nums: List[int], target: int, start: int, end: int) -> int:
        # main algorithm to perform binary search
        middle = (start + end) // 2
        
        if end >= start:
            if nums[middle] == target:
                return middle

            # if the element is greater than `nums[middle]` then
            # the element can be present in the 'right subarray'
            elif nums[middle] < target:
                return self.binary(nums, target, middle + 1, end)

            # if the element is smaller than `nums[middle]` then
            # the element can be present in the 'left subarray'
            else:
                return self.binary(nums, target, start, middle - 1)
        
        else:
            # the element is not present
            return -1
        
        
    def search(self, nums: List[int], target: int) -> int:
        # since the data is sorted in ascending order,
        # thus we can get the `min` and `max` element as
        min_, max_ = nums[0], nums[-1]
        
        # directly send `-1` if the given target is not in
        # range (`min_`, `max_`)
        if (target < min_) or (target > max_):
            return -1
        
        # set index to search
        start, end = 0, len(nums) - 1
        return self.binary(nums, target, start, end)