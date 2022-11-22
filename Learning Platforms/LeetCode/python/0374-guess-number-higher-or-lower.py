# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            # print(low, high)
            mid = low + (high - low) // 2
            res = guess(mid) # reqd. number
            if res == 0: return mid
            elif res < 0: high = mid - 1
            else: low = mid + 1
        
        return -1