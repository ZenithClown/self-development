from bisect import bisect_left # https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs, n = sorted(zip(startTime, endTime, profit)), len(startTime)
        dp = [0] * (n + 1)
        
        for i in reversed(range(n)):
            k = bisect_left(jobs, jobs[i][1], key=lambda j: j[0])
            dp[i] = max(jobs[i][2] + dp[k], dp[i+1])
            
        return dp[0]