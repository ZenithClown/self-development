from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        lookup = {b : False for b in bank}
        
        q = deque([(start, 0)])
        while q:
            cur, level = q.popleft()
            if cur == end:
                return level
            
            for i in range(len(cur)):
                for c in ["A", "T", "G", "C"]:
                    if cur[i] == c:
                        continue
                        
                    next_ = cur[:i] + c + cur[i+1:]
                    if (next_ in lookup) and (lookup[next_] == False):
                        q.append((next_, level + 1))
                        lookup[next_] = True
                        
        return -1