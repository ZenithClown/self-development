class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = []
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                nc = c+grid[r][c]
                if not (0 <= nc < len(grid[0]) and grid[r][nc] == grid[r][c]):
                    c = -1
                    break
                c = nc
            result.append(c)
        return result