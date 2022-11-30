from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict(Counter(arr)) # get the count of each element
        
        # the output is true given, the key and the count of
        # each key is same, i.e. we can
        return len(counts.keys()) == len(set(counts.values()))