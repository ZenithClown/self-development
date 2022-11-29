class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        subseq = 0 # final subsequence count
        cnt = [defaultdict(int) for _ in range(len(nums))]
        
        for i,a in enumerate(nums):
            for j,b in enumerate(nums[:i]):
                cnt[i][a-b] += cnt[j][a-b] + 1
                subseq += cnt[j][a-b]
        
        return subseq