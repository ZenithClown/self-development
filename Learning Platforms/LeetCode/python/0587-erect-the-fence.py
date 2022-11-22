class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort() # sort the keys by `x` values
        vector = [] # will return the final trees, not containing duplicates
        
        orient = lambda p, q, r : (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        
        for tree in trees + trees[::-1]:
            while (len(vector) >= 2) and (orient(vector[-2], vector[-1], tree) > 0):
                vector.pop()
                
            vector.append(tree)
            
        return list(set((xy[0], xy[1]) for xy in vector))